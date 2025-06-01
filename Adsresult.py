import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

API_KEY = "AIzaSyBdeW_A4m3P_LDROAL_-Lm_piQ0A6eyjPc"  # Thay bằng API key thực tế
CSE_ID = "51ab9c9ab838a4491"           # Thay bằng Custom Search Engine ID thực tế

def google_search(query, num_results):
    url = "https://www.googleapis.com/customsearch/v1"
    all_items = []
    for i in range(0, num_results, 10):
        params = {
            "key": API_KEY,
            "cx": CSE_ID,
            "q": query,
            "start": i + 1,
        }
        res = requests.get(url, params=params)
        if res.status_code == 200:
            all_items += res.json().get("items", [])
        else:
            st.error(f"Lỗi API Google: {res.status_code}")
            break
    return all_items

def has_affiliate_program(html):
    soup = BeautifulSoup(html, "html.parser")
    affiliate_keywords = [
        "affiliate program", "affiliates", "become an affiliate", 
        "partnership program", "refer and earn", "đối tác tiếp thị", "chương trình affiliate"
    ]
    text = soup.get_text(" ").lower()
    # Kiểm tra anchor chứa từ khóa liên quan affiliate/partner
    for a in soup.find_all("a", href=True):
        if any(keyword in a['href'].lower() for keyword in ["affiliate", "partner"]):
            return True
    return any(keyword in text for keyword in affiliate_keywords)

def has_affiliate_signals(url):
    try:
        r = requests.get(url, timeout=7, headers={"User-Agent": "Mozilla/5.0"})
        html = r.text
        return has_affiliate_program(html)
    except:
        return False

def get_domain(url):
    try:
        netloc = urlparse(url).netloc
        if netloc.startswith("www."):
            netloc = netloc[4:]
        return netloc
    except:
        return ""

st.set_page_config(page_title="Lọc Dự Án Affiliate", page_icon="🔗", layout="centered")
st.title("🔗 Lọc Dự Án Theo Ngành Có Chương Trình Affiliate")

nganh_list = [
    "Wordpress", "AI", "Marketing", "Edu LMS",  "Gaming", "Bitcoin", "Finance App",
    "E-commerce", "Digital Tools & Services", "Hosting", "Online Education", "Software",
    "Baby Products", "Remote Work Tools", "Pet Products", "CRM plugin",
    "Smart home devices", "VPN services", "Coding bootcamps", "Eco-friendly travel", "Budgeting apps & tools","Real Estate"," Personal Finance"," Health & Beauty","Insurance","Digital Marketing ","Pets & Pet Care","Legal & Law Advice"
]
custom_nganh = st.text_input("Hoặc nhập ngành khác (tùy chọn):")
nganh = st.selectbox("🔎 Chọn ngành", nganh_list)
if custom_nganh.strip():
    nganh = custom_nganh.strip()

so_ket_qua = st.slider("📊 Số kết quả Google", 10, 50, 20)
filter_domain = st.text_input("Lọc theo domain (ví dụ: .com, .io, .vn, để trống nếu không lọc):").strip()

if st.button("🚀 Lọc chỉ dự án có Affiliate"):
    with st.spinner("🔍 Đang truy vấn Google và kiểm tra affiliate..."):
        query = f"{nganh} affiliate project"
        results = google_search(query, so_ket_qua)
        if not results:
            st.warning("Không tìm thấy kết quả nào từ Google.")
        else:
            ket_qua_affiliate = []
            progress = st.progress(0)
            total = len(results)
            # Đa luồng để kiểm tra nhanh hơn
            with ThreadPoolExecutor(max_workers=8) as executor:
                futures = {}
                for item in results:
                    link = item.get("link")
                    if not link:
                        continue
                    # Lọc domain nếu người dùng nhập bộ lọc
                    if filter_domain and not link.endswith(filter_domain):
                        continue
                    futures[executor.submit(has_affiliate_signals, link)] = item
                count = 0
                for future in as_completed(futures):
                    item = futures[future]
                    title = item.get("title")
                    link = item.get("link")
                    snippet = item.get("snippet", "")
                    has_aff = future.result()
                    if has_aff:
                        domain = get_domain(link)
                        ket_qua_affiliate.append((title, link, "Có affiliate", domain, snippet))
                    count += 1
                    progress.progress(count / max(len(futures), 1))

            st.success(
                f"✅ Tổng cộng {len(ket_qua_affiliate)} dự án có affiliate cho ngành '{nganh}'."
            )

            st.subheader("Danh sách dự án có affiliate:")
            for title, link, aff, domain, snippet in ket_qua_affiliate:
                st.markdown(
                    f"<a href='{link}' target='_blank'>🔗 {title}</a> &nbsp; | &nbsp; <b>{aff}</b> &nbsp; | &nbsp; 🌐 {domain}",
                    unsafe_allow_html=True
                )
                if snippet:
                    st.markdown(
                        f"<div style='background:#FFF9E1;border-left:4px solid #FFC107;padding:8px 14px;margin:6px 0;color:#444;'><strong>📄 Trích đoạn:</strong><br>{snippet}</div>",
                        unsafe_allow_html=True
                    )

            # Kết quả cho phép tải về
            if ket_qua_affiliate:
                df = pd.DataFrame(
                    ket_qua_affiliate, 
                    columns=["Tiêu đề", "Link", "Affiliate", "Domain", "Trích đoạn"]
                )
                csv = df.to_csv(index=False)
                st.download_button("⬇️ Tải kết quả CSV", csv, "affiliate_only_project.csv", "text/csv")
            else:
                st.info("Không có dự án nào phát hiện có affiliate trong ngành này.")