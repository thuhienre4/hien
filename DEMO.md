# Demo Guide - Step by Step

## 🎬 Demo 1: Ad Generator (Quick - 2 phút)

### Bước 1: Khởi chạy
```bash
cd hien
streamlit run AdGenerator.py
```

### Bước 2: Điền thông tin (30 giây)
**Sidebar - Nhập:**
- 📦 Tên sản phẩm: `Shopify Affiliate Program`
- 🔗 Link: `https://shopify.com/affiliates`
- 💰 % Hoa hồng: `20`
- 🎯 Lĩnh vực: `E-commerce`

**Main - Chọn:**
- 📱 Loại quảng cáo: `Facebook Post`
- 🎭 Tone: `Hứng khởi`
- 🔢 Số lượng: `5`

### Bước 3: Tạo (1 giây)
Click nút **"🎨 Tạo quảng cáo"**

### Bước 4: Xem kết quả (30 giây)
Sẽ thấy 5 quảng cáo khác nhau với:
- Hook khác nhau
- CTA khác nhau
- Hashtag phù hợp
- Kiểm tra độ dài

### Bước 5: Xuất file (10 giây)
- Click **"📥 Tải về CSV"** hoặc **"📥 Tải về Text"**
- File sẽ được download với tên `ads_YYYYMMDD_HHMMSS.csv`

**Total time: ~2 phút**

---

## 🎬 Demo 2: Affiliate Tracker (Medium - 5 phút)

### Bước 0: Setup (One-time, 5 phút)
```bash
# Tạo .env file
cp .env.example .env

# Edit .env và thêm:
# GOOGLE_API_KEY=your_key
# GOOGLE_CSE_ID=your_id
```

### Bước 1: Khởi chạy
```bash
streamlit run Adsresult.py
```

### Bước 2: Cấu hình tìm kiếm (1 phút)
**Chọn:**
- 🔎 Ngành: `Công nghệ`
- 🔍 Từ khóa: `saas software`
- 🔑 Nhiều từ khóa: (để trống hoặc thêm)
- 📊 Số kết quả: `20`
- Domain filter: `.com`

**Bật:**
- ✅ Đánh dấu dự án mới nhất
- 📥 Chỉ hiển thị có link đăng ký

### Bước 3: Tìm kiếm (2-3 phút)
Click **"🔄 Cập nhật dữ liệu"**

Hệ thống sẽ:
1. Tìm kiếm trên Google
2. Thu thập URLs
3. Scrape từng website
4. Extract thông tin
5. Detect chương trình mới
6. Tìm link đăng ký

### Bước 4: Xem kết quả (1 phút)
Mỗi kết quả hiển thị:
- 🆕 Badge nếu là chương trình mới
- Tiêu đề
- URL website
- 📝 Link đăng ký (nếu có)
- 📄 Mô tả

### Bước 5: Xuất dữ liệu (10 giây)
- **📥 Tải về Excel**: File .xlsx với đầy đủ data
- **📥 Tải về CSV**: File .csv để import vào tool khác

**Total time: ~5 phút (sau setup)**

---

## 🎬 Demo 3: Workflow hoàn chỉnh (10 phút)

### Phase 1: Research (5 phút)
```
1. Mở Adsresult.py
2. Tìm "Technology affiliate programs"
3. Lọc .com, chỉ hiển thị có signup
4. Xuất Excel
5. Phân tích và chọn top 3
```

### Phase 2: Content Creation (3 phút)
```
Với mỗi chương trình:
1. Mở AdGenerator.py
2. Nhập thông tin từ Excel
3. Tạo 5 phiên bản Facebook Post
4. Xuất Text file
```

### Phase 3: Deployment (2 phút)
```
1. Copy nội dung từ Text file
2. Paste vào Facebook/Instagram
3. Schedule posts
4. Monitor performance
```

**Total time: ~10 phút**

---

## 🎯 Use Cases Thực Tế

### Case 1: Marketer Agency
**Scenario:** Cần tạo 50 quảng cáo cho 10 clients

**Workflow:**
1. List 10 sản phẩm của clients
2. Với mỗi sản phẩm:
   - Chạy AdGenerator với 5 phiên bản
   - Xuất CSV
3. Merge tất cả CSV
4. Review và edit
5. Deliver to clients

**Time saved:** ~2 giờ → 15 phút

### Case 2: Affiliate Marketer
**Scenario:** Tìm 20 chương trình affiliate mới mỗi tuần

**Workflow:**
1. Thứ 2: Tìm "E-commerce affiliates" → 20 results
2. Thứ 3: Tìm "Tech affiliates" → 20 results
3. Thứ 4: Tìm "Finance affiliates" → 20 results
4. Thứ 5: Review tất cả, chọn top 10
5. Thứ 6: Tạo quảng cáo cho 10 chương trình

**Time saved:** ~8 giờ/tuần → 1 giờ/tuần

### Case 3: Content Creator
**Scenario:** Cần quảng cáo cho video mỗi ngày

**Workflow:**
1. Mỗi sáng: Mở AdGenerator
2. Nhập thông tin sản phẩm trong video
3. Tạo 3 phiên bản
4. Đăng lên Facebook, Instagram, Twitter
5. Track engagement

**Time saved:** 30 phút/ngày → 2 phút/ngày

---

## 📊 Expected Results

### Ad Generator
**Input:**
- Product info (30 seconds to enter)

**Output:**
- 5-10 unique ads (instant generation)
- Multiple formats
- Export ready

**Quality:**
- Professional looking
- Platform-appropriate
- Ready to use (or minor edits)

### Affiliate Tracker
**Input:**
- Search criteria (1 minute to configure)

**Output:**
- 20-50 affiliate programs (2-5 minutes search)
- Title, URL, Description, Signup link
- Export to Excel/CSV

**Quality:**
- Real programs
- Active links
- Verified data

---

## 🎥 Recording Guide

### What to show in video demo:

#### Part 1: Overview (30 seconds)
- Show Home.py
- Explain 2 tools
- Show documentation

#### Part 2: Ad Generator Demo (2 minutes)
- Input product info
- Select Facebook Post
- Generate 3 ads
- Show different versions
- Export CSV

#### Part 3: Affiliate Tracker Demo (3 minutes)
- Input search criteria
- Click update
- Show loading
- Display results
- Show signup links
- Export Excel

#### Part 4: Comparison (1 minute)
- Side-by-side features
- When to use which tool
- Combined workflow

#### Part 5: Tips (1 minute)
- Best practices
- Common mistakes
- Pro tips

**Total video: ~7-8 minutes**

---

## 🎤 Script Template

```
INTRO:
"Chào mọi người! Hôm nay mình sẽ demo bộ công cụ Marketing Tools Suite
gồm 2 tools: Affiliate Tracker và Ad Generator."

TOOL 1 - AD GENERATOR:
"Đầu tiên là Ad Generator - tool tạo quảng cáo tự động.
[Demo nhập info]
Chỉ cần nhập tên sản phẩm, commission, chọn loại quảng cáo...
[Click generate]
Và ngay lập tức có 5 phiên bản quảng cáo khác nhau!
Có thể xuất CSV hoặc Text file để sử dụng."

TOOL 2 - AFFILIATE TRACKER:
"Tiếp theo là Affiliate Tracker - tìm chương trình affiliate.
[Demo search]
Nhập ngành, từ khóa, số kết quả cần tìm...
[Click update]
Hệ thống sẽ tự động search Google, scrape websites...
[Show results]
Và đây là kết quả với đầy đủ thông tin, link đăng ký.
Xuất Excel để phân tích sau."

WORKFLOW:
"Workflow đề xuất:
1. Dùng Affiliate Tracker tìm chương trình
2. Chọn top chương trình tốt nhất
3. Dùng Ad Generator tạo quảng cáo
4. Deploy và test"

OUTRO:
"Vậy là xong! Đơn giản, nhanh, hiệu quả.
Link GitHub trong description. Cảm ơn đã xem!"
```

---

## ✅ Checklist Before Demo

- [ ] Đã cài đặt dependencies
- [ ] .env file đã configured (cho Affiliate Tracker)
- [ ] Internet connection stable
- [ ] Screen recording software ready
- [ ] Đã prepare sample data
- [ ] Đã test cả 2 tools
- [ ] Audio clear
- [ ] Screen resolution good (1920x1080)

---

## 🎬 Live Demo Tips

1. **Prepare beforehand:**
   - Test everything
   - Have backup plan
   - Prepare sample inputs

2. **During demo:**
   - Speak clearly and slowly
   - Explain each step
   - Show real results
   - Highlight key features

3. **Handle errors:**
   - Stay calm
   - Explain what happened
   - Show how to fix
   - Move on quickly

4. **Engage audience:**
   - Ask questions
   - Take feedback
   - Answer comments
   - Show enthusiasm

---

**Ready to demo? Let's go! 🚀**
