import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from googleapiclient.discovery import build
from datetime import datetime
import io
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

st.set_page_config(page_title="Affiliate Project Tracker", layout="wide")
st.markdown("<h1 style='text-align: center; color: #f22c74;'>🚀 Affiliate Project Tracker</h1>", unsafe_allow_html=True)

nganh = st.selectbox("🔎 Chọn ngành:", [
    "Technology", "Fashion", "Beauty", "Health", "Fitness",
    "Travel", "Food", "Finance", "Education", "Gaming",
    "Home & Garden", "Sports", "Automotive", "Pet Care",
    "Software", "Web Hosting", "Marketing", "E-commerce",
    "Insurance", "Real Estate", "Photography", "Books",
    "Music", "Electronics", "Toys", "Jewelry", "Crafts"
])
keyword_bo_sung = st.text_input("🔍 Từ khóa thêm (tùy chọn)", "")
keywords_multi = st.text_area("🔑 Nhập nhiều từ khóa (mỗi dòng một từ)", "")
so_ket_qua = st.slider("📊 Số kết quả Google", 5, 50, 20)
domain_input = st.text_input("Nhập domain filter (vd: .com, .vn, ...) (cách nhau dấu phẩy)")
highlight_new = st.checkbox("✅ Đánh dấu dự án mới nhất?", value=True)
filter_new_only = st.checkbox("🆕 Chỉ hiển thị dự án mới?", value=False)
filter_has_signup = st.checkbox("📥 Chỉ hiển thị có link đăng ký affiliate?", value=False)
concurrency = st.slider("⚙️ Số luồng xử lý song song", 1, 20, 10)

st.markdown(f"🕐 Lần cập nhật: **{datetime.now().strftime('%d/%m/%Y %H:%M')}**")

if "logs" not in st.session_state:
    st.session_state["logs"] = []

df = pd.DataFrame()

if st.button("🔄 Cập nhật dữ liệu"):
    domain_filter_list = [d.strip() for d in domain_input.split(",") if d.strip()]

    @st.cache_data(ttl=3600)
    def loc_affiliate_ads(nganh, keyword_bo_sung, keywords_multi, so_ket_qua, domain_filter_list, highlight_new):
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        query = f"affiliate {nganh} program"
        if keyword_bo_sung:
            query += f" {keyword_bo_sung}"
        if keywords_multi:
            keyword_list = [k.strip() for k in keywords_multi.splitlines() if k.strip()]
            query += " (" + " OR ".join(keyword_list) + ")"
        if domain_filter_list:
            query += " (" + " OR ".join([f"site:{d}" for d in domain_filter_list]) + ")"

        urls = set()
        startIndex = 1
        while len(urls) < so_ket_qua:
            try:
                res = service.cse().list(q=query, cx=GOOGLE_CSE_ID, num=min(10, so_ket_qua - len(urls)), start=startIndex).execute()
                for item in res.get("items", []):
                    link = item.get("link")
                    if link and "#" not in link and "utm_" not in link and "ads" not in link:
                        urls.add(link)
                if "nextPage" in res.get("queries", {}):
                    startIndex = res["queries"]["nextPage"][0]["startIndex"]
                else:
                    break
            except Exception as e:
                st.error(f"Lỗi API Google Custom Search: {e}")
                break

        headers = {"User-Agent": "Mozilla/5.0 Chrome/114.0.0.0"}
        keywords_new = ["2025", "2024", "new", "latest", "updated", "launch", "release"]

        def process_url(url):
            try:
                response = requests.get(url, timeout=5, headers=headers)
                html = response.text.lower()
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string.strip() if soup.title else url
                description = soup.find("meta", attrs={"name": "description"})
                description_text = description["content"] if description and description.get("content") else (soup.find("p").get_text(strip=True) if soup.find("p") else "Chưa có mô tả.")
                is_new = False
                if highlight_new:
                    candidates = [title.lower()] + [tag.get_text().lower() for tag in soup.find_all(['h1', 'h2', 'meta'])]
                    is_new = any(k in html for k in keywords_new) or any(k in c for c in candidates for k in keywords_new)

                affiliate_keywords = ["affiliate", "referral", "partner", "commission", "revenue share"]
                if not any(k in html for k in affiliate_keywords):
                    return None

                # Tìm link đăng ký affiliate (nếu có)
                signup_link = ""
                for a in soup.find_all("a", href=True):
                    href = a["href"]
                    text = a.get_text(strip=True).lower()
                    if any(word in href.lower() or word in text for word in ["affiliate", "join", "partner", "signup"]):
                        if href.startswith("http"):
                            signup_link = href
                        else:
                            from urllib.parse import urljoin
                            signup_link = urljoin(url, href)
                        break

                return {
                    'title': title,
                    'url': url,
                    'is_new': is_new,
                    'description': description_text,
                    'signup_link': signup_link
                }
            except Exception as e:
                st.session_state["logs"].append(f"Lỗi xử lý URL {url}: {e}")
                return None

        with st.spinner("⏳ Đang thu thập dữ liệu..."):
            with ThreadPoolExecutor(max_workers=concurrency) as executor:
                ket_qua = list(filter(None, executor.map(process_url, urls)))

        return ket_qua

    results = loc_affiliate_ads(nganh, keyword_bo_sung, keywords_multi, so_ket_qua, domain_filter_list, highlight_new)

    if results:
        df = pd.DataFrame(results)
        if filter_new_only:
            df = df[df['is_new']]
        if filter_has_signup:
            df = df[df['signup_link'] != ""]

        for item in df.to_dict(orient="records"):
            st.markdown(f"""
                <div style='border:1px solid #444;padding:10px;border-radius:10px;margin-bottom:10px;background:#111;'>
                    <h4 style='color:#f767a1'>{'🆕 ' if item['is_new'] else ''}{item['title']}</h4>
                    <p style='color:#ccc;'>🌐 <a href="{item['url']}" target="_blank">{item['url']}</a></p>
                    {"<p style='color:#90ee90;'>📝 <b>Đăng ký:</b> <a href='" + item['signup_link'] + "' target='_blank'>" + item['signup_link'] + "</a></p>" if item['signup_link'] else ""}
                    <p style='color:#bbb;'>📄 {item['description']}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Không tìm thấy dữ liệu phù hợp.")

# Xuất Excel/CSV
if not df.empty:
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    st.download_button("📥 Tải về Excel", data=excel_buffer.getvalue(), file_name="affiliate_programs.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    csv_buffer = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Tải về CSV", data=csv_buffer, file_name="affiliate_programs.csv", mime="text/csv")

if st.session_state["logs"]:
    with st.expander("📄 Xem log lỗi chi tiết"):
        for log in st.session_state["logs"]:
            st.text(log)
