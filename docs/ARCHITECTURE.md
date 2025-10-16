# 🏗️ Swoop Service Auto - System Architecture

## Overview

Swoop Service Auto is a comprehensive automotive service documentation system that combines a curated vehicle database with AI-powered research to generate professional repair guides. The system is designed for mobile mechanics who need reliable, professional documentation in the field.

---

## 🎯 Core Objectives

1. **Accurate Data**: Wikipedia-sourced vehicle specifications with full citations
2. **Professional Output**: ALLDATA-quality documentation with torque specs, diagrams, and procedures
3. **Cost-Effective**: Smart caching eliminates repeat costs; uses budget-friendly AI models
4. **Mobile-First**: Works on phones/tablets via Tailscale; offline-capable
5. **Production-Ready**: Suitable for real-world mechanic use; professional enough for customers

---

## 📊 System Components

### 1. Data Layer

#### vehicles.json (2,270+ entries)
- **Structure**: Array of vehicle objects
- **Coverage**: 48 manufacturers, 1910s-2025
- **Schema**: 12 required fields per entry
  - years, make, model, engines, transmissions
  - region, drivetrain, body_styles
  - hybrid, diesel, difficulty_modifier, notes

#### services.json (100+ services)
- **Categories**: Brakes, Engine, Maintenance, Electrical, etc.
- **Fields**: name, category, labor_time_hours, price_range_labor, price_range_parts
- **Mobile flag**: Indicates if service can be performed on-site

#### Backup System
- Timestamped backups in `backups/` directory
- Created before every merge operation
- Format: `vehicles_YYYYMMDD_HHMMSS.json`

### 2. Research Layer

#### AI Client (Hybrid Model)

**Research AI (Perplexity Sonar Pro)**
- **Purpose**: Web-connected research for accurate, current information
- **Model**: `sonar-pro` (web access, citations)
- **Cost**: ~$0.01-0.05 per query
- **Temperature**: 0.2 (factual, minimal creativity)
- **Max Tokens**: 4000

**Formatter AI (OpenAI GPT-4o-mini)**
- **Purpose**: Structure formatting, HTML generation
- **Model**: `gpt-4o-mini` (fast, cheap, good formatting)
- **Cost**: ~$0.001-0.01 per document
- **Temperature**: 0.3 (slightly creative for good phrasing)
- **Max Tokens**: 8000

**Configurable via .env:**
```bash
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro
FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
```

### 3. Generation Layer

#### Service Documentation Generator

**Flow:**
```
1. User Input (year, make, model, service)
   ↓
2. Check Cache (MD5 hash key)
   ├─ Hit → Return cached document (instant, free)
   └─ Miss → Continue to step 3
   ↓
3. Database Lookup
   ├─ Find vehicle in vehicles.json
   └─ Find service in services.json
   ↓
4. AI Research (Perplexity)
   - Build detailed prompt with vehicle specs
   - Query for: procedure, torque specs, parts, common issues
   - Parse JSON response
   ↓
5. HTML Generation (GPT-4o-mini)
   - Professional styling (Swoop Service Auto branding)
   - Mobile-responsive layout
   - Safety warnings, tips, citations
   ↓
6. Cache Document
   - Save to: service_docs/Make/Model/Year_Service.html
   - Update cache_index.json
   ↓
7. Return Document Path
```

**Cache Key Generation:**
```python
cache_key = md5(f"{year}_{make}_{model}_{service}".lower())
```

**Directory Structure:**
```
service_docs/
├── cache_index.json           # Fast lookup index
├── Ford/
│   ├── F-150/
│   │   ├── 2020_Oil_Change.html
│   │   ├── 2020_Brake_Pads_Replacement_Front.html
│   │   └── 2019_Oil_Change.html
│   └── Mustang/
│       └── 2020_Spark_Plugs_Replacement.html
└── Toyota/
    └── Camry/
        └── 2020_Oil_Change.html
```

### 4. Interface Layer

#### Web App (Streamlit)

**Pages:**

1. **Generate Service Doc**
   - Interactive vehicle selection (Make → Model → Year)
   - Service selection with category filtering
   - Real-time vehicle details display
   - Generate or retrieve from cache
   - Preview, download, or open in browser

2. **Browse Cache**
   - Searchable table of cached documents
   - Filter by make and service
   - Quick view functionality

3. **AI Assistant**
   - Context-aware chat interface
   - Uses Research AI for answers
   - Can reference last generated document

4. **Statistics**
   - Vehicle database analytics
   - Cache usage metrics
   - Top manufacturers and services

5. **Settings**
   - AI configuration display
   - Cache management
   - System information

**Features:**
- Mobile-responsive design
- Professional styling
- Fast load times
- Works via Tailscale

#### REST API (Flask)

**Endpoints:**

- `GET /api/service_doc` - Generate/retrieve document
  - Query: year, make, model, service, force, format
  - Returns: HTML or JSON

- `GET /api/vehicles` - Search vehicles
  - Query: make, model, year, limit
  - Returns: Array of matching vehicles

- `GET /api/services` - List services
  - Query: category, mobile
  - Returns: Array of services

- `GET /api/cache/stats` - Cache statistics
  - Returns: Document counts by make and service

- `GET /api/popular` - Popular combinations
  - Returns: List of high-demand vehicle/service pairs

**Usage:**
```bash
# Start API server
python tools/service_api.py --port 5000

# Generate document
curl "http://localhost:5000/api/service_doc?year=2020&make=Ford&model=F-150&service=Oil%20Change"

# Search vehicles
curl "http://localhost:5000/api/vehicles?make=Ford&model=F-150"
```

---

## 🔄 Data Flow Diagrams

### Document Generation Flow

```
User Request
    ↓
[Web App / CLI / API]
    ↓
ServiceDocGenerator
    ↓
Cache Check? ──Yes──→ Return Cached Doc (instant, free)
    ↓ No
Database Lookup
    ↓
[vehicles.json] ← Find vehicle specs
[services.json] ← Find service details
    ↓
AI Research (Perplexity)
    ↓
Research Data (JSON)
    ↓
HTML Generation
    ↓
Save to Cache
    ↓
Return New Doc
```

### AI Research Flow

```
Build Prompt
├─ Vehicle: year, make, model, engines, transmissions
├─ Service: name, category, labor_time
└─ Request: procedure, torque_specs, parts, issues, warnings
    ↓
Perplexity API
├─ Web search enabled
├─ Citations included
└─ JSON structured response
    ↓
Parse Response
├─ Extract JSON from markdown
├─ Validate structure
└─ Fallback to text if needed
    ↓
Return Research Data
```

---

## 💾 Data Management

### vehicles.json Workflow

**Phase 1: Research**
- Create `wip/[manufacturer]/` workspace
- Research Wikipedia generation-specific pages
- Create isolated `[decade].json` files (1910s, 1920s, etc.)

**Phase 2: Validation**
- Validate each decade: `jq empty [decade].json`
- Check all 12 required fields present
- Verify Wikipedia citations included

**Phase 3: Merge**
- Backup: `cp data/vehicles.json backups/vehicles_$(date +%Y%m%d_%H%M%S).json`
- Merge: `jq -s '.[0] + .[1] + ...' data/vehicles.json wip/.../[decades].json > temp.json`
- Validate merged: `jq empty temp.json`
- Replace: `mv temp.json data/vehicles.json`

**Phase 4: Archive**
- Rename decade files with `_APPENDED` suffix
- Create completion report
- Update CHECKLIST.md

### Cache Management

**Automatic:**
- Documents cached on first generation
- Cache index updated atomically
- No expiration (manual cleanup only)

**Manual:**
- View cache: `ls -lh service_docs/`
- Clear cache: `rm -rf service_docs/*` (except cache_index.json)
- Rebuild index: App auto-rebuilds on next run

---

## 🔐 Security & Privacy

### API Keys
- Stored in `.env` (gitignored)
- Never committed to repository
- Separate keys for research and formatting
- Rotation supported (just update .env)

### Data Privacy
- All vehicle specs from public Wikipedia data
- Generated docs stored locally
- Only research queries sent to AI providers
- No PII collected or transmitted

### Access Control
- Tailscale for private network access
- Optional: Add Streamlit authentication
- Optional: Flask API authentication
- Consider IP whitelisting for production

---

## 💰 Cost Analysis

### Per-Document Costs

**New Generation (cache miss):**
- Research AI (Perplexity): $0.01-0.05
- Formatter AI (GPT-4o-mini): $0.001-0.01
- **Total: $0.01-0.06 per document**

**Cached Retrieval (cache hit):**
- No AI calls
- **Total: $0.00 (FREE!)**

### Cost Optimization Strategies

1. **Pre-generation**
   - Generate common vehicles during downtime
   - Build cache before field use
   - Batch generate top 100 combinations

2. **Cache Utilization**
   - Check cache before generating
   - Download docs for offline use
   - Share cache across team

3. **Smart Model Selection**
   - Perplexity for research (web access needed)
   - GPT-4o-mini for formatting (fast, cheap)
   - Avoid expensive models (Claude, GPT-4)

### Monthly Cost Estimates

**Low Usage (10 new docs/month):**
- $0.50-0.60/month

**Medium Usage (100 new docs/month):**
- $5-6/month

**High Usage (500 new docs/month):**
- $25-30/month

**Note:** Cached documents are FREE - costs only apply to NEW generations!

---

## 🚀 Deployment Architectures

### Option 1: Single-User (Tailscale)

```
[Laptop/Desktop]
├─ Python + Streamlit
├─ Local SQLite cache
└─ Tailscale daemon
    ↓
[Phone/Tablet via Tailscale]
```

**Pros:** Simple, secure, no hosting costs
**Cons:** Main machine must be running

### Option 2: Multi-User (Cloud)

```
[Streamlit Cloud / Heroku / AWS]
├─ Web app accessible via HTTPS
├─ Shared cache (S3/persistent volume)
└─ Environment secrets
    ↓
[Any device via internet]
```

**Pros:** Always available, team access
**Cons:** Hosting costs, API keys in cloud

### Option 3: Shop Server (Docker)

```
[Shop Server]
├─ Docker container
├─ Volume-mounted cache
└─ Reverse proxy (nginx)
    ↓
[Shop network devices]
```

**Pros:** Full control, persistent cache, fast
**Cons:** Requires server, Docker knowledge

---

## 📈 Performance Characteristics

### Document Generation Times

| Operation | Time | Cost |
|-----------|------|------|
| Cache hit | <100ms | $0.00 |
| Cache miss (new gen) | 30-60s | $0.01-0.06 |
| Batch generation (100 docs) | 1-2 hours | $1-6 |

### Database Query Performance

| Operation | Time | Notes |
|-----------|------|-------|
| Find vehicle by year/make/model | <10ms | In-memory JSON |
| List all makes | <5ms | Cached in memory |
| Filter by year range | <50ms | O(n) scan |

### Cache Performance

| Operation | Time | Notes |
|-----------|------|-------|
| Cache lookup | <5ms | MD5 hash, dict lookup |
| Cache write | <50ms | File write + index update |
| Cache index load | <100ms | JSON parse on startup |

---

## 🔧 Maintenance & Operations

### Regular Tasks

**Daily:**
- Monitor cache size (target: <1GB)
- Check AI connection status
- Review error logs

**Weekly:**
- Backup vehicles.json
- Clear unused cached docs
- Review cost usage

**Monthly:**
- Update AI model versions
- Rotate API keys (if needed)
- Review and optimize cache

### Monitoring

**Key Metrics:**
- Cache hit rate (target: >80%)
- Average generation time
- API costs per day
- Error rate

**Tools:**
- Streamlit Statistics page
- Flask API `/api/cache/stats`
- System logs

### Troubleshooting

**Common Issues:**

1. **Slow generation**
   - Check internet connection
   - Verify AI provider status
   - Consider increasing timeout

2. **High costs**
   - Check cache hit rate
   - Review generation patterns
   - Pre-generate common docs

3. **Cache corruption**
   - Delete cache_index.json
   - App will rebuild on restart

---

## 🔮 Future Architecture Plans

### Planned Enhancements

1. **Offline Mode**
   - Pre-download all AI research
   - Local embedding model for search
   - Sync when online

2. **Database Optimization**
   - SQLite for faster queries
   - Full-text search
   - Indexed lookups

3. **Advanced Caching**
   - Redis for distributed cache
   - CDN for document delivery
   - Smart pre-warming

4. **AI Enhancements**
   - Fine-tuned model on automotive data
   - RAG (Retrieval Augmented Generation)
   - Vector database for similar repairs

5. **Integration**
   - Parts supplier APIs
   - OBD-II scanner integration
   - Customer quote generation
   - Billing system integration

---

## 📚 Related Documentation

- **[README.md](../README.md)** - Project overview
- **[Web App Guide](WEB_APP_GUIDE.md)** - Web interface usage
- **[Service System Guide](service_system/README_SERVICE_DOCS.md)** - API documentation
- **[Workflow Guide](workflow/WORKFLOW.md)** - Data contribution workflow
- **[Agent Instructions](agents/CLAUDE.md)** - AI agent guidelines

---

**Last Updated: January 17, 2025**

*Built with modern architecture principles for maintainability, scalability, and cost-effectiveness.*
