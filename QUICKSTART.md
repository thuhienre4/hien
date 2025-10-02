# Hướng dẫn Nhanh - Quick Start Guide

## Cài đặt nhanh trong 4 bước

### 1. Clone dự án
```bash
git clone https://github.com/thuhienre4/hien.git
cd hien
```

### 2. Cài đặt thư viện
```bash
# Tạo môi trường ảo (khuyến nghị)
python -m venv venv

# Kích hoạt môi trường ảo
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt
```

### 3. Cấu hình API Keys
```bash
# Sao chép file mẫu
cp .env.example .env

# Chỉnh sửa file .env và thêm API keys của bạn
# GOOGLE_API_KEY=your_actual_api_key
# GOOGLE_CSE_ID=your_actual_cse_id
```

### 4. Chạy ứng dụng
```bash
streamlit run Adsresult.py
```

Ứng dụng sẽ mở tự động tại: http://localhost:8501

---

## Lấy Google API Keys

### Google API Key:
1. Truy cập: https://console.cloud.google.com/
2. Tạo project mới
3. Bật "Custom Search API"
4. Tạo API Key trong Credentials

### Google CSE ID:
1. Truy cập: https://programmablesearchengine.google.com/
2. Tạo search engine mới
3. Sao chép Search Engine ID

---

## Troubleshooting

**Lỗi ModuleNotFoundError?**
```bash
pip install -r requirements.txt
```

**Lỗi streamlit not found?**
```bash
python -m streamlit run Adsresult.py
```

**Lỗi API Key?**
- Kiểm tra file .env
- Đảm bảo không có khoảng trắng thừa
- Kiểm tra quota Google API

---

Xem thêm chi tiết trong [README.md](README.md)
