# Swoop Service Auto - System Architecture

## Complete System Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        SWOOP SERVICE AUTO SYSTEM                        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                           USER INTERFACES                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────┐           ┌──────────────────────┐           │
│  │   Streamlit Web App  │           │   Mobile Mechanic    │           │
│  │   (app.py)           │           │   App (React/Swift)  │           │
│  │                      │           │                      │           │
│  │  - Vehicle Selection │           │  - Job Dashboard     │           │
│  │  - Service Catalog   │           │  - Customer Info     │           │
│  │  - Doc Generation    │           │  - Service Docs      │           │
│  │  - Browse Cache      │           │  - Tech Notes        │           │
│  │                      │           │                      │           │
│  │  Port: 8501          │           │  iOS/Android         │           │
│  └──────────┬───────────┘           └──────────┬───────────┘           │
│             │                                   │                       │
└─────────────┼───────────────────────────────────┼───────────────────────┘
              │                                   │
              │                                   │
┌─────────────┼───────────────────────────────────┼───────────────────────┐
│             │         API LAYER                 │                       │
├─────────────┼───────────────────────────────────┼───────────────────────┤
│             │                                   │                       │
│             ▼                                   ▼                       │
│  ┌─────────────────────────────────────────────────────────┐           │
│  │          FastAPI REST API (api.py)                      │           │
│  │          Port: 8000                                     │           │
│  ├─────────────────────────────────────────────────────────┤           │
│  │  Authentication: X-API-Key header                       │           │
│  │  Documentation: /docs (Swagger UI)                      │           │
│  ├─────────────────────────────────────────────────────────┤           │
│  │  Endpoints:                                             │           │
│  │    GET  /api/v1/health                                  │           │
│  │    GET  /api/v1/vehicles/search?q=camry                │           │
│  │    GET  /api/v1/vehicles/makes                          │           │
│  │    GET  /api/v1/services                                │           │
│  │    POST /api/v1/documentation/generate                  │           │
│  │    GET  /api/v1/documentation/{id}/html                 │           │
│  └─────────────────────┬───────────────────────────────────┘           │
│                        │                                               │
└────────────────────────┼───────────────────────────────────────────────┘
                         │
                         │
┌────────────────────────┼───────────────────────────────────────────────┐
│             SERVICE DOCUMENTATION GENERATOR                             │
├────────────────────────┼───────────────────────────────────────────────┤
│                        │                                               │
│                        ▼                                               │
│  ┌─────────────────────────────────────────────────────────┐           │
│  │  ServiceDocGenerator (tools/service_doc_generator.py)   │           │
│  ├─────────────────────────────────────────────────────────┤           │
│  │  1. Load vehicle from database                          │           │
│  │  2. Load service requirements                           │           │
│  │  3. Check cache (service_docs/)                         │           │
│  │  4. If not cached:                                      │           │
│  │     a) Research with AI (specs, procedures)             │           │
│  │     b) Format with AI (professional HTML)               │           │
│  │     c) Save to cache                                    │           │
│  │  5. Return document path                                │           │
│  └─────────────────────┬───────────────────────────────────┘           │
│                        │                                               │
└────────────────────────┼───────────────────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼
┌──────────────────┐            ┌──────────────────┐
│   Research AI    │            │   Formatter AI   │
│                  │            │                  │
│  Provider:       │            │  Provider:       │
│  - Perplexity    │            │  - OpenAI        │
│  - OpenRouter    │            │  - Anthropic     │
│  - OpenAI        │            │  - OpenRouter    │
│                  │            │                  │
│  Task:           │            │  Task:           │
│  - Find specs    │            │  - Create HTML   │
│  - Get torques   │            │  - Format tables │
│  - Research      │            │  - Structure     │
│    procedures    │            │    sections      │
│                  │            │                  │
│  ~15 seconds     │            │  ~2-3 seconds    │
└──────────────────┘            └──────────────────┘
        │                                 │
        └────────────────┬────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          DATA STORAGE                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────┐  ┌────────────────────┐  ┌──────────────────┐  │
│  │  vehicles.json     │  │  services.json     │  │  service_docs/   │  │
│  │                    │  │                    │  │                  │  │
│  │  2,270 vehicles    │  │  782 services      │  │  Generated HTML  │  │
│  │  - Year/Make/Model │  │  - Name/Category   │  │  - Cached docs   │  │
│  │  - Engine/Trans    │  │  - Labor time      │  │  - Quick access  │  │
│  │  - Body style      │  │  - Difficulty      │  │  - < 100ms load  │  │
│  │  - Specs           │  │  - Description     │  │                  │  │
│  │                    │  │                    │  │  cache_index.json│  │
│  └────────────────────┘  └────────────────────┘  └──────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Data Flow for Mobile App Integration

### When Customer Books Job:

```
┌──────────────────────────────────────────────────────────────────┐
│ 1. Customer Books Job in Mobile App                             │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                       │ Customer Info:
                       │ - 2015 Toyota Camry
                       │ - 2.5L 4-Cyl
                       │ - Service: Oil Change
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────┐
│ 2. Mobile App Backend Calls API                                 │
│                                                                  │
│    POST /api/v1/documentation/generate                          │
│    Headers: X-API-Key: your-key                                 │
│    Body: {                                                      │
│      "year": 2015,                                              │
│      "make": "Toyota",                                          │
│      "model": "Camry",                                          │
│      "service": "Oil Change",                                   │
│      "engine": "2.5L 4-Cyl"                                     │
│    }                                                            │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────┐
│ 3. API Checks Cache                                             │
│                                                                  │
│    Cache Key: 2015_toyota_camry_oil_change_2.5l                │
│                                                                  │
│    ┌─────────────┐                                              │
│    │ In Cache?   │                                              │
│    └──┬─────┬────┘                                              │
│       │ YES │ NO                                                │
└───────┼─────┼──────────────────────────────────────────────────┘
        │     │
        │     ▼
        │  ┌──────────────────────────────────────────────┐
        │  │ 4a. Generate Documentation (~15 seconds)     │
        │  │                                              │
        │  │  1. Research AI finds:                       │
        │  │     - Oil capacity (4.6 qts)                 │
        │  │     - Filter part# (90915-YZZF2)            │
        │  │     - Drain plug torque (27 ft-lbs)          │
        │  │     - Procedure steps                        │
        │  │                                              │
        │  │  2. Formatter AI creates:                    │
        │  │     - Professional HTML                      │
        │  │     - Torque spec table                      │
        │  │     - Step-by-step procedure                 │
        │  │     - Parts list                             │
        │  │                                              │
        │  │  3. Save to cache                            │
        │  └──────────────────────────────────────────────┘
        │             │
        ▼             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 4b/5. Return Response (<100ms cached, ~15s new)                 │
│                                                                  │
│    {                                                             │
│      "status": "success",                                        │
│      "doc_id": "abc123...",                                      │
│      "from_cache": false,                                        │
│      "generation_time": 14.52,                                   │
│      "html_url": "/api/v1/documentation/abc123.../html"         │
│    }                                                             │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────┐
│ 6. Mobile App Displays in Tech Dashboard                        │
│                                                                  │
│    WebView loads:                                                │
│    GET /api/v1/documentation/abc123.../html                     │
│                                                                  │
│    Tech sees:                                                    │
│    - Complete procedure                                          │
│    - Torque specifications                                       │
│    - Parts needed                                                │
│    - Troubleshooting tips                                        │
│    - Common issues                                               │
│                                                                  │
│    ✅ Tech is ready to work!                                     │
└──────────────────────────────────────────────────────────────────┘
```

## Performance Characteristics

### First Generation (Not Cached)
```
Request → API Auth (10ms)
       → Check Cache (50ms) → MISS
       → Load Vehicle Data (100ms)
       → Research AI (10-15s)
       → Format AI (2-3s)
       → Save to Cache (200ms)
       → Return Response
       
Total: ~15-20 seconds
```

### Subsequent Requests (Cached)
```
Request → API Auth (10ms)
       → Check Cache (50ms) → HIT
       → Read HTML (20ms)
       → Return Response
       
Total: <100ms
```

## Security Model

```
┌─────────────────────────────────────────────────────────┐
│                   Security Layers                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  1. API Key Authentication                               │
│     ├─ X-API-Key header required                        │
│     ├─ Configured in .env                               │
│     └─ Validated on every request                       │
│                                                          │
│  2. CORS Configuration                                   │
│     ├─ Restrict allowed origins                         │
│     ├─ Production: specific domains only                │
│     └─ Development: * (all origins)                     │
│                                                          │
│  3. Environment Variables                                │
│     ├─ No secrets in code                               │
│     ├─ .env file for configuration                      │
│     └─ .env.example for reference                       │
│                                                          │
│  4. Input Validation                                     │
│     ├─ Pydantic models validate all inputs              │
│     ├─ Type checking on all parameters                  │
│     └─ Error messages on invalid data                   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Deployment Architecture

### Development (Current Setup)
```
Local Machine
  ├─ Streamlit App: http://localhost:8501
  ├─ REST API: http://localhost:8000
  ├─ Tailscale Access: http://your-tailscale-ip:8000
  └─ Direct file access to service_docs/
```

### Production (Recommended)
```
Cloud Server (DigitalOcean/AWS/etc.)
  │
  ├─ Nginx Reverse Proxy (HTTPS)
  │   ├─ api.swoopservice.com → Port 8000 (API)
  │   └─ app.swoopservice.com → Port 8501 (Web App)
  │
  ├─ FastAPI Application
  │   ├─ Uvicorn workers (multiple)
  │   ├─ Rate limiting middleware
  │   ├─ Request logging
  │   └─ Error tracking
  │
  ├─ File Storage
  │   ├─ service_docs/ (cached HTML)
  │   ├─ data/ (vehicles.json, services.json)
  │   └─ Regular backups
  │
  └─ Environment
      ├─ Python virtual environment
      ├─ .env with production keys
      └─ Systemd service for auto-start
```

## Technology Stack

```
┌────────────────────────────────────────────────────────┐
│                  Frontend / Client                     │
├────────────────────────────────────────────────────────┤
│  • Streamlit (Web UI)                                  │
│  • React Native (Mobile - iOS/Android)                 │
│  • Swift/UIKit (iOS Native)                            │
│  • Kotlin/Android SDK (Android Native)                 │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│                    API Layer                           │
├────────────────────────────────────────────────────────┤
│  • FastAPI (REST API framework)                        │
│  • Uvicorn (ASGI server)                               │
│  • Pydantic (Data validation)                          │
│  • CORS middleware                                      │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│                 Business Logic                         │
├────────────────────────────────────────────────────────┤
│  • ServiceDocGenerator (Core generator)                │
│  • AIClient (Multi-provider AI interface)              │
│  • Cache management (JSON index + HTML files)          │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│                   AI Providers                         │
├────────────────────────────────────────────────────────┤
│  • Perplexity Sonar (Research with web access)         │
│  • OpenAI GPT-4 (Formatting and structuring)           │
│  • Anthropic Claude (Alternative formatter)            │
│  • OpenRouter (Multi-model access)                     │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│                  Data Storage                          │
├────────────────────────────────────────────────────────┤
│  • JSON (Vehicle and service databases)                │
│  • HTML (Generated service documents)                  │
│  • File system (Cache and storage)                     │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│                Infrastructure                          │
├────────────────────────────────────────────────────────┤
│  • Python 3.8+ (Runtime)                               │
│  • Virtual environment (Isolation)                     │
│  • Git (Version control)                               │
│  • GitHub (Repository hosting)                         │
│  • Streamlit Cloud (Web app deployment - optional)     │
└────────────────────────────────────────────────────────┘
```

## File Organization

```
/home/eanhd/projects/vehicles/
│
├── app.py                          # Streamlit web interface
├── api.py                          # FastAPI REST API
│
├── data/
│   ├── vehicles.json               # 2,270 vehicles
│   └── services.json               # 782 services
│
├── tools/
│   ├── service_doc_generator.py    # Main generator
│   ├── service_doc_generator_refactored.py  # HTML templates
│   ├── ai_client.py                # Multi-provider AI client
│   ├── diagram_generator.py        # Optional image generation
│   └── batch_generate.py           # Batch operations
│
├── service_docs/                   # Cache directory
│   ├── cache_index.json           # Document index
│   └── *.html                     # Cached documents
│
├── docs/                          # System documentation
│   ├── agents/                    # AI agent instructions
│   ├── workflow/                  # Research workflow
│   └── service_system/            # Service system docs
│
├── wip/                           # Research workspace
│   └── [manufacturer]/            # Per-brand data
│
├── start_app.sh                   # Start Streamlit
├── start_api.sh                   # Start FastAPI
├── test_api.py                    # API test suite
│
├── README.md                      # Main documentation
├── API_DOCUMENTATION.md           # API reference
├── API_QUICK_START.md             # API quick start
├── MOBILE_APP_INTEGRATION.md      # Mobile integration guide
├── QUICK_START_APP.md             # Web app guide
│
├── requirements.txt               # Python dependencies
├── .env                          # Configuration (not in git)
└── .env.example                  # Configuration template
```

---

**System Status**: ✅ Fully Operational

- **Web Interface**: http://localhost:8501
- **REST API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Database**: 2,270 vehicles, 782 services
- **Cache**: 8+ documents ready

**Ready for production use!** 🚀
