# 🚀 Affiliate Project Tracker

Ứng dụng web theo dõi và tìm kiếm các chương trình affiliate marketing sử dụng Streamlit và Google Custom Search API.

## 📋 Yêu cầu hệ thống

- Python 3.8 trở lên
- Git
- Tài khoản Google API (để sử dụng Custom Search API)

## 🔧 Cài đặt và Build Dự án

### Bước 1: Clone dự án từ GitHub về máy

```bash
git clone https://github.com/thuhienre4/hien.git
cd hien
```

### Bước 2: Tạo môi trường ảo Python (khuyến nghị)

**Trên Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Trên macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài đặt các thư viện phụ thuộc

```bash
pip install -r requirements.txt
```

### Bước 4: Cấu hình biến môi trường

Tạo file `.env` trong thư mục gốc của dự án với nội dung sau:

```env
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CSE_ID=your_google_cse_id_here
```

**Hướng dẫn lấy API Keys:**

1. **Google API Key:**
   - Truy cập [Google Cloud Console](https://console.cloud.google.com/)
   - Tạo project mới hoặc chọn project hiện có
   - Bật API "Custom Search API"
   - Tạo credentials (API Key)
   - Sao chép API Key vào file `.env`

2. **Google CSE ID (Custom Search Engine ID):**
   - Truy cập [Google Programmable Search Engine](https://programmablesearchengine.google.com/)
   - Tạo search engine mới
   - Sao chép Search Engine ID vào file `.env`

## 🚀 Chạy ứng dụng

Sau khi cài đặt xong, chạy lệnh sau để khởi động ứng dụng:

```bash
streamlit run Adsresult.py
```

Ứng dụng sẽ tự động mở trên trình duyệt tại địa chỉ: `http://localhost:8501`

## 📦 Các thư viện sử dụng

- **streamlit**: Framework xây dựng web app
- **pandas**: Xử lý và phân tích dữ liệu
- **beautifulsoup4**: Parse và trích xuất dữ liệu HTML
- **requests**: Gửi HTTP requests
- **google-api-python-client**: Tích hợp Google APIs
- **python-dotenv**: Quản lý biến môi trường
- **openpyxl**: Xuất file Excel

## 💡 Cách sử dụng

1. Chọn ngành nghề bạn muốn tìm kiếm
2. Nhập từ khóa bổ sung (tùy chọn)
3. Cấu hình các bộ lọc:
   - Số kết quả Google
   - Domain filter
   - Đánh dấu dự án mới
   - Chỉ hiển thị dự án mới
   - Chỉ hiển thị có link đăng ký affiliate
4. Nhấn nút "🔄 Cập nhật dữ liệu"
5. Xem kết quả và tải về file Excel/CSV nếu cần

## 🐛 Xử lý lỗi thường gặp

### Lỗi: `ModuleNotFoundError`
- Đảm bảo bạn đã kích hoạt môi trường ảo
- Chạy lại: `pip install -r requirements.txt`

### Lỗi: API Key không hợp lệ
- Kiểm tra lại file `.env`
- Đảm bảo API Key và CSE ID chính xác
- Kiểm tra quota của Google API

### Lỗi: `streamlit: command not found`
- Đảm bảo streamlit đã được cài đặt: `pip install streamlit`
- Hoặc chạy: `python -m streamlit run Adsresult.py`

## 📝 Lưu ý

- File `.env` chứa thông tin nhạy cảm, không nên commit lên GitHub
- Đảm bảo kết nối internet khi chạy ứng dụng
- Google Custom Search API có giới hạn số lượng request miễn phí

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng tạo issue hoặc pull request.

## 📄 License

Dự án này được phát hành dưới giấy phép MIT.