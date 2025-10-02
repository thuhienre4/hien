import streamlit as st

st.set_page_config(
    page_title="Marketing Tools Suite",
    page_icon="🚀",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: #f22c74;'>🚀 Marketing Tools Suite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Bộ công cụ marketing tự động cho Affiliate & Quảng cáo</p>", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 Affiliate Project Tracker
    
    Công cụ tìm kiếm và theo dõi các chương trình affiliate:
    
    - 🔍 Tìm kiếm chương trình affiliate theo ngành
    - 📝 Thu thập thông tin tự động
    - 💾 Xuất dữ liệu Excel/CSV
    - 🆕 Đánh dấu dự án mới
    - 📥 Tìm link đăng ký affiliate
    
    """)
    if st.button("➡️ Mở Affiliate Tracker", use_container_width=True):
        st.markdown("**Chạy lệnh:** `streamlit run Adsresult.py`")

with col2:
    st.markdown("""
    ### 🎨 Công cụ tạo quảng cáo
    
    Tự động tạo nội dung quảng cáo cho nhiều nền tảng:
    
    - 📱 Facebook, Instagram, Twitter/X
    - 📧 Email, Google Ads, Banner
    - 🎯 Tùy chỉnh theo lĩnh vực
    - 🔄 Tạo nhiều phiên bản
    - 💾 Xuất CSV/Text
    
    """)
    if st.button("➡️ Mở Ad Generator", use_container_width=True):
        st.markdown("**Chạy lệnh:** `streamlit run AdGenerator.py`")

st.markdown("---")

st.markdown("""
## 🎯 Quy trình làm việc đề xuất

1. **Bước 1**: Sử dụng **Affiliate Project Tracker** để tìm các chương trình affiliate phù hợp
2. **Bước 2**: Xuất dữ liệu và chọn các chương trình tốt nhất
3. **Bước 3**: Sử dụng **Ad Generator** để tạo quảng cáo cho các chương trình đã chọn
4. **Bước 4**: Test các phiên bản quảng cáo khác nhau và tối ưu hóa

## 📖 Hướng dẫn cài đặt

```bash
# Clone repository
git clone https://github.com/thuhienre4/hien.git
cd hien

# Cài đặt dependencies
pip install -r requirements.txt

# Tạo file .env và thêm API keys
echo "GOOGLE_API_KEY=your_api_key" > .env
echo "GOOGLE_CSE_ID=your_cse_id" >> .env

# Chạy ứng dụng
streamlit run Home.py          # Trang chủ
streamlit run Adsresult.py     # Affiliate Tracker
streamlit run AdGenerator.py   # Ad Generator
```

## 🔑 Cấu hình API

Để sử dụng Affiliate Tracker, bạn cần:

1. **Google Custom Search API Key**
   - Truy cập: https://console.cloud.google.com/
   - Tạo project và enable Custom Search API
   - Tạo API key

2. **Google Custom Search Engine ID**
   - Truy cập: https://programmablesearchengine.google.com/
   - Tạo search engine mới
   - Lấy Search Engine ID

3. Thêm vào file `.env`:
   ```
   GOOGLE_API_KEY=your_api_key_here
   GOOGLE_CSE_ID=your_search_engine_id_here
   ```

## 🚀 Tính năng nổi bật

### Affiliate Project Tracker
- Tìm kiếm thông minh với Google Custom Search
- Xử lý song song nhiều URL
- Lọc và sắp xếp kết quả
- Phát hiện chương trình mới
- Xuất dữ liệu Excel/CSV

### Ad Generator
- Template cho 6+ loại quảng cáo
- Tự động tạo hook, CTA, hashtag
- Kiểm tra độ dài phù hợp
- Hỗ trợ nhiều lĩnh vực
- A/B testing với nhiều phiên bản

## 💡 Tips sử dụng

- **Affiliate Tracker**: Sử dụng từ khóa cụ thể và domain filter để tìm chương trình chất lượng
- **Ad Generator**: Tạo nhiều phiên bản để test và chọn phiên bản tốt nhất
- **Kết hợp**: Sử dụng dữ liệu từ Tracker làm input cho Generator

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request.

## 📄 License

MIT License
""")
