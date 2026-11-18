"""Bo nguong dinh luong v3 cho trang cham: dinh nghia thanh phan (hien tren trang) + goi y diem tu so lieu da trich.
Nguon: E:\\MIV2026\\_nguong_dinh_luong\\nguong_de_xuat_v3_ban_cuoi.md (ban day du, thu ky giu).
Goi y chi cho thanh phan [DL] co so lieu, da ap tran tu khai; giam khao phai xac minh.
"""

# k: khoa; l: nhan; t: DL (tra bang) / BC (bac bang chung) / CM (chuyen mon); m: diem toi da; b: [tu, den, mo ta]; n: ghi chu
V3 = {
    1: {"parts": [
        {"k": "A", "l": "Mức khác biệt", "t": "CM", "m": 9, "b": [
            [8, 9, "Chưa có SP tương đương tại VN và khác biệt rõ với giải pháp quốc tế, có bằng chứng"],
            [6, 7, "Khác biệt rõ trong phân khúc tại VN"], [4, 5, "Cải tiến gia tăng trên nhóm SP đã phổ biến"],
            [2, 3, "Khác biệt chủ yếu ở giá/đóng gói"], [0, 1, "Phổ thông"]],
         "n": "Nếu SP tương đương tại VN nằm trong danh sách đối thủ hiển nhiên thì tối đa 7."},
        {"k": "B", "l": "Chất lượng so sánh", "t": "BC", "m": 4, "b": [
            [4, 4, "≥3 đối thủ thật (≥1 quốc tế, ≥1 trong nước), ≥3 tiêu chí đo được, có nguồn"],
            [3, 3, "≥2 đối thủ có tên, so từng đối thủ theo ≥3 tiêu chí, chưa có số"],
            [2, 2, "1 đối thủ có tên, so trên ≥2 tiêu chí cụ thể"], [1, 1, "Chỉ nêu tên đối thủ, nhận xét chung"], [0, 0, "Không so sánh"]],
         "n": "Trừ 1 nếu bỏ sót đối thủ hiển nhiên. Người đi đầu (A ≥ 8, không có đối thủ trực tiếp) so với giải pháp thay thế gần nhất: 3."},
        {"k": "C", "l": "Xu hướng", "t": "CM", "m": 4, "b": [
            [4, 4, "Định hình xu hướng đang hình thành, có dẫn chứng"], [3, 3, "Phù hợp xu hướng chính, ứng dụng cụ thể"],
            [1, 2, "Chỉ liên hệ chung"], [0, 0, "Không có"]]},
        {"k": "D", "l": "Ghi nhận độc lập cho chính SP", "t": "DL", "m": 3, "b": [
            [3, 3, "Giải cấp bộ / hiệp hội toàn quốc / quốc tế có hội đồng, trao cho chính SP trong 3 năm"],
            [2, 2, "Lọt chung kết/top chương trình có tuyển chọn"], [1, 1, "Giải địa phương, hoặc giải của công ty/SP khác"],
            [0, 0, "Không có, giải thu phí, vinh danh truyền thông"]]},
    ]},
    2: {"parts": [
        {"k": "S1", "l": "Công nghệ lõi & mức làm chủ", "t": "BC", "m": 5, "b": [
            [5, 5, "Như 4, thêm kiểm chứng độc lập (công bố có phản biện, bên thứ ba, repo có cộng đồng)"],
            [4, 4, "Có cả SBOM lẫn số đo; lõi chiến lược tự xây, có số liệu vận hành thật"],
            [3, 3, "Kiến trúc + SBOM hoặc số tự đo đủ 4 điều kiện"],
            [2, 2, "Có sơ đồ kiến trúc, mô tả thành phần (phần AI gọi API ngoài: tối đa 2)"],
            [1, 1, "Chỉ liệt kê tên công nghệ"], [0, 0, "Không mô tả"]]},
        {"k": "S2", "l": "Độ tin cậy", "t": "BC", "m": 3, "b": [
            [3, 3, "Uptime ≥99,5% đo ≥90 ngày bằng công cụ bên ngoài; nghiệm thu vận hành có số; kiểm định"],
            [2, 2, "Production ≥3 tháng có số quy mô; HA có cấu hình; SLA trong hợp đồng có phạt"],
            [1, 1, "Tuyên bố, cam kết suông"], [0, 0, "Không đề cập / chỉ kế hoạch"]]},
        {"k": "S3", "l": "Tiện lợi", "t": "BC", "m": 3, "b": [
            [3, 3, "Kiểm thử người dùng có cỡ mẫu và chỉ số (SUS, tỷ lệ hoàn thành)"],
            [2, 2, "≥2/3: ảnh giao diện thật, luồng thao tác có số bước, tài liệu hướng dẫn"],
            [1, 1, "Tuyên bố"], [0, 0, "Không đề cập"]]},
        {"k": "S4", "l": "Hiệu năng", "t": "BC", "m": 3, "b": [
            [3, 3, "Giám khảo tái lập được (PageSpeed, benchmark công bố) hoặc bên thứ ba/khách hàng đo và ký"],
            [2, 2, "Số tự đo đủ 4 điều kiện (p95/thông lượng, độ chính xác tập tách riêng, crash <1,09%)"],
            [1, 1, "Số không kèm điều kiện đo"], [0, 0, "Không đề cập / chỉ tiêu thiết kế"]]},
        {"k": "S5", "l": "Bảo trì, bảo hành", "t": "BC", "m": 3, "b": [
            [3, 3, "≥4 bản phát hành công khai/12 tháng; số liệu hỗ trợ có xác nhận; ISO 20000-1 gồm SP"],
            [2, 2, "Quy trình hỗ trợ có thời gian phản hồi; CI/kiểm thử tự động có số; lịch sử phiên bản"],
            [1, 1, "Tuyên bố"], [0, 0, "Không đề cập"]]},
        {"k": "S6", "l": "An toàn, bảo mật của chính SP", "t": "BC", "m": 3, "b": [
            [3, 3, "Pentest bên thứ ba ≤12 tháng; ISO 27001 phạm vi gồm SP; hồ sơ cấp độ HTTT được duyệt"],
            [2, 2, "Biện pháp cụ thể (mã hóa, phân quyền, nhật ký); quét lỗ hổng nội bộ; giấy phép KD ATTT"],
            [1, 1, "Tuyên bố"], [0, 0, "Không đề cập"]],
         "n": "Chức năng bảo mật SP cung cấp cho khách chấm ở TC1/TC4, không chấm ở đây."},
    ]},
    3: {"cap": 10, "parts": [
        {"k": "P", "l": "Đường chứng minh cao nhất (chọn một)", "t": "DL", "m": 8, "b": [
            [8, 8, "P1: sáng chế / GPHI / thiết kế bố trí đã cấp, bao phần lõi"],
            [7, 7, "P2: GCN quyền tác giả đúng SP / HĐ KH&CN nghiệm thu / GCN DN KH&CN có tên SP; hoặc P3 thuyết minh đủ 4 yếu tố"],
            [5, 6, "P3 đủ 3 yếu tố; P4 đã nộp đơn có số; kiểu dáng phần cứng đã cấp"],
            [3, 4, "P3 có 1–2 yếu tố; kiểu dáng phần cứng đã nộp đơn"],
            [2, 2, "P5: chỉ cam kết/tuyên bố"], [0, 1, "Nhãn hiệu (đơn 4-…), văn bằng của phần mềm khác, không có"]],
         "n": "Trần 3 nếu lõi là white-label/bán lại/thuê nước ngoài. Mã nguồn mở không bị trừ."},
        {"k": "X", "l": "Điểm cộng", "t": "DL", "m": 2, "b": [
            [2, 2, "Có thêm bằng chứng độc lập ≥5 điểm và tác giả là người Việt của đơn vị"],
            [1, 1, "Một trong hai"], [0, 0, "Không"]]},
    ]},
    4: {"parts": [
        {"k": "A", "l": "Bằng chứng sử dụng & hài lòng", "t": "DL", "m": 3, "b": [
            [3, 3, "Gia hạn/giữ chân có chứng từ; NPS/CSAT có phương pháp (n≥30); ≥4,3★ với ≥100 đánh giá; ≥2 xác nhận khách độc lập"],
            [2, 2, "1 xác nhận độc lập; nghiệm thu/case study có số trước–sau; giữ chân tự khai có định nghĩa"],
            [1, 1, "Case study tự viết có tên khách"], [0, 0, "Không có / chỉ tự khen / chưa có người dùng"]]},
        {"k": "B", "l": "Tương thích, mở rộng", "t": "DL", "m": 2, "b": [
            [2, 2, "API/SDK công khai có tài liệu và ≥3 tích hợp tự phát triển; hoặc ≥2 chuẩn mở ngành"],
            [1, 1, "API có tài liệu (không công khai), hoặc ≥1 tích hợp tự phát triển đang chạy"], [0, 0, "Không có"]]},
        {"k": "C", "l": "Đa nền tảng, tùy biến", "t": "DL", "m": 2, "b": [
            [2, 2, "≥2 nền tảng (hoặc ≥2 mô hình triển khai) và tùy biến không cần sửa mã"],
            [1, 1, "Đạt một trong hai"], [0, 0, "Không"]], "n": "\"Web\" + \"cloud\" của cùng một SaaS tính là 1."},
        {"k": "D", "l": "Trải nghiệm theo giao thức dùng thử", "t": "CM", "m": 3, "b": [
            [3, 3, "Cả 3 tác vụ chạy đúng, mượt"], [2, 2, "2/3 tác vụ đúng, hoặc đủ 3 còn lỗi nhỏ, hoặc video liền mạch đủ 3"],
            [1, 1, "1 tác vụ, chỉ ảnh chụp, hoặc DN không cung cấp tài khoản/video"], [0, 0, "Không xem được SP chạy"]]},
    ]},
    5: {"parts": [
        {"k": "A", "l": "Mức cấp thiết", "t": "CM", "m": 5, "b": [
            [5, 5, "Lớn, cấp bách, ảnh hưởng diện rộng"], [4, 4, "Rõ ràng, có ý nghĩa với một ngành/nhóm lớn"],
            [3, 3, "Có ích cho một phân khúc"], [1, 2, "Mơ hồ / nhu cầu \"có thì tốt\""], [0, 0, "Không thuyết minh"]]},
        {"k": "B", "l": "Lượng hóa quy mô bài toán", "t": "DL", "m": 2, "b": [
            [2, 2, "Số đối tượng đang gặp vấn đề từ cơ quan nhà nước, tổ chức quốc tế, hiệp hội, bài báo có phản biện"],
            [1, 1, "Báo cáo thương mại hoặc số không nguồn"], [0, 0, "Định tính"]]},
        {"k": "C", "l": "Chính sách", "t": "DL", "m": 1, "b": [
            [1, 1, "Trích điều, khoản hoặc chỉ tiêu cụ thể mà SP đáp ứng"], [0, 0, "Chỉ nêu tên văn bản / không có"]]},
        {"k": "D", "l": "Bằng chứng nhu cầu", "t": "DL", "m": 2, "b": [
            [2, 2, "≥3 LOI/biên bản thí điểm/thư xác nhận của tổ chức có tên, hoặc khảo sát ≥100 người có phương pháp"],
            [1, 1, "1–2 bằng chứng như trên"], [0, 0, "Không có"]], "n": "Hợp đồng có trả phí tính ở TC6-A."},
    ]},
    6: {"parts": [
        {"k": "A", "l": "Lực kéo thị trường", "t": "DL", "m": 6, "b": [
            [6, 6, "Nhà nước/HĐ ≥300tr ≥30 · tổ chức khác ≥300 · cá nhân trả phí ≥10.000 (cần chứng từ)"],
            [5, 5, "Nhà nước 10–29 · tổ chức 100–299 · cá nhân 2.000–9.999 · miễn phí ≥100.000"],
            [4, 4, "Nhà nước 3–9 · tổ chức 30–99 · cá nhân 500–1.999 · miễn phí 10.000–99.999"],
            [3, 3, "Nhà nước 1–2 · tổ chức 10–29 · cá nhân 100–499 · miễn phí 2.000–9.999"],
            [2, 2, "Tổ chức 3–9 · cá nhân 1–99 · miễn phí 500–1.999"],
            [1, 1, "Thí điểm có biên bản · tổ chức 1–2 · miễn phí 1–499"], [0, 0, "Không có"]],
         "n": "Đếm khách trả phí còn hiệu lực tại ngày nộp; lấy thang cho điểm cao nhất. Chưa rõ trả phí −1, dùng thử −2."},
        {"k": "B", "l": "Tăng trưởng doanh thu SP 2025/2024", "t": "DL", "m": 2, "b": [
            [2, 2, "≥40% (cần chứng từ)"], [1, 1, "20–39%, hoặc ≥40% nhưng doanh thu 2024 dưới 0,1 tỷ"],
            [0, 0, "Dưới 20%, giảm, chưa đủ 2 năm"]]},
        {"k": "C", "l": "Quy mô thị trường", "t": "DL", "m": 2, "b": [
            [2, 2, "SOM từ dưới lên kèm thị phần hiện tại"], [1, 1, "TAM/SAM của thị trường mục tiêu có nguồn"],
            [0, 0, "Không có / không nguồn / số toàn cầu chung chung"]]},
        {"k": "D", "l": "Mô hình & chiến lược kinh doanh", "t": "CM", "m": 5, "b": [
            [5, 5, "Bảng giá, kênh bán vận hành, phân khúc, kế hoạch có mốc, chỉ số đơn vị từ số thực"],
            [4, 4, "Như 5 nhưng chỉ số đơn vị tự khai"], [3, 3, "Có giá, kênh, phân khúc, kế hoạch mở rộng"],
            [2, 2, "Có giá và kênh bán"], [1, 1, "Mô tả chung"], [0, 0, "Không có"]]},
    ]},
    7: {"parts": [
        {"k": "A", "l": "Doanh thu sản phẩm", "t": "DL", "m": 3, "b": [
            [3, 3, "≥10 tỷ (cần chứng từ)"], [2, 2, "1–<10 tỷ"], [1, 1, "0,1–<1 tỷ"], [0, 0, "Dưới 0,1 tỷ / chưa có"]],
         "n": "Doanh thu năm 2025 của chính SP; số của công ty chỉ dùng khi SP chiếm ≥70% và đã bán ≥12 tháng."},
        {"k": "B", "l": "Quy mô sử dụng", "t": "DL", "m": 1, "b": [
            [1, 1, "≥500 người dùng hoạt động hoặc ≥5 tổ chức đang dùng"], [0, 0, "Chưa đạt"]]},
        {"k": "C", "l": "Tác động hoặc giá cạnh tranh", "t": "DL", "m": 1, "b": [
            [1, 1, "Tác động lượng hóa có xác nhận; hoặc giá thấp hơn ≥30% SP nước ngoài, có báo giá đối chiếu"],
            [0, 0, "Không có"]]},
    ]},
    8: {"parts": [
        {"k": "A", "l": "Mở rộng quốc tế", "t": "DL", "m": 5, "b": [
            [5, 5, "Doanh thu nước ngoài ≥10% hoặc khách trả phí ≥2 nước, và ≥0,1 tỷ/24 tháng (cần chứng từ)"],
            [4, 4, "Khách trả phí hoặc thí điểm có biên bản ở ≥1 nước"],
            [3, 3, "Thỏa thuận văn bản với đối tác/nhà phân phối; pháp nhân/nhãn hiệu ở nước ngoài; marketplace quốc tế"],
            [2, 2, "Kế hoạch đủ: tên nước, năm bắt đầu, ngân sách hoặc nhân sự"], [1, 1, "Chỉ nêu định hướng"], [0, 0, "Không đề cập"]],
         "n": "Đơn vị cùng tập đoàn ở nước ngoài không tính cho bậc 3–5."},
    ]},
    9: {"parts": [
        {"k": "A", "l": "Vốn bên ngoài đã nhận", "t": "DL", "m": 3, "b": [
            [3, 3, "Quỹ/nhà đầu tư thiên thần có tên, ≥2,6 tỷ, trong 36 tháng, có chứng từ"],
            [2, 2, "Vốn ngoài nhỏ hơn hoặc cũ hơn; BCTC thể hiện vốn góp ngoài; term sheet đã ký"],
            [1, 1, "Tài trợ/giải tiền mặt cạnh tranh; ươm tạo có văn bản; đầu tư chuyển đổi"],
            [0, 0, "Vốn sáng lập, ngân sách tập đoàn, vay ngân hàng"]]},
        {"k": "B", "l": "Sức hấp dẫn đầu tư (mỗi tín hiệu 1 điểm)", "t": "DL", "m": 2, "b": [
            [2, 2, "≥2 tín hiệu"], [1, 1, "1 tín hiệu"], [0, 0, "Không có"]],
         "n": "Tín hiệu: kế hoạch gọi vốn có số tiền, phân bổ, mốc; có lãi/dòng tiền dương 2025 theo BCTC; GCN khởi nghiệp sáng tạo; LOI/đàm phán với nhà đầu tư có tên."},
    ]},
}

RULES = [
    "Kỳ số liệu: doanh thu năm 2025 (dưới 0,1 tỷ hoặc ra mắt sau 2025 thì lấy số lớn hơn giữa 2025 và 2026 tới ngày nộp, không quy ra cả năm); khách hàng, người dùng là số đang dùng tại ngày nộp; không dùng kế hoạch, trừ TC8 bậc 1–2 và TC9 tín hiệu kế hoạch.",
    "Mức bằng chứng: K = tài liệu bên thứ ba hoặc cùng ký, hoặc tra cứu công khai được; T = tự khai (kể cả nêu tên khách không kèm tài liệu). Bậc cao nhất của TC6-A, TC6-B, TC7-A, TC8 và nhánh gia hạn TC4-A cần K; số T tối đa bậc liền dưới.",
    "Số liệu mâu thuẫn (cùng chỉ tiêu, cùng kỳ): K thắng T; còn lại lấy số nhỏ hơn, chênh hơn 2 lần mà không có chứng từ thì hạ thêm 1 bậc; tổng không khớp các thành phần thì dùng tổng thành phần.",
    "Số của công ty chỉ dùng khi sản phẩm là nguồn thu chính (≥70%) và đã bán ≥12 tháng; còn lại coi số của sản phẩm bằng 0.",
    "Khách hàng, doanh thu, đối tác, vốn từ công ty cùng tập đoàn không tính ở TC5-D, TC6-A, TC7, TC8, TC9.",
    "Một khẳng định chỉ cho điểm ở một chỗ: văn bằng, GCN DN KH&CN → TC3; thư đánh giá, gia hạn → TC4-A; LOI, thí điểm → TC5-D; hợp đồng trả phí → TC6-A; tăng trưởng → TC6-B; giải thưởng → TC1-D.",
    "Chấm phần chuyên môn [CM] trước khi xem điểm AI; nghi vấn tư cách dự thi không làm đổi điểm (đánh dấu cho Ban tổ chức).",
    "Ghi vào Ghi chú cho mỗi số đã dùng: TCx-thành phần | giá trị | kỳ | K/T | nguồn (file, trang) | quy tắc đã áp.",
]

# Sua phan loai SHTT da phat hien khi review (nhan hieu / kieu dang / van bang cua phan mem khac / sang che)
SHTT_FIX = {49: ("khong", "Chỉ có nhãn hiệu eClick, không phải văn bằng phần mềm"),
            19: ("khong", "GCN 2019 cấp cho phần mềm khác (bộ điều khiển nhà thông minh)"),
            2: ("khong", "Đơn nhãn hiệu (4-…)"), 6: ("khong", "Đơn nhãn hiệu (4-…)"), 32: ("khong", "Đơn nhãn hiệu (4-…)"),
            35: ("khong", "Số đơn dạng nhãn hiệu (VN-4-…)"), 14: ("khong", "Đơn nhãn hiệu và kiểu dáng; quyền tác giả đang làm thủ tục"),
            36: ("sang_che", "Có bằng sáng chế US")}
EXTRA = {20: {3: "Hai đơn sáng chế dùng chung với STT 54 (cùng công ty): chỉ tính cho một sản phẩm."},
         54: {3: "Hai đơn sáng chế dùng chung với STT 20 (cùng công ty): chỉ tính cho một sản phẩm."},
         50: {7: "Doanh thu 2025 theo quy tắc mâu thuẫn là 0,124 tỷ (metrics ghi 0,184)."},
         26: {5: "Chưa thấy LOI/biên bản thí điểm dù metrics ghi 2 xác nhận."},
         33: {5: "Chưa thấy LOI/biên bản thí điểm dù metrics ghi 2 xác nhận.", 7: "Hợp đồng Trí Nam để trống ngày ký: mức T."}}
KE_HOACH_VON = {1, 6, 18, 32, 33, 46, 51}  # doc tay: co ke hoach goi von neu so tien


def _n(x):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) else None


def _f(x, d=2):
    if x is None: return "—"
    s = f"{x:,.{d}f}".rstrip("0").rstrip(".") if isinstance(x, float) else f"{x:,}"
    return s.replace(",", " ").replace(".", ",").replace(" ", ".")


def _ladder(v, steps):
    if v is None: return 0
    for th, pt in steps:
        if v >= th: return pt
    return 0


def suggest(r):
    """Goi y diem cho cac thanh phan [DL] (da ap tran tu khai: TC6-A <=5, TC6-B <=1, TC7-A <=2, TC8 <=4)."""
    stt = r["stt"]; s = {}
    shtt = SHTT_FIX.get(stt, (r.get("shtt"),))[0]
    path = 8 if shtt == "sang_che" else 7 if shtt == "da_cap" else 5 if shtt == "da_nop" else 0
    lo = r.get("loi_tu_phat_trien")
    p3 = {"co_thuyet_minh": 5, "mot_phan": 3, "khong_ro": 2}.get(lo, 2)
    P = max(path, p3)
    s[3] = {"P": min(P, 3) if lo == "white_label" else P}
    nt, api = _n(r.get("so_tich_hop")) or 0, bool(r.get("api_cong_khai"))
    tk = {str(x).lower() for x in (r.get("trien_khai") or [])}
    nen_tang = len(tk & {"web", "mobile", "ios", "android", "desktop"}) >= 2 or {"cloud", "on-premise"} <= tk
    s[4] = {"B": 2 if (api and nt >= 3) else 1 if (nt >= 1 or api) else 0, "C": 1 if nen_tang else 0}
    xn = _n(r.get("xac_nhan_nhu_cau"))
    s[5] = {"B": {"co_nguon": 2, "khong_nguon": 1}.get(r.get("bai_toan_luong_hoa"), 0),
            "C": 1 if r.get("dan_chieu_chinh_sach") else 0, "D": _ladder(xn, [[3, 2], [1, 1]])}
    kh, tc, nd = _n(r.get("khach_hang_tra_phi")), _n(r.get("to_chuc_su_dung")), _n(r.get("nguoi_dung"))
    dt = _n(r.get("doanh_thu_ty"))
    lon = r.get("loai_khach") == "B2G" or bool(kh and dt and dt / kh >= 0.3)
    T = [[30, 6], [10, 5], [3, 4], [1, 3]]
    S = [[300, 6], [100, 5], [30, 4], [10, 3], [3, 2], [1, 1]]
    C2 = [[100000, 5], [10000, 4], [2000, 3], [500, 2], [1, 1]]
    cand = []
    if kh: cand.append(_ladder(kh, T if lon else S))
    if tc and tc > (kh or 0): cand.append(max(_ladder(tc, T if lon else S) - 1, 0))
    if nd: cand.append(_ladder(nd, C2))
    g = _n(r.get("tang_truong_pct"))
    b6 = 0
    if g is not None and dt:
        nen = dt - dt * g / (100 + g)
        b6 = 2 if g >= 40 else 1 if g >= 20 else 0
        if b6 == 2 and nen < 0.1: b6 = 1
    s[6] = {"A": min(max(cand) if cand else 0, 5), "B": min(b6, 1), "C": 1 if r.get("tam_sam_som") == "co_nguon" else 0}
    a7 = 0 if not dt else 3 if dt >= 10 else 2 if dt >= 1 else 1 if dt >= 0.1 else 0
    s[7] = {"A": min(a7, 2), "B": 1 if ((nd or 0) >= 500 or (tc or 0) >= 5) else 0,
            "C": 1 if (_n(r.get("gia_re_hon_ngoai_pct")) or 0) >= 30 else 0}
    s[8] = {"A": min(_n(r.get("quoc_te_muc")) or 0, 4)}
    vl, v = r.get("von_loai"), _n(r.get("von_ty"))
    a9 = 3 if (vl in ("quy", "thien_than") and v and v >= 2.6) else 2 if vl in ("quy", "thien_than") else 1 if vl == "uom_tao_tai_tro" else 0
    cn = " ".join(r.get("chung_nhan") or []).lower()
    b9 = (1 if stt in KE_HOACH_VON else 0) + (1 if "khởi nghiệp" in cn else 0) + (1 if vl == "dang_dam_phan" else 0)
    s[9] = {"A": a9, "B": min(b9, 2)}
    return s


BC_TXT = {"kiem_chung": "kiểm chứng", "tu_khai": "tự khai", "khong": "không có"}


def facts(r):
    """Cac so lieu da trich, chia theo tieu chi (hien de giam khao doi chieu)."""
    stt = r["stt"]; f = {t: [] for t in range(1, 10)}
    add = lambda t, k, v: f[t].append([k, v])
    add(1, "Đối thủ được so sánh", f"{_f(_n(r.get('so_doi_thu_so_sanh')) or 0)}" + (" (có quốc tế)" if r.get("co_doi_thu_quoc_te") else ""))
    if r.get("giai_thuong"): add(1, "Giải thưởng", "; ".join(map(str, r["giai_thuong"])))
    if r.get("dau_tien_vn"): add(1, "Tự nhận", "Đầu tiên tại VN (cần cách rà soát)")
    if r.get("chung_nhan"): add(2, "Chứng nhận", "; ".join(map(str, r["chung_nhan"])))
    if _n(r.get("sla_uptime_pct")): add(2, "SLA uptime", f"{_f(r['sla_uptime_pct'])}%" + (" (có số đo)" if r.get("uptime_do_thuc_te") else " (cam kết)"))
    add(2, "Benchmark / pentest", ("có benchmark" if r.get("benchmark") else "không benchmark") + " · " + ("có pentest/đánh giá ATTT" if r.get("pentest_danh_gia_attt") else "không pentest"))
    sh = {"da_cap": "đã cấp", "da_nop": "đã nộp đơn", "khong": "không có", "sang_che": "sáng chế"}
    add(3, "SHTT (theo trích)", sh.get(r.get("shtt"), "—") + (f" · {_f(r['so_van_bang'])} văn bằng" if _n(r.get("so_van_bang")) else ""))
    if stt in SHTT_FIX: add(3, "Lưu ý review", SHTT_FIX[stt][1])
    add(3, "Phần lõi", {"co_thuyet_minh": "có thuyết minh", "mot_phan": "tự làm một phần", "white_label": "white-label", "khong_ro": "không rõ"}.get(r.get("loi_tu_phat_trien"), "—"))
    if _n(r.get("doi_ngu")): add(3, "Đội ngũ", f"{_f(r['doi_ngu'])} người" + (f" · {_f(r['doi_ngu_vn_pct'])}% người Việt" if _n(r.get("doi_ngu_vn_pct")) else ""))
    add(4, "Tích hợp / API", f"{_f(_n(r.get('so_tich_hop')))} tích hợp · " + ("API công khai" if r.get("api_cong_khai") else "không thấy API công khai"))
    if r.get("trien_khai"): add(4, "Triển khai", ", ".join(map(str, r["trien_khai"])))
    hl = [x for x in [("NPS " + _f(r["nps"])) if _n(r.get("nps")) is not None else "", ("CSAT " + _f(r["csat_pct"]) + "%") if _n(r.get("csat_pct")) else "", (_f(r["rating_sao"]) + "★") if _n(r.get("rating_sao")) else ""] if x]
    add(4, "Hài lòng", " · ".join(hl) or "không có số đo")
    add(5, "Lượng hóa bài toán", {"co_nguon": "có số kèm nguồn", "khong_nguon": "có số không nguồn", "dinh_tinh": "định tính"}.get(r.get("bai_toan_luong_hoa"), "—") + " · " + ("có dẫn chiếu chính sách" if r.get("dan_chieu_chinh_sach") else "không dẫn chiếu chính sách"))
    add(5, "Xác nhận nhu cầu", _f(_n(r.get("xac_nhan_nhu_cau"))))
    lk = {"B2B": "doanh nghiệp", "B2C": "cá nhân", "B2G": "nhà nước", "hon_hop": "hỗn hợp"}
    add(6, "Loại khách", lk.get(r.get("loai_khach"), "—"))
    add(6, "Khách trả phí / tổ chức dùng / người dùng", f"{_f(_n(r.get('khach_hang_tra_phi')))} / {_f(_n(r.get('to_chuc_su_dung')))} / {_f(_n(r.get('nguoi_dung')))} ({BC_TXT.get(r.get('nguoi_dung_bang_chung'), '—')})")
    if _n(r.get("tang_truong_pct")) is not None: add(6, "Tăng trưởng", f"{_f(r['tang_truong_pct'], 1)}%")
    add(6, "TAM/SAM/SOM", {"co_nguon": "có nguồn", "khong_nguon": "không nguồn", "khong": "không có"}.get(r.get("tam_sam_som"), "—"))
    dtv = _n(r.get("doanh_thu_ty"))
    add(7, "Doanh thu SP", (f"{_f(dtv, 3)} tỷ" if dtv is not None else "—") + (f" ({r['doanh_thu_nam']})" if r.get("doanh_thu_nam") else "") + f" · {BC_TXT.get(r.get('doanh_thu_bang_chung'), '—')}")
    if _n(r.get("doanh_thu_cong_ty_ty")): add(7, "Doanh thu công ty", f"{_f(r['doanh_thu_cong_ty_ty'], 2)} tỷ (chỉ dùng theo quy tắc số của công ty)")
    if _n(r.get("gia_re_hon_ngoai_pct")): add(7, "Giá rẻ hơn SP ngoại", f"{_f(r['gia_re_hon_ngoai_pct'])}% (cần báo giá đối chiếu)")
    add(8, "Mức quốc tế (theo trích)", f"{_f(_n(r.get('quoc_te_muc')) or 0)}" + (f" · {', '.join(map(str, r['quoc_te_nuoc']))}" if r.get("quoc_te_nuoc") else ""))
    vl = {"quy": "quỹ", "thien_than": "thiên thần", "uom_tao_tai_tro": "ươm tạo/tài trợ", "tap_doan": "tập đoàn (không tính)", "tu_than": "tự thân", "dang_dam_phan": "đang đàm phán", "khong_ro": "không rõ"}
    add(9, "Nguồn vốn", vl.get(r.get("von_loai"), "—") + (f" · {_f(r['von_ty'], 2)} tỷ" if _n(r.get("von_ty")) else "") + (f" · {', '.join(map(str, r['nha_dau_tu']))}" if r.get("nha_dau_tu") else ""))
    add(9, "Kế hoạch gọi vốn có số tiền", "có" if stt in KE_HOACH_VON else "không thấy")
    for t, txt in EXTRA.get(stt, {}).items(): add(t, "Lưu ý review", txt)
    return {str(t): v for t, v in f.items() if v}


# ===================== BO NGUONG V4 (18/11/2026) =====================
# Giu cach xep bac bang chung cua v3 (bac = muc bang chung), doi bang quy doi bac -> diem theo thang hieu chuan
# cua cuoc thi (tuyen bo chung ~50-60%, mo ta cu the ~75-85%, kiem chung 100%), ha nguong cac thanh phan
# gan nhu ai cung 0, bo tran "tu khai" o bac cao nhat. Phan chuyen mon [CM] giu thang tuyen tinh.
import copy as _copy

MAX_TC = {1: 20, 2: 20, 3: 10, 4: 10, 5: 10, 6: 15, 7: 5, 8: 5, 9: 5}
PTS = {1: [0, 1], 2: [0, 1.5, 2], 3: [0, 1.5, 2.5, 3], 4: [0, 2, 3, 3.5, 4], 5: [0, 2, 3, 4, 4.5, 5],
       6: [0, 2.5, 3.5, 4, 5, 5.5, 6], 8: [0, 3, 4, 5, 5.5, 6.5, 7, 7.5, 8], 9: [0, 3, 4, 5, 6, 6.5, 7.5, 8, 8.5, 9]}


def level_points(part, lv):
    """Diem cua mot bac (bac la so nguyen 0..m)."""
    lv = max(0, min(int(lv), part["m"]))
    return part["p"][lv] if part.get("p") else lv


V4 = _copy.deepcopy(V3)
for _tt, _c in V4.items():
    for _p in _c["parts"]:
        _p["p"] = PTS[_p["m"]]   # moi thanh phan (ke ca chuyen mon) quy doi theo cung mot bang
        for _b in _p["b"]:
            _b[2] = _b[2].replace(" (cần chứng từ)", "")

def _part(tt, k):
    return next(p for p in V4[tt]["parts"] if p["k"] == k)

# TC4-A: co nguoi dung that (tu khai) da duoc bac 1
_part(4, "A")["b"][2] = [1, 1, "Case study tự viết có tên khách, hoặc có người dùng/khách thật (tự khai có tên, số)"]
# TC4-D: dung thu theo giao thuc, quy doi nhu thang bang chung
_part(4, "D")["p"] = PTS[3]
# TC5: gop "Chinh sach" vao A (0-6)
V4[5]["parts"] = [p for p in V4[5]["parts"] if p["k"] != "C"]
_a5 = _part(5, "A")
_a5.update({"l": "Mức cấp thiết & gắn chính sách", "m": 6, "b": [
    [6, 6, "Lớn, cấp bách, ảnh hưởng diện rộng, gắn chỉ tiêu/điều khoản chính sách cụ thể"],
    [5, 5, "Lớn, cấp bách, ảnh hưởng diện rộng"], [4, 4, "Rõ ràng, có ý nghĩa với một ngành/nhóm lớn"],
    [3, 3, "Có ích cho một phân khúc"], [1, 2, "Mơ hồ / nhu cầu \"có thì tốt\""], [0, 0, "Không thuyết minh"]],
    "n": "Nêu được điều, khoản hoặc chỉ tiêu chính sách mà sản phẩm đáp ứng thì cộng 1 bậc (tối đa 6)."})
_a5["p"] = PTS[6]
_part(5, "D")["b"][1] = [1, 1, "1–2 bằng chứng, hoặc có tổ chức thí điểm/dùng thử có tên (chưa cần biên bản)"]
# TC6-B, TC6-C: ha nguong
_part(6, "B")["b"] = [[2, 2, "Tăng ≥20% (doanh thu hoặc khách hàng, năm 2025 so với 2024)"],
                      [1, 1, "Có tăng trưởng dương, có số liệu"], [0, 0, "Giảm, không có số, chưa đủ 2 năm"]]
_part(6, "C")["b"] = [[2, 2, "Có số quy mô thị trường (TAM/SAM/SOM) kèm nguồn"], [1, 1, "Có số quy mô thị trường nhưng chưa ghi nguồn"],
                      [0, 0, "Không có số"]]
# TC9-B: suc hap dan dau tu -> chuyen mon
_b9 = _part(9, "B")
_b9.update({"l": "Sức hấp dẫn đầu tư", "t": "CM", "b": [
    [2, 2, "Có lực kéo thị trường thật và kế hoạch/tín hiệu gọi vốn (kế hoạch có số tiền, LOI, GCN KH&CN/khởi nghiệp sáng tạo, có lãi)"],
    [1, 1, "Có lực kéo hoặc tiềm năng sản phẩm rõ, chưa có kế hoạch gọi vốn"], [0, 0, "Chưa rõ"]],
    "n": "Đánh giá khả năng thu hút nhà đầu tư; vốn đã nhận chấm ở A."})
_b9["p"] = PTS[2]

RULES_V4 = [
    "Mỗi thành phần xếp theo BẬC bằng chứng (như v3), rồi quy đổi ra điểm theo bảng: thang 3 bậc → 1,5 / 2,5 / 3; thang 2 bậc → 1,5 / 2; thang 4 → 2 / 3 / 3,5 / 4; thang 5 → 2 / 3 / 4 / 4,5 / 5; thang 6 → 2,5 / 3,5 / 4 / 5 / 5,5 / 6; thang 9 (TC1-A) → 3 / 4 / 5 / 6 / 6,5 / 7,5 / 8 / 8,5 / 9. Áp cho mọi thành phần, kể cả chuyên môn. Điểm tiêu chí làm tròn tới số nguyên.",
    "Kỳ số liệu: doanh thu năm 2025 (dưới 0,1 tỷ hoặc ra mắt sau 2025 thì lấy số lớn hơn giữa 2025 và 2026 tới ngày nộp); khách hàng, người dùng là số đang dùng tại ngày nộp; không dùng kế hoạch, trừ TC8 bậc 1–3 và TC9-B.",
    "Số tự khai cụ thể, nhất quán được tính đủ bậc. Ban tổ chức xin chứng từ cho các hồ sơ dẫn đầu trước khi chốt; không bổ sung được thì hạ 1 bậc ở thành phần đó.",
    "Số liệu mâu thuẫn (cùng chỉ tiêu, cùng kỳ): số có chứng từ thắng số tự khai; còn lại lấy số nhỏ hơn, chênh hơn 2 lần mà không có chứng từ thì hạ thêm 1 bậc.",
    "Số của công ty chỉ dùng khi sản phẩm là nguồn thu chính (≥70%) và đã bán ≥12 tháng; còn lại coi số của sản phẩm bằng 0.",
    "Khách hàng, doanh thu, đối tác, vốn từ công ty cùng tập đoàn không tính ở TC5-D, TC6-A, TC7, TC8, TC9-A.",
    "Một khẳng định chỉ cho điểm ở một chỗ: văn bằng → TC3; thư đánh giá, gia hạn → TC4-A; LOI, thí điểm → TC5-D; hợp đồng trả phí → TC6-A; tăng trưởng → TC6-B; giải thưởng → TC1-D; vốn đã nhận → TC9-A.",
    "Chấm phần chuyên môn [CM] trước khi xem điểm AI; nghi vấn tư cách dự thi không làm đổi điểm (đánh dấu cho Ban tổ chức).",
]
