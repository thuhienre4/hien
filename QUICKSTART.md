# Quick Start Guide

## 🚀 Bắt đầu nhanh trong 5 phút

### Bước 1: Cài đặt (2 phút)
```bash
git clone https://github.com/thuhienre4/hien.git
cd hien
pip install -r requirements.txt
```

### Bước 2: Chạy Ad Generator ngay (không cần API key!)
```bash
streamlit run AdGenerator.py
```

Công cụ tự động tạo quảng cáo **KHÔNG CẦN** API key và có thể sử dụng ngay!

### Bước 3: Tạo quảng cáo đầu tiên (1 phút)

1. Điền thông tin:
   - **Tên sản phẩm:** "Shopify Affiliate"
   - **Link:** "https://shopify.com/affiliates"
   - **% Hoa hồng:** "20"
   - **Lĩnh vực:** "E-commerce"

2. Chọn loại quảng cáo: **"Facebook Post"**

3. Nhấn **"🎨 Tạo quảng cáo"**

4. Bùm! Bạn có ngay 3 phiên bản quảng cáo khác nhau! 🎉

### Bước 4 (Tùy chọn): Affiliate Tracker

Nếu muốn dùng Affiliate Tracker để tìm chương trình:

1. Tạo file `.env`:
   ```bash
   cp .env.example .env
   ```

2. Thêm Google API keys vào file `.env` (xem README.md để biết cách lấy)

3. Chạy:
   ```bash
   streamlit run Adsresult.py
   ```

## 📊 So sánh công cụ

| Công cụ | Cần API Key? | Mục đích | Thời gian setup |
|---------|-------------|----------|-----------------|
| **Ad Generator** | ❌ Không | Tạo quảng cáo tự động | 2 phút |
| **Affiliate Tracker** | ✅ Cần | Tìm chương trình affiliate | 10 phút |

## 💡 Tip: Bắt đầu với Ad Generator

Nếu bạn mới bắt đầu, hãy sử dụng **Ad Generator** trước! Nó không cần API key và bạn có thể tạo quảng cáo ngay lập tức.

## 🎯 Use Cases phổ biến

### 1. Marketer cần tạo quảng cáo nhanh
```bash
streamlit run AdGenerator.py
# Input: Tên sản phẩm, link, %
# Output: 3-10 phiên bản quảng cáo khác nhau
# Thời gian: < 1 phút
```

### 2. Affiliate Marketer tìm chương trình
```bash
streamlit run Adsresult.py
# Input: Ngành, từ khóa
# Output: Danh sách chương trình affiliate + link đăng ký
# Thời gian: 2-5 phút
```

### 3. Kết hợp cả 2 (Recommended!)
```
Adsresult.py → Tìm 10 chương trình tốt
     ↓
Chọn top 3 chương trình
     ↓
AdGenerator.py → Tạo quảng cáo cho 3 chương trình
     ↓
Deploy & Test
```

## ✨ Tính năng nổi bật

### Ad Generator (Không cần API)
- ✅ Sẵn sàng dùng ngay
- ✅ Hỗ trợ 6+ nền tảng
- ✅ Tạo nhiều phiên bản
- ✅ Xuất CSV/Text

### Affiliate Tracker (Cần API)
- 🔍 Tìm kiếm thông minh
- 📊 Thu thập tự động
- 💾 Xuất Excel/CSV
- 🆕 Detect chương trình mới

## 🆘 Cần trợ giúp?

- Xem **USAGE.md** cho hướng dẫn chi tiết
- Xem **README.md** cho cài đặt và cấu hình
- Tạo issue trên GitHub nếu gặp lỗi

---

**Bắt đầu ngay:** `streamlit run AdGenerator.py` 🚀
