# Affiliate Project Tracker

An automated tool for searching and tracking affiliate programs using Google Custom Search API.

## Features

- 🔍 **Auto-search** affiliate programs across multiple industries
- 🎯 **Multi-keyword support** for refined searches
- 🆕 **Auto-detect** new/latest affiliate programs
- 📊 **Export** results to Excel or CSV
- 🔗 **Extract** signup links automatically
- ⚡ **Concurrent processing** for fast results

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Google API credentials:
```
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CSE_ID=your_cse_id_here
```

## Usage

Run the Streamlit app:
```bash
streamlit run Adsresult.py
```

Then:
1. Select an industry from the dropdown
2. Add optional keywords to refine your search
3. Configure filters (domain, new programs only, etc.)
4. Click "🔄 Cập nhật dữ liệu" to start searching
5. Export results to Excel or CSV

## Industries Supported

Technology, Fashion, Beauty, Health, Fitness, Travel, Food, Finance, Education, Gaming, Home & Garden, Sports, Automotive, Pet Care, Software, Web Hosting, Marketing, E-commerce, Insurance, Real Estate, Photography, Books, Music, Electronics, Toys, Jewelry, Crafts

## Requirements

- Python 3.8+
- Google Custom Search API key
- Google Custom Search Engine ID