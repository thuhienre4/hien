# 🚀 Marketing Tools Suite

Bộ công cụ marketing tự động cho Affiliate Marketing và tạo Quảng cáo

## 📋 Tổng quan

Repository này bao gồm 2 công cụ chính:

1. **Affiliate Project Tracker** (`Adsresult.py`) - Công cụ tìm kiếm và theo dõi các chương trình affiliate
2. **Ad Generator** (`AdGenerator.py`) - Công cụ tự động tạo nội dung quảng cáo cho nhiều nền tảng

## ✨ Tính năng

### 📊 Affiliate Project Tracker

- 🔍 Tìm kiếm chương trình affiliate theo ngành nghề
- 🌐 Thu thập thông tin tự động từ Google Custom Search
- 📝 Trích xuất mô tả, link đăng ký, và thông tin chi tiết
- 🆕 Tự động đánh dấu các chương trình mới nhất (2024, 2025)
- 🔄 Xử lý song song nhiều URL để tăng tốc độ
- 💾 Xuất dữ liệu ra Excel và CSV
- 🎯 Lọc theo domain, trạng thái mới, có link đăng ký

### 🎨 Ad Generator (Tool tự động tạo quảng cáo)

- 📱 **Hỗ trợ nhiều nền tảng:**
  - Facebook Post
  - Instagram Caption
  - Twitter/X Post
  - Google Ads
  - Email Subject
  - Banner Ad

- 🎯 **Tính năng nổi bật:**
  - Tự động tạo hook thu hút
  - Generate CTA (Call-to-Action) hiệu quả
  - Tạo hashtag phù hợp theo lĩnh vực
  - Kiểm tra độ dài phù hợp từng platform
  - Tạo nhiều phiên bản để A/B testing
  - Xuất CSV và Text file

## 🚀 Cài đặt

### Prerequisites

- Python 3.8+
- pip

### Các bước cài đặt

```bash
# 1. Clone repository
git clone https://github.com/thuhienre4/hien.git
cd hien

# 2. Cài đặt dependencies
pip install -r requirements.txt

# 3. Tạo file .env (chỉ cần cho Affiliate Tracker)
cp .env.example .env
# Hoặc tạo file .env mới
echo "GOOGLE_API_KEY=your_api_key_here" > .env
echo "GOOGLE_CSE_ID=your_search_engine_id_here" >> .env
```

### Lấy API Keys (Cho Affiliate Tracker)

#### Google Custom Search API Key:

1. Truy cập [Google Cloud Console](https://console.cloud.google.com/)
2. Tạo project mới hoặc chọn project có sẵn
3. Enable **Custom Search API**
4. Tạo credentials (API Key)
5. Copy API key vào file `.env`

#### Google Custom Search Engine ID:

1. Truy cập [Programmable Search Engine](https://programmablesearchengine.google.com/)
2. Tạo search engine mới
3. Cấu hình tìm kiếm trên toàn bộ web
4. Copy Search Engine ID vào file `.env`

## 🎯 Sử dụng

### Chạy Affiliate Project Tracker

```bash
streamlit run Adsresult.py
```

Sau đó:
1. Chọn ngành nghề
2. Thêm từ khóa (tùy chọn)
3. Cấu hình các bộ lọc
4. Nhấn "🔄 Cập nhật dữ liệu"
5. Xem kết quả và xuất dữ liệu

### Chạy Ad Generator

```bash
streamlit run AdGenerator.py
```

Sau đó:
1. Nhập thông tin sản phẩm/chương trình
2. Chọn loại quảng cáo (Facebook, Instagram, etc.)
3. Chọn lĩnh vực để tạo hashtag phù hợp
4. Tùy chỉnh nội dung (nếu cần)
5. Nhấn "🎨 Tạo quảng cáo"
6. Xem và xuất các quảng cáo được tạo

### Chạy Trang chủ (Home)

```bash
streamlit run Home.py
```

Trang chủ cung cấp giao diện tổng quan và điều hướng giữa các công cụ.

## 📖 Quy trình làm việc đề xuất

```
1. Affiliate Tracker → Tìm chương trình affiliate
        ↓
2. Lọc & chọn → Chọn các chương trình tốt nhất
        ↓
3. Ad Generator → Tạo quảng cáo cho các chương trình
        ↓
4. A/B Testing → Test và tối ưu quảng cáo
        ↓
5. Deploy → Triển khai quảng cáo
```

## 📁 Cấu trúc thư mục

```
hien/
├── Adsresult.py        # Affiliate Project Tracker
├── AdGenerator.py      # Ad Generator Tool
├── Home.py            # Trang chủ
├── requirements.txt   # Python dependencies
├── .env              # API keys (không commit)
├── .env.example      # Template cho .env
└── README.md         # Documentation
```

## 🛠️ Dependencies

- `streamlit` - Web framework
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `beautifulsoup4` - Web scraping
- `requests` - HTTP library
- `google-api-python-client` - Google API
- `python-dotenv` - Environment variables
- `openpyxl` - Excel export

## 💡 Tips & Tricks

### Affiliate Tracker
- Sử dụng từ khóa cụ thể để tìm chương trình chất lượng cao
- Kết hợp domain filter (.com, .vn) để lọc kết quả
- Tăng số luồng xử lý (concurrency) để tăng tốc độ
- Bật filter "Chỉ hiển thị có link đăng ký" để lọc chương trình có thể tham gia ngay

### Ad Generator
- Tạo nhiều phiên bản (5-10) để có nhiều lựa chọn
- Test các tone giọng điệu khác nhau
- Kiểm tra độ dài trước khi đăng
- Sử dụng hashtag phù hợp với lĩnh vực

## 🔧 Troubleshooting

### Lỗi API Key
- Kiểm tra file `.env` có đúng format
- Đảm bảo API key còn hạn sử dụng
- Kiểm tra quota API của Google

### Lỗi Import Module
```bash
pip install -r requirements.txt --upgrade
```

### Streamlit không chạy
```bash
# Kiểm tra phiên bản Python
python --version  # Cần >= 3.8

# Cài đặt lại Streamlit
pip install --upgrade streamlit
```

## 🤝 Đóng góp

Contributions, issues và feature requests đều được chào đón!

1. Fork repository
2. Tạo branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📝 Roadmap

- [ ] Thêm AI-powered content generation (OpenAI/Claude)
- [ ] Tích hợp với Facebook Ads API
- [ ] Thêm analytics và tracking
- [ ] Hỗ trợ nhiều ngôn ngữ hơn
- [ ] Tạo template quảng cáo tùy chỉnh
- [ ] Export PDF với design đẹp

## 📄 License

MIT License - xem file LICENSE để biết thêm chi tiết

## 👤 Tác giả

**thuhienre4**

- GitHub: [@thuhienre4](https://github.com/thuhienre4)

## 🙏 Credits

- Streamlit - Web framework
- Google Custom Search API - Search functionality
- BeautifulSoup - Web scraping

---

⭐ Nếu thấy hữu ích, hãy star repo này!