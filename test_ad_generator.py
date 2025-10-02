#!/usr/bin/env python3
"""
Simple test script for Ad Generator logic
Tests the core functionality without Streamlit UI
"""

import random

# Templates (same as in AdGenerator.py)
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
    "Twitter/X Post": {
        "template": """{hook}

{description}

{cta}

{hashtags}""",
        "max_length": 280
    }
}

HOOKS = [
    "Kiếm tiền online dễ dàng với {product}!",
    "Khám phá cơ hội affiliate tuyệt vời!",
    "💰 Cơ hội kiếm hoa hồng cao đến {commission}%!",
]

CTAS = [
    "Đăng ký ngay hôm nay!",
    "Tham gia ngay để không bỏ lỡ!",
    "Bắt đầu kiếm tiền ngay!",
]

BENEFITS = [
    "✓ Hoa hồng cao và cạnh tranh",
    "✓ Thanh toán đúng hạn",
    "✓ Dashboard theo dõi chi tiết",
]

HASHTAG_GROUPS = {
    "Affiliate Marketing": ["#affiliatemarketing", "#affiliate", "#passiveincome"],
    "E-commerce": ["#ecommerce", "#onlinebusiness", "#entrepreneur"],
}

def generate_ad(product_name, commission, ad_type, niche):
    """Generate a single ad"""
    # Select random components
    hook = random.choice(HOOKS).replace("{product}", product_name)
    if commission:
        hook = hook.replace("{commission}", commission)
    
    cta = random.choice(CTAS)
    
    # Select benefits
    benefits_text = "\n".join(random.sample(BENEFITS, min(3, len(BENEFITS))))
    
    # Description
    description = f"Tham gia {product_name} và bắt đầu hành trình kiếm tiền online của bạn!"
    
    # Hashtags
    hashtags = " ".join(HASHTAG_GROUPS.get(niche, ["#marketing", "#business"]))
    
    # Generate ad
    template = AD_TEMPLATES[ad_type]["template"]
    
    if ad_type == "Twitter/X Post":
        short_desc = description[:80] + "..." if len(description) > 80 else description
        ad_text = template.replace("{hook}", hook).replace("{description}", short_desc).replace("{cta}", cta).replace("{hashtags}", hashtags)
    else:
        ad_text = template.replace("{hook}", hook).replace("{description}", description).replace("{benefits}", benefits_text).replace("{cta}", cta).replace("{hashtags}", hashtags)
    
    return ad_text, len(ad_text)

def test_ad_generation():
    """Test the ad generation functionality"""
    print("="*60)
    print("Testing Ad Generator Logic")
    print("="*60)
    
    # Test case 1: Facebook Post
    print("\n1. Testing Facebook Post generation...")
    ad_text, length = generate_ad("Shopify Affiliate", "20", "Facebook Post", "E-commerce")
    print(f"\nGenerated Ad (Length: {length}):")
    print("-"*60)
    print(ad_text)
    print("-"*60)
    assert len(ad_text) > 0, "Ad text should not be empty"
    assert "Shopify Affiliate" in ad_text, "Product name should be in ad"
    print("✅ Facebook Post test passed!")
    
    # Test case 2: Twitter Post
    print("\n2. Testing Twitter/X Post generation...")
    ad_text, length = generate_ad("HubSpot Partner", "15", "Twitter/X Post", "Affiliate Marketing")
    print(f"\nGenerated Ad (Length: {length}):")
    print("-"*60)
    print(ad_text)
    print("-"*60)
    assert len(ad_text) > 0, "Ad text should not be empty"
    assert length <= 280, f"Twitter post should be <= 280 chars, got {length}"
    print("✅ Twitter/X Post test passed!")
    
    # Test case 3: Multiple generations
    print("\n3. Testing multiple ad generations...")
    ads = []
    for i in range(5):
        ad_text, length = generate_ad("Test Product", "25", "Facebook Post", "E-commerce")
        ads.append(ad_text)
    
    # Check that ads are different (randomization works)
    unique_ads = set(ads)
    print(f"Generated {len(ads)} ads, {len(unique_ads)} unique")
    assert len(unique_ads) > 1, "Multiple generations should produce different ads"
    print("✅ Multiple generations test passed!")
    
    print("\n" + "="*60)
    print("All tests passed! ✅")
    print("="*60)

if __name__ == "__main__":
    try:
        test_ad_generation()
        print("\n✨ Ad Generator logic is working correctly!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        exit(1)
