# Hướng dẫn sử dụng Marketing Tools Suite

## 1. Cài đặt

```bash
# Clone repository
git clone https://github.com/thuhienre4/hien.git
cd hien

# Cài đặt dependencies
pip install -r requirements.txt
```

## 2. Cấu hình (Chỉ cho Affiliate Tracker)

Tạo file `.env` với nội dung:

```
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CSE_ID=your_cse_id_here
```

Hoặc copy từ template:
```bash
cp .env.example .env
# Sau đó edit file .env và thêm API keys
```

## 3. Chạy các công cụ

### A. Trang chủ (Home)
```bash
streamlit run Home.py
```
Mở trình duyệt tại: http://localhost:8501

### B. Affiliate Project Tracker
```bash
streamlit run Adsresult.py
```

**Các bước sử dụng:**
1. Chọn ngành (Công nghệ, Tài chính, Du lịch, etc.)
2. Thêm từ khóa bổ sung (tùy chọn): "high commission", "recurring", etc.
3. Cấu hình số kết quả muốn tìm (5-50)
4. Thêm domain filter nếu cần: .com, .vn
5. Bật các checkbox:
   - "Đánh dấu dự án mới nhất" - Highlight chương trình 2024/2025
   - "Chỉ hiển thị dự án mới" - Lọc chỉ chương trình mới
   - "Chỉ hiển thị có link đăng ký" - Lọc có link affiliate
6. Nhấn "🔄 Cập nhật dữ liệu"
7. Xem kết quả và xuất Excel/CSV

**Ví dụ tìm kiếm:**
- Ngành: "Công nghệ"
- Từ khóa: "software saas"
- Domain: ".com"
- Kết quả: 20

### C. Ad Generator (Tự động tạo quảng cáo)
```bash
streamlit run AdGenerator.py
```

**Các bước sử dụng:**
1. **Sidebar - Nhập thông tin:**
   - Tên sản phẩm: "Shopify Affiliate Program"
   - Link đăng ký: "https://www.shopify.com/affiliates"
   - % Hoa hồng: "20"
   - Lĩnh vực: "E-commerce"

2. **Chọn loại quảng cáo:**
   - Facebook Post (bài viết dài)
   - Instagram Caption (với emoji)
   - Twitter/X Post (ngắn gọn)
   - Google Ads (headline + description)
   - Email Subject (tiêu đề)
   - Banner Ad (nội dung banner)

3. **Tùy chọn:**
   - Tone: Chuyên nghiệp / Thân thiện / Hứng khởi / Cấp thiết
   - Mô tả tùy chỉnh (tùy chọn)
   - Số lượng: 1-10 quảng cáo

4. **Nhấn "🎨 Tạo quảng cáo"**

5. **Kết quả:**
   - Xem nhiều phiên bản quảng cáo
   - Kiểm tra độ dài
   - Xuất CSV hoặc Text file

## 4. Quy trình làm việc đề xuất

### Bước 1: Tìm chương trình Affiliate
```
1. Mở Adsresult.py
2. Tìm kiếm "E-commerce affiliate" 
3. Lọc domain .com
4. Xuất Excel
5. Chọn top 5 chương trình tốt nhất
```

### Bước 2: Tạo quảng cáo
```
1. Mở AdGenerator.py
2. Với mỗi chương trình:
   - Nhập tên và link
   - Chọn Facebook Post
   - Tạo 5 phiên bản
   - Xuất Text file
```

### Bước 3: A/B Testing
```
1. Đăng 5 phiên bản khác nhau
2. Theo dõi engagement
3. Chọn phiên bản tốt nhất
4. Scale up
```

## 5. Ví dụ cụ thể

### Ví dụ 1: Affiliate Marketing cho SaaS

**Bước 1 - Tìm chương trình:**
```
Ngành: Công nghệ
Từ khóa: "saas software affiliate"
Domain: .com
Số kết quả: 20
```

**Kết quả mẫu:**
- HubSpot Affiliate Program
- Shopify Affiliate Program
- ClickFunnels Affiliate
- ConvertKit Affiliate

**Bước 2 - Tạo quảng cáo cho HubSpot:**
```
Sản phẩm: HubSpot Affiliate Program
Link: https://www.hubspot.com/partners/affiliates
Hoa hồng: 15%
Lĩnh vực: Technology
Loại: Facebook Post
Số lượng: 5
```

**Kết quả mẫu (1 trong 5 phiên bản):**
```
🚀 Kiếm tiền online dễ dàng với HubSpot Affiliate Program!

Tham gia HubSpot Affiliate Program và bắt đầu hành trình kiếm tiền online của bạn!

✨ Lợi ích:
✓ Hoa hồng cao và cạnh tranh
✓ Thanh toán đúng hạn
✓ Dashboard theo dõi chi tiết

👉 Đăng ký ngay hôm nay!

#affiliatemarketing #affiliate #affiliateprogram #passiveincome #makemoneyonline
```

### Ví dụ 2: Travel Affiliate

**Tìm kiếm:**
```
Ngành: Du lịch
Từ khóa: "hotel booking"
Kết quả: Booking.com, Agoda, Airbnb affiliates
```

**Tạo quảng cáo Instagram:**
```
Sản phẩm: Booking.com Partner Program
Lĩnh vực: General
Loại: Instagram Caption
```

## 6. Tips & Tricks

### Affiliate Tracker:
- **Tip 1:** Sử dụng từ khóa như "high commission", "recurring revenue" để tìm chương trình tốt
- **Tip 2:** Domain filter giúp lọc chương trình uy tín (.com thường uy tín hơn)
- **Tip 3:** Tăng concurrency (10-20) để xử lý nhanh hơn
- **Tip 4:** Bật "Chỉ hiển thị có link đăng ký" để tìm chương trình tham gia được ngay

### Ad Generator:
- **Tip 1:** Tạo 5-10 phiên bản để có nhiều lựa chọn
- **Tip 2:** Test nhiều tone khác nhau (Chuyên nghiệp vs Hứng khởi)
- **Tip 3:** Cho Twitter, giữ nội dung ngắn gọn (< 280 ký tự)
- **Tip 4:** Sử dụng emoji phù hợp với từng platform
- **Tip 5:** Kiểm tra độ dài trước khi đăng

### Kết hợp cả 2:
- **Workflow:** Tracker → Excel → Phân tích → Top programs → Generator → A/B Test → Scale
- **Automation:** Có thể tự động hóa bằng cách export CSV từ Tracker và import vào Generator (future feature)

## 7. Troubleshooting

### Lỗi "No module named 'streamlit'"
```bash
pip install streamlit pandas numpy beautifulsoup4 requests
```

### Lỗi "GOOGLE_API_KEY not found"
```bash
# Kiểm tra file .env tồn tại
ls -la .env

# Nếu không có, tạo mới
cp .env.example .env
# Sau đó edit và thêm API keys
```

### Streamlit không mở trình duyệt
```bash
# Mở thủ công
# Sau khi chạy streamlit run, copy URL và mở trong trình duyệt
# Thường là: http://localhost:8501
```

### Lỗi API quota exceeded
```
- Google Custom Search có giới hạn 100 queries/day (free tier)
- Nếu vượt, chờ 24h hoặc upgrade plan
```

## 8. Nâng cao

### Tích hợp với API khác:
```python
# Có thể mở rộng AdGenerator.py để tích hợp:
# - OpenAI GPT cho content generation thông minh hơn
# - Facebook Ads API để đăng tự động
# - Analytics API để track performance
```

### Tùy chỉnh templates:
```python
# Edit AdGenerator.py
# Tìm biến AD_TEMPLATES và thêm template mới
AD_TEMPLATES = {
    "Your Custom Format": {
        "template": "Your template here...",
        "max_length": 1000
    }
}
```

## 9. Support

Nếu gặp vấn đề:
1. Kiểm tra lại hướng dẫn
2. Xem issues trên GitHub
3. Tạo issue mới với mô tả chi tiết lỗi

---

**Happy Marketing! 🚀**
