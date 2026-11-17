"""Gop du lieu san pham + diem AI vao template HTML -> trang Artifact.
Usage: python -P -E -X utf8 build_web.py <E:\\MIV2026> <scores_dir> <template.html> <out.html>
"""
import json
import sys
from pathlib import Path

root, scores_dir, tpl, out = (Path(a) for a in sys.argv[1:5])
info = json.loads((root / "MIV2026_tong_hop.json").read_text(encoding="utf-8"))

CRIT = [
    (1, "Tính sáng tạo và độc đáo của sản phẩm", "Sáng tạo, độc đáo", 20, "I",
     ["Tính khác biệt với những sản phẩm quốc tế và trong nước hiện nay (khác biệt về phân khúc thị trường hoặc về công nghệ hoặc kết hợp nhiều kỹ thuật).", "Định hình/phù hợp xu hướng."]),
    (2, "Công nghệ, chất lượng sản phẩm", "Công nghệ, chất lượng", 20, "I",
     ["Áp dụng các công nghệ số chiến lược, đổi mới công nghệ, công nghệ mở, mã nguồn mở, nền tảng phát triển mở.", "Độ tin cậy của sản phẩm.", "Sự tiện lợi của sản phẩm đối với người dùng.", "Hiệu năng của sản phẩm.", "Khả năng bảo trì, bảo hành của sản phẩm.", "Tính an toàn, bảo mật."]),
    (3, "Công đoạn cốt lõi của sản phẩm do người Việt Nam thực hiện", "Cốt lõi do người VN", 10, "I",
     ["Có chứng nhận sở hữu trí tuệ (trong nước hoặc nước ngoài) hoặc hợp đồng khoa học công nghệ hoặc thuyết minh chi tiết sản phẩm được đăng ký/công bố tại Việt Nam."]),
    (4, "Tính năng sản phẩm (dễ sử dụng, tương thích, tùy biến, mở rộng,...)", "Tính năng", 10, "I",
     ["Khả năng đáp ứng yêu cầu người dùng, mức độ thân thiện, sự hài lòng của người dùng.", "Khả năng mở rộng.", "Khả năng tùy biến."]),
    (5, "Tính cấp thiết của bài toán mà sản phẩm đang giải quyết tại Việt Nam", "Tính cấp thiết", 10, "II",
     ["Thuyết minh bài toán mà sản phẩm giải quyết.", "Vấn đề đang giải quyết có ý nghĩa như thế nào đối với người dùng."]),
    (6, "Mô hình, chiến lược và quy mô thị trường", "Mô hình, thị trường", 15, "II",
     ["Thị phần và tiềm năng thị trường trong nước.", "Mô hình, chiến lược kinh doanh."]),
    (7, "Tác động kinh tế xã hội", "Tác động KT-XH", 5, "II",
     ["Doanh thu sản phẩm.", "Số lượng người/Doanh nghiệp/tổ chức sử dụng.", "Tác động kinh tế, xã hội.", "Giá cạnh tranh."]),
    (8, "Khả năng mở rộng ra thị trường quốc tế", "Mở rộng quốc tế", 5, "II",
     ["Mô hình, chiến lược kinh doanh ra thị trường nước ngoài."]),
    (9, "Khả năng kêu gọi được vốn", "Kêu gọi vốn", 5, "II",
     ["Kết quả kêu gọi vốn đầu tư cho sản phẩm.", "Khả năng kêu gọi vốn đầu tư, sức hấp dẫn của sản phẩm đối với thị trường và nhà đầu tư."]),
]

# Thang tham chieu AI dung khi cham (scoring_guide), hien cho giam khao de doi chieu. [tu, den, mo ta]
ANCHORS = {
    1: [[17, 20, "Mới thật sự ở VN, khác biệt rõ với giải pháp quốc tế, có so sánh đối thủ"], [13, 16, "Khác biệt rõ trong phân khúc tại VN, đúng xu hướng"], [9, 12, "Tương tự nhiều sản phẩm đã có, khác biệt nhỏ"], [0, 8, "Sao chép / phổ thông"]],
    2: [[17, 20, "Công nghệ lõi tự phát triển, có bằng chứng chất lượng (ISO, chứng nhận ATTT, kiểm thử, benchmark, kiến trúc chi tiết)"], [13, 16, "Công nghệ tốt, mô tả kỹ thuật cụ thể, có một phần bằng chứng"], [9, 12, "Chỉ mô tả chung, chưa có bằng chứng chất lượng / bảo mật"], [0, 8, "Sơ sài"]],
    3: [[9, 10, "Có văn bằng SHTT / GCN bản quyền phần mềm hoặc hợp đồng KH&CN; đội ngũ VN làm phần lõi"], [7, 8, "Đã nộp đơn SHTT, hoặc thuyết minh kỹ thuật chi tiết chứng tỏ đội VN làm lõi"], [5, 6, "Chỉ tuyên bố, không có chứng nhận"], [0, 4, "Lõi phụ thuộc nước ngoài hoặc không rõ"]],
    4: [[9, 10, "Tính năng phong phú, có bằng chứng hài lòng người dùng, API / tích hợp, mở rộng và tùy biến rõ"], [7, 8, "Tốt nhưng ít bằng chứng hài lòng"], [5, 6, "Cơ bản"], [0, 4, "Hạn chế"]],
    5: [[9, 10, "Bài toán lớn, cấp bách ở VN, được lượng hóa (số liệu, chính sách)"], [7, 8, "Rõ ràng, có ý nghĩa"], [5, 6, "Có ích nhưng không cấp thiết"], [0, 4, "Mơ hồ"]],
    6: [[13, 15, "Đã có lực kéo thị trường rõ, mô hình và chiến lược cụ thể, TAM/SAM/SOM hợp lý"], [10, 12, "Mô hình rõ, có khách hàng ban đầu"], [7, 9, "Có kế hoạch nhưng ít lực kéo"], [0, 6, "Chưa rõ"]],
    7: [[5, 5, "Doanh thu đáng kể, nhiều người dùng / tổ chức, có số liệu"], [4, 4, "Có doanh thu và người dùng ổn"], [3, 3, "Lực kéo ban đầu"], [2, 2, "Mới thí điểm"], [0, 1, "Chưa có"]],
    8: [[5, 5, "Đã có khách hàng / doanh thu nước ngoài"], [4, 4, "Kế hoạch cụ thể, có thí điểm / đối tác nước ngoài"], [3, 3, "Có kế hoạch rõ"], [2, 2, "Chỉ nêu định hướng"], [0, 1, "Không đề cập"]],
    9: [[5, 5, "Đã gọi được vốn đáng kể từ quỹ / tổ chức (có tên, số tiền)"], [4, 4, "Đã nhận vốn thiên thần / seed / ươm tạo, hoặc tập đoàn lớn hậu thuẫn"], [3, 3, "Hấp dẫn, đang đàm phán, có kế hoạch gọi vốn cụ thể"], [2, 2, "Tự thân, có tiềm năng"], [0, 1, "Không có thông tin"]],
}

products = []
for p in info["san_pham"]:
    sc = json.loads((scores_dir / f"{p['stt']:02d}.json").read_text(encoding="utf-8"))
    smap = {s["tt"]: s for s in sc["scores"]}
    fl = p["fields"]
    products.append({
        "stt": p["stt"], "id": p["id"], "name": p["ten_san_pham"], "company": p["doanh_nghiep"],
        "category": p["hang_muc_du_thi"],
        "link": fl.get("Link sản phẩm/giới thiệu sản phẩm (nếu có)", ""),
        "website": fl.get("Địa chỉ website", ""),
        "desc": fl.get("Mô tả ngắn gọn về tính năng sản phẩm", ""),
        "files": [{"field": f["field"], "name": f["file_name"], "url": f["url"],
                   "kb": round(f.get("size_bytes", 0) / 1024)} for f in p["files"]],
        "statUrl": p["statistic_url"],
        "ai": {
            "s": [smap[t]["diem"] for t in range(1, 10)],
            "r": [smap[t]["ly_do"] for t in range(1, 10)],
            "summary": sc.get("nhan_xet_chung", ""),
            "strengths": sc.get("diem_manh", ""),
            "weaknesses": sc.get("diem_yeu", ""),
            "verify": sc.get("can_xac_minh", ""),
            "docs": sc.get("tai_lieu_da_doc", []),
            "limits": sc.get("han_che", ""),
            "conf": (sc.get("do_tin_cay", "") or "").split(" ")[0].replace("Trung", "Trung bình"),
        },
    })

data = {
    "meta": {"scoredAt": "17/11/2026", "category": "Sản phẩm công nghệ số tiềm năng", "n": len(products)},
    "criteria": [{"tt": t, "name": n, "short": s, "max": m, "group": g, "sub": sub, "anchors": ANCHORS[t]} for t, n, s, m, g, sub in CRIT],
    "grades": [[85, "Xuất sắc"], [75, "Tốt"], [65, "Khá"], [50, "Trung bình"], [0, "Yếu"]],
    "products": products,
}
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = tpl.read_text(encoding="utf-8").replace("__MIV_DATA__", payload)
out.write_text(html, encoding="utf-8")
print("written", out, "bytes", len(html.encode("utf-8")), "products", len(products))
