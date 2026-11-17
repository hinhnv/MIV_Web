# Phòng chấm MIV 2026: bản tự chạy trên server

Trang chấm điểm 55 sản phẩm hạng mục *Sản phẩm công nghệ số tiềm năng* (bản build từ Artifact claude.ai), chạy bằng Docker sau **Cloudflare Tunnel** tại **https://miv2026.p-tech.xyz**. Giám khảo đăng nhập bằng tài khoản được cấp; điểm, ghi chú và góp ý lưu chung trên server và tự đồng bộ khoảng 3 giây một lần.

```
Trình duyệt ──HTTPS──> Cloudflare ──tunnel──> cloudflared (container, mạng host) ──> 127.0.0.1:3001 ──> web (container Node)
                                                                                                         └─ volume miv-data: tài khoản + điểm
```

| File | Vai trò |
|------|---------|
| `phong-cham-miv2026.html` | Trang chấm, đã gộp sẵn dữ liệu 55 sản phẩm + điểm AI. Không sửa tay. |
| `server.js` | Server Node (không có dependency): đăng nhập, API lưu điểm, quản lý tài khoản. |
| `claude-shim.js` | Thay `window.claude` của claude.ai bằng API của `server.js`, nên HTML giữ nguyên. |
| `login.html` | Trang đăng nhập. |
| `docker-compose.yml` | 2 service: `web` (cổng 3001, chỉ mở trên 127.0.0.1) và `tunnel` (cloudflared). |
| `deploy.sh` | Script triển khai/cập nhật một lệnh. |
| `.env.example` | Mẫu file `.env` (token tunnel, cổng). File `.env` thật **không** vào git. |
| `template.html`, `build_web.py` | Nguồn để build lại trang khi dữ liệu thay đổi (cần thư mục dữ liệu `E:\MIV2026` trên máy gốc). |

## Điều kiện

1. **Server Linux** có Docker Engine + Docker Compose v2 (`docker compose version` chạy được).
2. **Cloudflare Tunnel** đã có Public Hostname:
   `miv2026.p-tech.xyz` → Service **HTTP** → URL **`localhost:3001`**
   (Zero Trust › Networks › Tunnels › tunnel › Public Hostname). Container `tunnel` dùng mạng host nên `localhost:3001` trỏ đúng vào web.
3. Không cần mở cổng nào trên firewall: tunnel tự kết nối ra ngoài.

## Triển khai lần đầu

```bash
git clone <URL repo> phong-cham-miv && cd phong-cham-miv
sh deploy.sh
```

`deploy.sh` sẽ:
1. hỏi **token Cloudflare Tunnel** (dán chuỗi `eyJ...`, không hiện khi gõ) rồi lưu vào `.env` (quyền 600);
2. build và chạy 2 container, chờ web healthy;
3. nếu chưa có tài khoản nào thì hỏi tạo **tài khoản đầu tiên**;
4. in trạng thái và log tunnel. Mở https://miv2026.p-tech.xyz để đăng nhập.

Không muốn dùng script thì làm tay: `cp .env.example .env`, điền `TUNNEL_TOKEN`, rồi `docker compose up -d --build`.

## Quản lý tài khoản giám khảo

```bash
docker compose exec web node server.js user giamkhao1 '<mật khẩu ≥ 8 ký tự>' Giám khảo 1   # thêm mới / đổi mật khẩu / đổi tên
docker compose exec web node server.js list                                               # danh sách
docker compose exec web node server.js deluser giamkhao1                                  # xóa, mất quyền ngay
```

- Đổi mật khẩu thì các phiên đăng nhập cũ của người đó **bị đăng xuất**. Điểm đã chấm vẫn giữ (gắn với ID nội bộ, không gắn với tên).
- Không muốn mật khẩu nằm trong lịch sử shell: `printf '%s\n' '<mật khẩu>' | docker compose exec -T web node server.js user giamkhao1 - Giám khảo 1`.

## Cập nhật code / dữ liệu sản phẩm

```bash
git pull && sh deploy.sh
```

Muốn đổi dữ liệu sản phẩm thì chạy `build_web.py` trên máy có thư mục dữ liệu, commit file `phong-cham-miv2026.html` mới, rồi pull trên server. Tài khoản và điểm nằm trong volume `miv-data` nên **không mất** khi build lại.

## Sao lưu / khôi phục

```bash
docker compose cp web:/app/data ./backup-$(date +%F)            # sao lưu (users.json, judges.json, session-secret)
docker compose cp ./backup-2026-11-20/. web:/app/data/ && docker compose restart web   # khôi phục
```

Trong trang có mục **Xuất dữ liệu** (Excel/CSV/JSON) cho từng giám khảo.

## Vận hành

| Việc | Lệnh |
|------|------|
| Trạng thái | `docker compose ps` |
| Log (JSON) | `docker compose logs -f web` · `docker compose logs -f tunnel` |
| Khởi động lại | `docker compose restart` |
| Dừng | `docker compose down` (giữ dữ liệu; **không** thêm `-v` nếu không muốn xóa volume) |

Sau khi server khởi động lại, cả 2 container tự chạy lại (`restart: unless-stopped`).

## Bảo mật

- Web chỉ lắng nghe `127.0.0.1:3001`; ra Internet duy nhất qua tunnel, HTTPS do Cloudflare cấp. Cookie đăng nhập có `HttpOnly`, `SameSite=Lax`, `Secure`, hạn 30 ngày.
- Đăng nhập sai 10 lần trong 15 phút thì IP (lấy từ `CF-Connecting-IP`) bị khóa tạm.
- Header bảo mật: CSP, `X-Frame-Options: DENY`, HSTS, `nosniff`.
- **Token tunnel là bí mật**: ai có token đều chạy được connector cho domain này. Chỉ để trong `.env` trên server. Lộ token thì vào Cloudflare *Refresh token* rồi sửa `.env`, chạy lại `sh deploy.sh`.
- Repo chứa toàn bộ hồ sơ (có cả tài khoản dùng thử của thí sinh) và điểm AI: để repo ở chế độ **private**.
- Có thể thêm lớp **Cloudflare Access** (Zero Trust › Access › Applications) để chỉ email giám khảo mới vào được trang đăng nhập.
