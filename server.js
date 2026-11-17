// Server tu chay cho "Phong cham MIV 2026": dang nhap + luu diem giam khao vao file JSON.
// Trang HTML (ban build cua Artifact) giu nguyen; claude-shim.js thay the window.claude.
// Usage:
//   node server.js                                   -> chay web (PORT, mac dinh 3001)
//   node server.js user <username> <password> <ten>  -> them/sua tai khoan (password "-" = doc tu stdin)
//   node server.js deluser <username>                -> xoa tai khoan
//   node server.js list | count                      -> liet ke / dem tai khoan
"use strict";
const http = require("node:http");
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");

const ROOT = __dirname;
const DATA = process.env.DATA_DIR || path.join(ROOT, "data");
const PAGE = process.env.PAGE_FILE || path.join(ROOT, "phong-cham-miv2026.html");
const PORT = Number(process.env.PORT || 3001);
const USERS_F = path.join(DATA, "users.json");
const JUDGES_F = path.join(DATA, "judges.json");
const SECRET_F = path.join(DATA, "session-secret");
const SESSION_DAYS = 30;
const MAX_BODY = 4 * 1024 * 1024;

fs.mkdirSync(DATA, { recursive: true });
const readJson = (f, d) => { try { return JSON.parse(fs.readFileSync(f, "utf8")); } catch (e) { if (e.code === "ENOENT") return d; throw e; } };
const writeJson = (f, v) => { const t = f + ".tmp"; fs.writeFileSync(t, JSON.stringify(v)); fs.renameSync(t, f); };
const log = (action, fields = {}) => console.log(JSON.stringify({ t: new Date().toISOString(), action, ...fields }));

const hashPw = (pw, salt = crypto.randomBytes(16).toString("hex")) => salt + ":" + crypto.scryptSync(pw, salt, 32).toString("hex");
const checkPw = (pw, stored) => {
  const [salt, h] = String(stored).split(":"); if (!salt || !h) return false;
  return crypto.timingSafeEqual(Buffer.from(h, "hex"), crypto.scryptSync(pw, salt, 32));
};

/* ---------- CLI quan ly tai khoan ---------- */
const [cmd, ...args] = process.argv.slice(2);
if (cmd === "list" || cmd === "count") {
  const users = readJson(USERS_F, {});
  if (cmd === "count") console.log(Object.keys(users).length);
  else for (const [u, r] of Object.entries(users)) console.log(u + "\t" + r.name);
  process.exit(0);
}
if (cmd === "user" || cmd === "deluser") {
  const users = readJson(USERS_F, {});
  let [u, pw, ...name] = args;
  if (u) u = u.toLowerCase();
  if (pw === "-") { try { pw = fs.readFileSync(0, "utf8").split(/\r?\n/)[0]; } catch { pw = ""; } }
  if (!u || !/^[a-z0-9._-]{2,32}$/.test(u)) { console.error("username: 2-32 ky tu a-z 0-9 . _ -"); process.exit(1); }
  if (cmd === "deluser") { delete users[u]; }
  else {
    if (!pw || pw.length < 8) { console.error("password toi thieu 8 ky tu"); process.exit(1); }
    const prev = users[u] || {};
    users[u] = { id: prev.id || crypto.randomUUID(), name: name.join(" ") || prev.name || u, pw: hashPw(pw), canWrite: true };
  }
  writeJson(USERS_F, users);
  console.log(cmd === "deluser" ? "da xoa " + u : "da luu " + u + " (" + users[u].name + ")");
  process.exit(0);
}
if (cmd) { console.error("lenh khong hop le: " + cmd); process.exit(1); }

/* ---------- session cookie ky HMAC ---------- */
let secret = process.env.SESSION_SECRET;
if (!secret) { try { secret = fs.readFileSync(SECRET_F, "utf8"); } catch { secret = crypto.randomBytes(32).toString("hex"); fs.writeFileSync(SECRET_F, secret); } }
const sign = s => crypto.createHmac("sha256", secret).update(s).digest("base64url");
// pwTag: doi mat khau -> moi phien dang nhap cu het hieu luc
const pwTag = rec => crypto.createHash("sha256").update(String(rec.pw)).digest("base64url").slice(0, 10);
const makeCookie = (uname, rec) => { const v = Buffer.from(uname).toString("base64url") + "." + (Date.now() + SESSION_DAYS * 864e5) + "." + pwTag(rec); return v + "." + sign(v); };
function sessionUser(req) {
  const m = /(?:^|;\s*)sid=([^;]+)/.exec(req.headers.cookie || ""); if (!m) return null;
  const [u, exp, tag, sig] = m[1].split("."); if (!u || !exp || !tag || !sig) return null;
  const want = sign(u + "." + exp + "." + tag);
  if (sig.length !== want.length || !crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(want)) || Date.now() > Number(exp)) return null;
  const uname = Buffer.from(u, "base64url").toString();
  const rec = readJson(USERS_F, {})[uname];
  return rec && pwTag(rec) === tag ? { uname, ...rec } : null; // xoa tai khoan / doi mat khau -> mat phien ngay
}
const isHttps = req => req.headers["x-forwarded-proto"] === "https";
const cookieAttrs = req => "; Path=/; HttpOnly; SameSite=Lax" + (isHttps(req) ? "; Secure" : "");

/* ---------- chong do mat khau: 10 lan sai / 15 phut / IP ---------- */
// ponytail: dem trong RAM, reset khi restart container; du cho vai chuc nguoi dung noi bo
const fails = new Map();
// Sau Cloudflare: CF-Connecting-IP do Cloudflare dat, client khong gia mao duoc (X-Forwarded-For thi gia duoc phan dau).
// Cong web chi mo tren 127.0.0.1 nen moi request deu di qua tunnel.
const ipOf = req => String(req.headers["cf-connecting-ip"] || req.socket.remoteAddress || "").trim();
const blocked = ip => { const f = fails.get(ip); return f && f.n >= 10 && Date.now() - f.at < 15 * 6e4; };
const fail = ip => { const f = fails.get(ip); fails.set(ip, f && Date.now() - f.at < 15 * 6e4 ? { n: f.n + 1, at: f.at } : { n: 1, at: Date.now() }); };

/* ---------- du lieu cham ---------- */
let store = readJson(JUDGES_F, { version: 0, docs: {} });

/* ---------- trang ---------- */
const HEAD = '<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><script src="/claude-shim.js"></script>';
const SHIM = fs.readFileSync(path.join(ROOT, "claude-shim.js"));
const LOGIN = fs.readFileSync(path.join(ROOT, "login.html"), "utf8");
const pageHtml = () => HEAD + fs.readFileSync(PAGE, "utf8"); // doc lai moi lan: thay file HTML khong can restart

// Trang dung script/style inline + Google Fonts + SheetJS (cdnjs) khi xuat Excel.
const CSP = [
  "default-src 'self'",
  "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://static.cloudflareinsights.com",
  "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
  "font-src 'self' https://fonts.gstatic.com",
  "img-src 'self' data: blob:",
  "connect-src 'self' https://cloudflareinsights.com",
  "frame-ancestors 'none'", "form-action 'self'", "base-uri 'self'",
].join("; ");
function send(res, code, body, type = "application/json; charset=utf-8", extra = {}) {
  const sec = { "X-Content-Type-Options": "nosniff", "Referrer-Policy": "same-origin", "X-Frame-Options": "DENY", "Content-Security-Policy": CSP };
  if (res.req && isHttps(res.req)) sec["Strict-Transport-Security"] = "max-age=15552000";
  res.writeHead(code, { "Content-Type": type, "Cache-Control": "no-store", ...sec, ...extra });
  res.end(typeof body === "string" || Buffer.isBuffer(body) ? body : JSON.stringify(body));
}
function readBody(req) {
  return new Promise((ok, bad) => {
    let n = 0; const chunks = [];
    req.on("data", c => { n += c.length; if (n > MAX_BODY) { bad(Object.assign(new Error("too large"), { status: 413 })); req.destroy(); } else chunks.push(c); });
    req.on("end", () => ok(Buffer.concat(chunks).toString("utf8")));
    req.on("error", bad);
  });
}

async function route(req, res) {
  const url = new URL(req.url, "http://x");
  const p = url.pathname;
  if (p === "/healthz") return send(res, 200, { ok: true });
  if (p === "/claude-shim.js") return send(res, 200, SHIM, "text/javascript; charset=utf-8");

  if (p === "/login" && req.method === "GET") return send(res, 200, LOGIN, "text/html; charset=utf-8");
  if (p === "/login" && req.method === "POST") {
    const ip = ipOf(req);
    if (blocked(ip)) { log("login_blocked", { ip }); return send(res, 302, "", "text/plain", { Location: "/login?e=2" }); }
    const f = new URLSearchParams(await readBody(req));
    const uname = String(f.get("u") || "").trim().toLowerCase();
    const rec = readJson(USERS_F, {})[uname];
    if (!rec || !checkPw(String(f.get("p") || ""), rec.pw)) {
      fail(ip); log("login_failed", { ip, user: uname });
      return send(res, 302, "", "text/plain", { Location: "/login?e=1" });
    }
    fails.delete(ip); log("login_ok", { ip, user: uname });
    return send(res, 302, "", "text/plain", { Location: "/", "Set-Cookie": "sid=" + makeCookie(uname, rec) + cookieAttrs(req) + "; Max-Age=" + SESSION_DAYS * 86400 });
  }
  if (p === "/logout") return send(res, 302, "", "text/plain", { Location: "/login", "Set-Cookie": "sid=" + cookieAttrs(req) + "; Max-Age=0" });

  const me = sessionUser(req);
  if (!me) return p.startsWith("/api/") ? send(res, 401, { error: "unauthenticated" }) : send(res, 302, "", "text/plain", { Location: "/login" });

  if (p === "/" && req.method === "GET") return send(res, 200, pageHtml(), "text/html; charset=utf-8");
  if (p === "/api/me") return send(res, 200, { id: me.id, name: me.name, canWrite: me.canWrite !== false });
  if (p === "/api/profiles") {
    const out = {}; for (const u of Object.values(readJson(USERS_F, {}))) out[u.id] = { name: u.name, avatarUrl: "" };
    return send(res, 200, out);
  }
  if (p === "/api/judges" && req.method === "GET") {
    if (url.searchParams.get("since") === String(store.version)) return send(res, 204, "");
    return send(res, 200, store);
  }
  const m = /^\/api\/judges\/([\w-]+)$/.exec(p);
  if (m && req.method === "PUT") {
    if (m[1] !== me.id || me.canWrite === false) { log("judge_save_forbidden", { user: me.uname, doc: m[1] }); return send(res, 403, { error: "forbidden" }); }
    let doc; try { doc = JSON.parse(await readBody(req)); } catch (e) { if (e.status) throw e; return send(res, 400, { error: "bad json" }); }
    if (!doc || typeof doc !== "object" || Array.isArray(doc)) return send(res, 400, { error: "bad doc" });
    const next = { version: store.version + 1, docs: { ...store.docs, [me.id]: doc } };
    writeJson(JUDGES_F, next); store = next; // ghi file xong moi doi state: loi ghi -> client thay loi, khong mat du lieu cu
    log("judge_saved", { user: me.uname, version: store.version, scored: Object.keys(doc.scores || {}).length });
    return send(res, 200, { version: store.version });
  }
  return send(res, 404, { error: "not found" });
}

const server = http.createServer((req, res) => {
  route(req, res).catch(e => {
    log("request_failed", { method: req.method, url: req.url, error: String(e && e.stack || e) });
    if (!res.headersSent) send(res, e.status || 500, { error: e.status === 413 ? "too large" : "server error" });
  });
}).listen(PORT, () => log("server_started", { port: PORT, users: Object.keys(readJson(USERS_F, {})).length }));
// docker stop gui SIGTERM: ghi file la dong bo nen dung ngay duoc, khong mat du lieu
for (const sig of ["SIGTERM", "SIGINT"]) process.on(sig, () => { log("server_stopping", { sig }); server.close(() => process.exit(0)); setTimeout(() => process.exit(0), 3000).unref(); });
