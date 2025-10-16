# Service Documentation Generator System
**Version**: 1.0  
**Created**: January 2025  
**Purpose**: Generate professional, AI-researched service documentation for Swoop Service Auto

---

## System Overview

This system combines your **vehicles.json** (2,246 vehicles) and **services.json** (153 services) to generate detailed, researched repair documentation for any vehicle/service combination. Documents are cached to avoid token waste on regeneration.

### Key Features
- ✅ **AI-powered research** using web access for torque specs, procedures, diagrams
- ✅ **Professional HTML output** with Swoop Service Auto branding
- ✅ **Document caching** - never regenerate the same service twice
- ✅ **Mobile-optimized** - looks great on phones, tablets, computers
- ✅ **Cost-effective** - uses OpenRouter with cheap, quality models
- ✅ **Offline-capable** - cached docs available without internet

---

## AI Model Recommendation: **Perplexity Sonar Pro**

After analyzing your needs, I recommend **Perplexity Sonar Pro (via OpenRouter)** for this system:

### Why Perplexity Sonar Pro?
- **Built-in web search** - Native web access without needing `:online` hack
- **Citation tracking** - Automatically cites sources for verification
- **Cost-effective** - $3/million tokens (cheaper than GPT-4, Claude Opus)
- **Technical accuracy** - Trained specifically for factual research tasks
- **Fast responses** - Optimized for web-augmented generation

### Cost Comparison (per 1M tokens)
| Model | Input Cost | Output Cost | Web Access | Best For |
|-------|-----------|-------------|------------|----------|
| **Perplexity Sonar Pro** | $3 | $15 | ✅ Native | Research, citations |
| GPT-4o | $2.50 | $10 | ❌ Requires plugin | General purpose |
| Claude 3.5 Sonnet | $3 | $15 | ❌ Requires plugin | Code, analysis |
| Qwen2.5-72B | $0.35 | $0.80 | ❌ | Cheap, no research |
| DeepSeek V3 | $0.27 | $1.10 | ❌ | Very cheap, basic |

### Estimated Costs Per Document
- **Average document**: ~2,000 input + 3,000 output tokens
- **Cost per doc**: $0.006 input + $0.045 output = **~$0.05 per service guide**
- **1,000 documents**: ~$50
- **Your entire dataset** (2,246 vehicles × 153 services = 343,638 combos): Would use caching strategy

### Alternative: **GPT-4o with Bing/Tavily Plugin**
If you prefer ChatGPT ecosystem:
- Use **GPT-4o** ($2.50/$10 per 1M tokens)
- Add **Tavily Search API** (free tier: 1,000 searches/month)
- Slightly more complex setup, similar quality

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Request                              │
│  "Generate service doc for 2015 Ford F-150 brake job"       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Document Cache Check                            │
│  Check: service_docs/Ford_F-150_2015_Brake_Pads_Front.html  │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
    ✅ Exists               ❌ Missing
         │                       │
         ▼                       ▼
   Return cached      ┌──────────────────────────┐
   document           │  AI Research Pipeline     │
                      │  1. Query vehicles.json   │
                      │  2. Query services.json   │
                      │  3. Build research prompt │
                      │  4. Call Perplexity API   │
                      │  5. Parse & format        │
                      │  6. Generate HTML         │
                      │  7. Cache document        │
                      └─────────┬────────────────┘
                                │
                                ▼
                      Return new document
```

---

## Implementation Components

### 1. Document Cache Structure
```
service_docs/
├── cache_index.json                    # Fast lookup index
├── Ford/
│   ├── F-150/
│   │   ├── 2015_Brake_Pads_Front.html
│   │   ├── 2015_Oil_Change.html
│   │   ├── 2015_Brake_Pads_Front.json  # Source data
│   │   └── ...
│   └── Mustang/
│       └── 2020_Spark_Plugs.html
├── Chevrolet/
│   └── Silverado/
│       └── 2018_Alternator.html
└── ...
```

### 2. Core Scripts

#### `generate_service_doc.py` - Main Generator
- Accepts: year, make, model, service_name
- Checks cache first
- If missing, triggers AI research
- Returns: HTML document path

#### `research_service.py` - AI Research Engine
- Queries Perplexity Sonar Pro API
- Researches: procedures, torque specs, diagrams, common issues
- Parses citations and formats data
- Returns: structured JSON

#### `format_html.py` - HTML Template Engine
- Takes researched data
- Applies Swoop Service Auto branding
- Generates mobile-responsive HTML
- Includes print stylesheet

#### `cache_manager.py` - Cache Management
- Maintains cache_index.json
- Handles versioning (regenerate if data changes)
- Cleanup old/stale documents

---

## HTML Template Design

### Mobile-First, Professional Layout

**Features:**
- ✅ Swoop Service Auto header with logo placeholder
- ✅ Vehicle info card (year, make, model, engine, transmission)
- ✅ Service overview (labor time, cost estimate, difficulty)
- ✅ Step-by-step procedure with torque specs
- ✅ Parts list with checkboxes (print-friendly)
- ✅ Common issues & troubleshooting
- ✅ Safety warnings highlighted
- ✅ Source citations at bottom
- ✅ Watermark: "Generated by Swoop Service Auto AI"

### Color Scheme
- **Primary**: #1a73e8 (professional blue)
- **Accent**: #fbbc04 (warning yellow)
- **Success**: #34a853 (green for notes)
- **Danger**: #ea4335 (red for warnings)
- **Background**: #f8f9fa (light gray)

---

## API Integration: Perplexity Sonar Pro

### Setup Instructions

1. **Get API Key**
   ```bash
   # Sign up at https://www.perplexity.ai/settings/api
   # Free tier: $5 credit to start
   export PERPLEXITY_API_KEY="pplx-xxxxx"
   ```

2. **Install Dependencies**
   ```bash
   pip install openai requests jinja2
   # Perplexity uses OpenAI-compatible API
   ```

3. **Basic API Call**
   ```python
   from openai import OpenAI
   
   client = OpenAI(
       api_key="pplx-xxxxx",
       base_url="https://api.perplexity.ai"
   )
   
   response = client.chat.completions.create(
       model="sonar-pro",
       messages=[
           {"role": "system", "content": "You are an expert automotive technician."},
           {"role": "user", "content": "What are the torque specs for 2015 Ford F-150 5.0L V8 cylinder head bolts?"}
       ]
   )
   ```

### Research Prompt Template
```
You are an expert automotive technician creating a service guide for:

Vehicle: {year} {make} {model}
Engine: {engine}
Transmission: {transmission}
Service: {service_name}

Research and provide:
1. Complete step-by-step procedure
2. Required torque specifications
3. Special tools needed
4. Common issues and troubleshooting
5. Safety warnings
6. Estimated time breakdown

Format as structured JSON with citations.
```

---

## Usage Workflow

### Command-Line Interface
```bash
# Generate a service document
python generate_service_doc.py \
  --year 2015 \
  --make Ford \
  --model "F-150" \
  --service "Brake Pads Replacement (Front)"

# Output: service_docs/Ford/F-150/2015_Brake_Pads_Front.html
```

### Python API
```python
from service_doc_generator import ServiceDocGenerator

gen = ServiceDocGenerator(
    vehicles_db="vehicles.json",
    services_db="services.json",
    cache_dir="service_docs/"
)

# Generate document
doc_path = gen.generate(
    year=2015,
    make="Ford",
    model="F-150",
    service="Brake Pads Replacement (Front)"
)

print(f"Document ready: {doc_path}")
# If cached: returns instantly
# If new: takes ~10-30 seconds for AI research
```

### Web API (Flask)
```python
from flask import Flask, jsonify, send_file

app = Flask(__name__)
gen = ServiceDocGenerator(...)

@app.route('/api/service_doc')
def get_service_doc():
    year = request.args.get('year')
    make = request.args.get('make')
    model = request.args.get('model')
    service = request.args.get('service')
    
    doc_path = gen.generate(year, make, model, service)
    return send_file(doc_path, mimetype='text/html')
```

---

## Cost Optimization Strategies

### 1. Smart Caching
- **Cache everything** - Never regenerate identical requests
- **Version tracking** - Only regenerate if vehicles.json or services.json change
- **Pre-generate popular services** - Oil changes, brake jobs, etc.

### 2. Batch Generation
- Generate common services for high-volume vehicles (F-150, Silverado, Camry)
- Run overnight batch jobs for catalog building
- Prioritize by: make popularity × service frequency

### 3. Fallback to Cheaper Models
- Use **Perplexity Sonar Pro** for complex services (engine work, diagnostics)
- Use **GPT-4o-mini** ($0.15/$0.60 per 1M) for simple services (oil changes, filters)
- Decision logic based on service complexity in services.json

### 4. Progressive Enhancement
- Start with basic procedure + torque specs (cheap)
- Add diagrams/images only on user request (expensive)
- Offer "premium research" option for complex jobs

---

## Quality Assurance

### Document Validation Checklist
- [ ] Vehicle specs match vehicles.json exactly
- [ ] Service info matches services.json category
- [ ] All torque specs include unit (ft-lbs or Nm)
- [ ] Procedure steps are numbered and sequential
- [ ] Safety warnings are highlighted
- [ ] Citations include source URLs
- [ ] Mobile layout renders correctly
- [ ] Print version is readable
- [ ] Swoop Service Auto branding present

### AI Research Quality Checks
- [ ] Torque specs cross-referenced with 2+ sources
- [ ] Procedure validated against OEM patterns
- [ ] Special tools are legitimate (not hallucinated)
- [ ] Year/engine/model specificity confirmed
- [ ] Common issues align with known problems

---

## Deployment Options

### Option 1: Local CLI Tool (Simplest)
- Run on your laptop
- Generate docs as needed
- Store in Dropbox/Google Drive for access anywhere

### Option 2: Web Service (Scalable)
- Flask/FastAPI backend
- Host on cheap VPS ($5/month)
- Access via mobile browser
- Sync cache to cloud storage

### Option 3: Mobile App Integration (Professional)
- Embed Flask API in React Native/Flutter app
- Offline-first with cached docs
- Sync cache in background
- Full mobile experience

**Recommendation for MVP**: Start with Option 1 (local CLI), then upgrade to Option 2 once proven.

---

## Next Steps

1. **Implement core generator** (generate_service_doc.py)
2. **Create HTML template** (responsive, branded)
3. **Test with 10 popular services** (validate quality)
4. **Build cache index** (for fast lookups)
5. **Pre-generate top 100 combos** (F-150 oil change, etc.)
6. **Deploy web API** (optional, for mobile access)

---

## Estimated Timeline

- **Week 1**: Core generator + HTML template (5 hrs)
- **Week 2**: Perplexity API integration + testing (5 hrs)
- **Week 3**: Cache system + batch generation (3 hrs)
- **Week 4**: Web API + mobile optimization (5 hrs)

**Total**: ~18 hours of development

---

## Success Metrics

- **Cache hit rate**: >80% (most requests served instantly)
- **Generation time**: <30 seconds for new documents
- **Cost per document**: <$0.10 (target: $0.05)
- **Quality score**: >90% accuracy on torque specs/procedures
- **Mobile usability**: Load time <2 seconds on 3G

---

## Maintenance

- **Monthly**: Review AI-generated docs for quality
- **Quarterly**: Regenerate popular docs with updated research
- **Annually**: Full cache refresh for model year updates
- **As-needed**: Manual corrections for inaccuracies

---

## Support & Resources

- **Perplexity API Docs**: https://docs.perplexity.ai
- **OpenRouter Dashboard**: https://openrouter.ai (alternative provider)
- **Jinja2 Templates**: https://jinja.palletsprojects.com
- **Mobile CSS Framework**: Bootstrap 5 or Tailwind CSS

---

**Questions? Issues?**
Document problems in `service_docs/issues.md` for batch resolution.
