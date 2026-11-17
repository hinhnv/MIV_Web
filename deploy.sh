#!/bin/sh
# Trien khai / cap nhat "Phong cham MIV 2026" tren server Linux co Docker.
#   sh deploy.sh
# Lan dau: hoi token Cloudflare Tunnel (luu vao .env) + tao tai khoan dau tien.
# Cac lan sau (sau khi git pull): build lai va khoi dong lai, du lieu giu nguyen.
set -eu
cd "$(dirname "$0")"

say() { printf '\n==> %s\n' "$*"; }
ask_secret() {
  printf '%s' "$1" >&2
  if [ -t 0 ]; then stty -echo; fi
  IFS= read -r v || v=""
  if [ -t 0 ]; then stty echo; printf '\n' >&2; fi
  printf '%s' "$v"
}

command -v docker >/dev/null 2>&1 || { echo "Chua cai Docker: https://docs.docker.com/engine/install/"; exit 1; }
docker compose version >/dev/null 2>&1 || { echo "Can Docker Compose v2 (lenh 'docker compose')."; exit 1; }

if ! grep -qs '^TUNNEL_TOKEN=..*' .env; then
  [ -t 0 ] || { echo "Chua co .env: tao tu .env.example (dien TUNNEL_TOKEN) roi chay lai."; exit 1; }
  say "Chua co file .env - nhap token Cloudflare Tunnel (chuoi bat dau bang eyJ...)"
  TOKEN=$(ask_secret "TUNNEL_TOKEN: ")
  [ -n "$TOKEN" ] || { echo "Token trong, dung lai."; exit 1; }
  ( umask 077; printf 'TUNNEL_TOKEN=%s\nWEB_PORT=3001\n' "$TOKEN" > .env )
  echo "Da luu .env (chi chu so huu doc duoc, khong vao git)."
fi

say "Build va khoi dong (web + tunnel)"
docker compose up -d --build

say "Cho web san sang"
i=0
until [ "$(docker inspect -f '{{.State.Health.Status}}' phong-cham-miv 2>/dev/null || echo none)" = "healthy" ]; do
  i=$((i + 1))
  if [ "$i" -gt 45 ]; then echo "Web chua san sang sau 90 giay. Xem log: docker compose logs web"; exit 1; fi
  sleep 2
done
echo "Web OK tai http://127.0.0.1:3001 (chi trong may chu)"

if [ "$(docker compose exec -T web node server.js count | tr -d '\r')" = "0" ]; then
  if [ -t 0 ]; then
    say "Chua co tai khoan nao - tao tai khoan dau tien"
    printf 'Ten dang nhap (a-z 0-9 . _ -): '; IFS= read -r U
    printf 'Ten hien thi: '; IFS= read -r NAME
    PW=$(ask_secret "Mat khau (toi thieu 8 ky tu): ")
    printf '%s\n' "$PW" | docker compose exec -T web node server.js user "$U" - "$NAME"
  else
    echo "Chua co tai khoan. Tao bang: docker compose exec web node server.js user <ten> '<mat khau>' <Ten hien thi>"
  fi
fi

say "Trang thai"
docker compose ps
sleep 3
docker compose logs --tail 5 tunnel || true
cat <<'EOF'

Xong: https://miv2026.p-tech.xyz
  Them/doi mat khau giam khao : docker compose exec web node server.js user <ten> '<mat khau>' <Ten hien thi>
  Xem danh sach tai khoan     : docker compose exec web node server.js list
  Log                         : docker compose logs -f
EOF
