import streamlit as st
import pandas as pd
from datetime import datetime
import random

st.set_page_config(page_title="Tự động tạo quảng cáo", layout="wide")
st.markdown("<h1 style='text-align: center; color: #f22c74;'>🎨 Công cụ tự động tạo quảng cáo</h1>", unsafe_allow_html=True)

# Ad Templates
AD_TEMPLATES = {
    "Facebook Post": {
        "template": """🚀 {hook}

{description}

✨ Lợi ích:
{benefits}

👉 {cta}

{hashtags}""",
        "max_length": 2000
    },
    "Instagram Caption": {
        "template": """{hook} 💫

{description}

{benefits}

{cta} 🔥

{hashtags}""",
        "max_length": 2200
    },
    "Twitter/X Post": {
        "template": """{hook}

{description}

{cta}

{hashtags}""",
        "max_length": 280
    },
    "Google Ads": {
        "template": """Headline: {headline}

Description: {description}

URL: {url}""",
        "max_length": 300
    },
    "Email Subject": {
        "template": """{hook} - {benefit}""",
        "max_length": 60
    },
    "Banner Ad": {
        "template": """[HEADLINE]
{headline}

[SUBHEADLINE]
{description}

[CTA]
{cta}""",
        "max_length": 150
    }
}

# Hook templates
HOOKS = [
    "Kiếm tiền online dễ dàng với {product}!",
    "Khám phá cơ hội affiliate tuyệt vời!",
    "Bạn muốn tăng thu nhập thụ động?",
    "Chương trình affiliate hấp dẫn đang chờ bạn!",
    "💰 Cơ hội kiếm hoa hồng cao đến {commission}%!",
    "Tham gia ngay để nhận hoa hồng hấp dẫn!",
    "Đừng bỏ lỡ chương trình affiliate này!",
    "Thu nhập không giới hạn với {product}!",
]

# CTA templates
CTAS = [
    "Đăng ký ngay hôm nay!",
    "Tham gia ngay để không bỏ lỡ!",
    "Nhấn vào link để tìm hiểu thêm!",
    "Bắt đầu kiếm tiền ngay!",
    "Link đăng ký trong bio!",
    "Click để biết thêm chi tiết!",
    "Đừng chần chừ, đăng ký ngay!",
]

# Benefit templates
BENEFITS = [
    "✓ Hoa hồng cao và cạnh tranh",
    "✓ Thanh toán đúng hạn",
    "✓ Hỗ trợ marketing miễn phí",
    "✓ Dashboard theo dõi chi tiết",
    "✓ Không giới hạn thu nhập",
    "✓ Công cụ marketing chuyên nghiệp",
    "✓ Đào tạo miễn phí",
    "✓ Cộng đồng affiliate sôi động",
]

# Hashtag templates
HASHTAG_GROUPS = {
    "Affiliate Marketing": ["#affiliatemarketing", "#affiliate", "#affiliateprogram", "#passiveincome", "#makemoneyonline"],
    "E-commerce": ["#ecommerce", "#onlinebusiness", "#shopify", "#dropshipping", "#entrepreneur"],
    "Finance": ["#finance", "#investment", "#trading", "#crypto", "#fintech"],
    "Technology": ["#technology", "#tech", "#saas", "#software", "#startup"],
    "Education": ["#education", "#learning", "#onlinecourse", "#elearning", "#edtech"],
    "General": ["#marketing", "#business", "#entrepreneur", "#success", "#income"]
}

# Sidebar - Input Options
st.sidebar.header("⚙️ Tùy chọn quảng cáo")

# Product/Program Info
product_name = st.sidebar.text_input("📦 Tên sản phẩm/chương trình", "Chương trình Affiliate")
product_url = st.sidebar.text_input("🔗 Link đăng ký", "https://example.com/affiliate")
commission = st.sidebar.text_input("💰 % Hoa hồng (vd: 20)", "")
niche = st.sidebar.selectbox("🎯 Lĩnh vực", ["Affiliate Marketing", "E-commerce", "Finance", "Technology", "Education", "General"])

# Ad Type Selection
ad_type = st.sidebar.selectbox("📱 Loại quảng cáo", list(AD_TEMPLATES.keys()))

# Tone Selection
tone = st.sidebar.selectbox("🎭 Tone giọng điệu", ["Chuyên nghiệp", "Thân thiện", "Hứng khởi", "Cấp thiết"])

# Custom inputs
custom_description = st.sidebar.text_area("✍️ Mô tả tùy chỉnh (tùy chọn)", "")
num_ads = st.sidebar.slider("🔢 Số lượng quảng cáo tạo", 1, 10, 3)

# Generate Button
if st.sidebar.button("🎨 Tạo quảng cáo", type="primary"):
    st.header("📝 Quảng cáo được tạo")
    
    generated_ads = []
    
    for i in range(num_ads):
        # Select random components
        hook = random.choice(HOOKS).replace("{product}", product_name)
        if commission:
            hook = hook.replace("{commission}", commission)
        
        cta = random.choice(CTAS)
        
        # Select random benefits
        selected_benefits = random.sample(BENEFITS, min(3, len(BENEFITS)))
        benefits_text = "\n".join(selected_benefits)
        
        # Description
        if custom_description:
            description = custom_description
        else:
            descriptions = [
                f"Tham gia {product_name} và bắt đầu hành trình kiếm tiền online của bạn!",
                f"{product_name} - Chương trình affiliate uy tín, minh bạch và hiệu quả.",
                f"Với {product_name}, bạn có thể tạo thu nhập thụ động chỉ với vài click chuột.",
                f"Hàng nghìn người đã thành công với {product_name}. Bạn sẽ là người tiếp theo!",
            ]
            description = random.choice(descriptions)
        
        # Hashtags
        hashtags = " ".join(random.sample(HASHTAG_GROUPS[niche], min(5, len(HASHTAG_GROUPS[niche]))))
        
        # Generate ad based on template
        template = AD_TEMPLATES[ad_type]["template"]
        
        if ad_type == "Email Subject":
            ad_text = template.replace("{hook}", hook.split("!")[0]).replace("{benefit}", selected_benefits[0].replace("✓ ", ""))
        elif ad_type == "Banner Ad":
            headline = hook
            ad_text = template.replace("{headline}", headline).replace("{description}", description[:50] + "...").replace("{cta}", cta)
        elif ad_type == "Twitter/X Post":
            # Twitter needs to be shorter
            short_desc = description[:80] + "..." if len(description) > 80 else description
            ad_text = template.replace("{hook}", hook).replace("{description}", short_desc).replace("{cta}", cta).replace("{hashtags}", " ".join(random.sample(HASHTAG_GROUPS[niche], 3)))
        elif ad_type == "Google Ads":
            headline = hook[:30] if len(hook) > 30 else hook
            short_desc = description[:90] if len(description) > 90 else description
            ad_text = template.replace("{headline}", headline).replace("{description}", short_desc).replace("{url}", product_url)
        else:
            ad_text = template.replace("{hook}", hook).replace("{description}", description).replace("{benefits}", benefits_text).replace("{cta}", cta).replace("{hashtags}", hashtags)
        
        generated_ads.append({
            "ad_number": i + 1,
            "ad_text": ad_text,
            "length": len(ad_text)
        })
    
    # Display generated ads
    for ad in generated_ads:
        with st.expander(f"📄 Quảng cáo #{ad['ad_number']} - {ad_type} ({ad['length']} ký tự)", expanded=True):
            st.text_area(f"ad_{ad['ad_number']}", ad['ad_text'], height=200, key=f"ad_display_{ad['ad_number']}")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.info(f"Độ dài: {ad['length']}/{AD_TEMPLATES[ad_type]['max_length']} ký tự")
            with col2:
                if ad['length'] > AD_TEMPLATES[ad_type]['max_length']:
                    st.warning("⚠️ Vượt quá độ dài khuyến nghị!")
                else:
                    st.success("✅ Độ dài phù hợp!")
    
    # Export options
    if generated_ads:
        st.header("💾 Xuất quảng cáo")
        
        # Create DataFrame
        df = pd.DataFrame(generated_ads)
        
        # CSV Export
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Tải về CSV",
            data=csv,
            file_name=f"ads_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
        # Text Export
        all_ads_text = "\n\n" + "="*50 + "\n\n".join([f"QUẢNG CÁO #{ad['ad_number']}\n{ad['ad_text']}" for ad in generated_ads])
        st.download_button(
            label="📥 Tải về Text",
            data=all_ads_text.encode('utf-8'),
            file_name=f"ads_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

# Instructions
st.markdown("---")
st.markdown("""
### 📖 Hướng dẫn sử dụng

1. **Nhập thông tin sản phẩm**: Điền tên chương trình, link đăng ký và % hoa hồng
2. **Chọn loại quảng cáo**: Facebook, Instagram, Twitter, Google Ads, Email hoặc Banner
3. **Chọn lĩnh vực**: Để tạo hashtag phù hợp
4. **Tùy chỉnh**: Thêm mô tả riêng nếu muốn
5. **Tạo quảng cáo**: Nhấn nút và nhận ngay nhiều mẫu quảng cáo!

### ✨ Tính năng

- 🎯 Tự động tạo nội dung quảng cáo phù hợp với từng platform
- 📱 Hỗ trợ nhiều loại quảng cáo: Social Media, Google Ads, Email, Banner
- 🔄 Tạo nhiều phiên bản để A/B testing
- 💾 Xuất CSV hoặc Text file
- ✅ Kiểm tra độ dài phù hợp với từng platform

### 🎨 Các loại quảng cáo được hỗ trợ

- **Facebook Post**: Bài viết dạng dài với nhiều emoji và hashtag
- **Instagram Caption**: Tối ưu cho Instagram với format hấp dẫn
- **Twitter/X Post**: Ngắn gọn, trong giới hạn 280 ký tự
- **Google Ads**: Format chuẩn Google Ads với headline và description
- **Email Subject**: Tiêu đề email thu hút
- **Banner Ad**: Nội dung cho banner quảng cáo

""")
