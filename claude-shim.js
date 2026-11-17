// Thay the window.claude (runtime cua claude.ai) bang API cua server.js.
// Chi cai cac ham trang dang dung: user.me/can/profiles, db.collection().onSnapshot, db.doc().set, downloads.save.
(function () {
  "use strict";
  const POLL_MS = 3000;
  const err = code => Object.assign(new Error(code), { code });
  async function api(method, url, body) {
    let r;
    try { r = await fetch(url, { method, credentials: "same-origin", headers: body ? { "Content-Type": "application/json" } : {}, body: body ? JSON.stringify(body) : undefined }); }
    catch (e) { throw err("unavailable"); }
    if (r.status === 401) { location.href = "/login"; throw err("revoked"); }
    if (r.status === 403) throw err("invalid_argument");
    if (r.status === 413) throw err("quota_exceeded");
    if (r.status >= 500) throw err("unavailable");
    if (!r.ok) throw err("error_" + r.status);
    return r.status === 204 ? null : r.json();
  }

  let meP = null;
  const user = {
    me: () => (meP = meP || api("GET", "/api/me")).then(m => ({ id: m.id, name: m.name, avatarUrl: "" })),
    can: perm => (meP = meP || api("GET", "/api/me")).then(m => perm === "data.write" ? m.canWrite : false),
    profiles: () => api("GET", "/api/profiles").catch(() => ({})),
  };

  const db = {
    collection(name) {
      return {
        onSnapshot(cb, onErr) {
          let version = null, stopped = false;
          async function tick() {
            if (stopped) return;
            try {
              const s = await api("GET", "/api/" + name + (version == null ? "" : "?since=" + version));
              if (s) {
                version = s.version;
                cb({ metadata: { fromCache: false }, docs: Object.entries(s.docs).map(([id, d]) => ({ id, exists: true, data: () => d })) });
              }
            } catch (e) {
              if (e.code === "revoked") { stopped = true; if (onErr) onErr(e); return; }
              // loi mang tam thoi: giu du lieu dang co, thu lai o lan poll sau
            }
            setTimeout(tick, document.hidden ? POLL_MS * 5 : POLL_MS);
          }
          tick();
          return () => { stopped = true; };
        },
      };
    },
    doc(p) { return { set: body => api("PUT", "/api/" + p, body) }; },
  };

  const downloads = {
    async save({ filename, data }) {
      const blob = data instanceof Blob ? data : new Blob([data], { type: "text/plain;charset=utf-8" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob); a.download = filename;
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 10000);
    },
  };

  const caps = { user, db, downloads };
  window.claude = { use: async name => caps[name] || null };

  document.addEventListener("DOMContentLoaded", () => {
    const who = document.querySelector(".who");
    if (!who) return;
    const a = document.createElement("a");
    a.href = "/logout"; a.textContent = "Đăng xuất";
    a.style.cssText = "color:var(--hdr-muted);font-size:12.5px;margin-left:10px;white-space:nowrap";
    who.appendChild(a);
  });
})();
