# Project Architecture

## Overview
```
┌─────────────────────────────────────────────────────────┐
│         Marketing Tools Suite                          │
│         Bộ công cụ Marketing tự động                    │
└─────────────────────────────────────────────────────────┘
                          │
         ┌────────────────┴────────────────┐
         │                                 │
         ▼                                 ▼
┌──────────────────┐              ┌──────────────────┐
│ Affiliate        │              │ Ad Generator     │
│ Project Tracker  │              │ (Tạo quảng cáo)  │
│                  │              │                  │
│ (Adsresult.py)   │              │ (AdGenerator.py) │
└──────────────────┘              └──────────────────┘
         │                                 │
         ▼                                 ▼
   Google Search                    Template Engine
   Web Scraping                     Random Generation
   Data Export                      Multiple Formats
```

## Component Details

### 1. Home.py (Trang chủ)
```
┌────────────────────────────┐
│    Marketing Tools Suite   │
├────────────────────────────┤
│                            │
│  ┌──────────────────────┐  │
│  │ Affiliate Tracker    │  │
│  │ • Tìm chương trình   │  │
│  │ • Thu thập data      │  │
│  └──────────────────────┘  │
│                            │
│  ┌──────────────────────┐  │
│  │ Ad Generator         │  │
│  │ • Tạo quảng cáo      │  │
│  │ • Nhiều platform     │  │
│  └──────────────────────┘  │
│                            │
│  [Documentation Links]     │
└────────────────────────────┘
```

### 2. Adsresult.py (Affiliate Tracker)
```
┌────────────────────────────────────┐
│  Input                             │
├────────────────────────────────────┤
│  • Ngành nghề                      │
│  • Từ khóa                         │
│  • Domain filter                   │
│  • Số kết quả                      │
└────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  Processing                        │
├────────────────────────────────────┤
│  1. Google Custom Search API       │
│  2. Get URLs                       │
│  3. Web Scraping (BeautifulSoup)   │
│  4. Extract info                   │
│  5. Detect new programs            │
│  6. Find signup links              │
└────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  Output                            │
├────────────────────────────────────┤
│  • List of programs                │
│  • Descriptions                    │
│  • Signup links                    │
│  • Excel/CSV export                │
└────────────────────────────────────┘
```

### 3. AdGenerator.py (Ad Generator)
```
┌────────────────────────────────────┐
│  Input                             │
├────────────────────────────────────┤
│  • Product name                    │
│  • Commission %                    │
│  • URL                             │
│  • Niche/Category                  │
│  • Ad type (Facebook, etc)         │
│  • Number of ads                   │
└────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  Template Engine                   │
├────────────────────────────────────┤
│  1. Select template                │
│  2. Generate hook                  │
│  3. Generate CTA                   │
│  4. Generate benefits              │
│  5. Generate hashtags              │
│  6. Combine components             │
│  7. Check length                   │
└────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  Output                            │
├────────────────────────────────────┤
│  • Multiple ad versions            │
│  • Length validation               │
│  • CSV/Text export                 │
└────────────────────────────────────┘
```

## Data Flow

### Workflow 1: Find Affiliate Programs
```
User Input
    ↓
[Adsresult.py]
    ↓
Google Custom Search API
    ↓
Web Scraping
    ↓
Data Processing
    ↓
Excel/CSV File
    ↓
User Analysis
```

### Workflow 2: Generate Ads
```
User Input (Product info)
    ↓
[AdGenerator.py]
    ↓
Template Selection
    ↓
Random Generation
    ↓
Ad Assembly
    ↓
Multiple Ad Versions
    ↓
CSV/Text Export
    ↓
Deploy to Platforms
```

### Workflow 3: Combined (Recommended)
```
[Adsresult.py] → Find Programs
    ↓
Export & Select Best
    ↓
[AdGenerator.py] → Create Ads
    ↓
A/B Test
    ↓
Deploy Best Performing
```

## Technology Stack

```
┌────────────────────────────────────┐
│  Frontend                          │
├────────────────────────────────────┤
│  • Streamlit (Web UI)              │
│  • HTML/CSS (Custom styling)       │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  Backend                           │
├────────────────────────────────────┤
│  • Python 3.8+                     │
│  • Pandas (Data manipulation)      │
│  • BeautifulSoup (Web scraping)    │
│  • Requests (HTTP)                 │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  APIs                              │
├────────────────────────────────────┤
│  • Google Custom Search API        │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  Storage                           │
├────────────────────────────────────┤
│  • CSV Files                       │
│  • Excel Files (.xlsx)             │
│  • Text Files                      │
└────────────────────────────────────┘
```

## File Structure
```
hien/
├── Home.py                 # Navigation page
├── Adsresult.py           # Affiliate finder
├── AdGenerator.py         # Ad creator
├── test_ad_generator.py   # Unit tests
├── requirements.txt       # Dependencies
├── .env.example          # Config template
├── .gitignore            # Git ignore rules
│
├── Documentation:
│   ├── README.md         # Main documentation
│   ├── QUICKSTART.md     # Quick start guide
│   ├── USAGE.md          # Detailed usage
│   ├── EXAMPLES.md       # Sample outputs
│   └── ARCHITECTURE.md   # This file
│
└── .env                  # API keys (not in git)
```

## Module Dependencies

```
Home.py
  └── streamlit

Adsresult.py
  ├── streamlit
  ├── requests
  ├── pandas
  ├── beautifulsoup4
  ├── google-api-python-client
  ├── python-dotenv
  └── openpyxl

AdGenerator.py
  ├── streamlit
  ├── pandas
  └── random (built-in)

test_ad_generator.py
  └── random (built-in)
```

## Scalability Considerations

### Current Architecture
- ✅ Single user application
- ✅ Local data storage
- ✅ Simple deployment

### Future Enhancements
- 🔄 Multi-user support
- 🔄 Database integration (PostgreSQL)
- 🔄 API endpoints (REST API)
- 🔄 Cloud deployment (AWS/GCP)
- 🔄 Authentication system
- 🔄 AI integration (OpenAI GPT)
- 🔄 Analytics dashboard
- 🔄 Scheduled automation

## Security

### Current Measures
- ✅ .env file for API keys
- ✅ .gitignore to exclude sensitive files
- ✅ No hardcoded credentials

### Best Practices
- 🔐 Never commit .env file
- 🔐 Use environment variables
- 🔐 Validate user input
- 🔐 Rate limiting for APIs
- 🔐 Error handling

## Performance

### Optimization Strategies
1. **Adsresult.py**
   - Concurrent URL processing (ThreadPoolExecutor)
   - Configurable concurrency (1-20 threads)
   - Request timeout (5 seconds)
   - Caching with Streamlit @cache_data

2. **AdGenerator.py**
   - No external API calls
   - Pure Python logic
   - Instant generation
   - Minimal memory usage

## Error Handling

```
┌────────────────────────────────────┐
│  Error Type                        │
├────────────────────────────────────┤
│  • API Key Missing      → Clear msg│
│  • Network Error        → Retry    │
│  • Timeout              → Skip URL │
│  • Invalid Input        → Validate │
│  • Scraping Error       → Log      │
└────────────────────────────────────┘
```

## Testing Strategy

### Current Tests
- ✅ Unit test for AdGenerator logic
- ✅ Template generation
- ✅ Length validation
- ✅ Randomization

### Future Tests
- 🔄 Integration tests
- 🔄 E2E tests with Selenium
- 🔄 API mocking tests
- 🔄 Performance tests

---

**Last Updated:** 2025-01-02
