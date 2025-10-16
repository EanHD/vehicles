# 🚀 Quick Reference Card

**Swoop Service Auto - AI-Powered Service Documentation System**

---

## ⚡ Super Quick Start

```bash
# 1. Setup (one time)
cd /home/eanhd/projects/vehicles
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Configure
cp .env.example .env
# Edit .env and add your API keys

# 3. Test
python tools/ai_client.py test

# 4. Generate a document
python tools/service_doc_generator.py \
  --year 2020 --make Ford --model "F-150" --service "Oil Change"
```

---

## 📝 Common Commands

### Generate Service Documentation
```bash
source venv/bin/activate
python tools/service_doc_generator.py \
  --year YYYY --make MAKE --model "MODEL" --service "SERVICE"

# Force regenerate (ignore cache)
python tools/service_doc_generator.py ... --force
```

### Find Torque Specifications
```bash
source venv/bin/activate
python research_tools/torque_spec_finder.py \
  YYYY MAKE "MODEL" "COMPONENT"

# Save to JSON
python research_tools/torque_spec_finder.py ... --save
```

### Get Wiring Help
```bash
source venv/bin/activate
python research_tools/wiring_diagram_helper.py \
  YYYY MAKE "MODEL" "SYSTEM" ["ISSUE"]

# Save to JSON
python research_tools/wiring_diagram_helper.py ... --save
```

### Batch Generate (Popular Vehicles)
```bash
source venv/bin/activate
python tools/batch_generate.py --max 50 --delay 2
```

### Check Configuration
```bash
source venv/bin/activate
python tools/ai_client.py        # Show config
python tools/ai_client.py test   # Test connections
```

---

## 🔧 Configuration (.env)

### Minimum Required
```bash
# Add at least one API key
PERPLEXITY_API_KEY=pplx-...
# OR
OPENAI_API_KEY=sk-...
# OR
ANTHROPIC_API_KEY=sk-ant-...
```

### Recommended Setup
```bash
# Research AI (web access)
PERPLEXITY_API_KEY=pplx-...
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro

# Formatter AI (cost-effective)
OPENAI_API_KEY=sk-...
FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
```

---

## 💰 Cost Guide

| Configuration | Per Doc | Per 100 Docs |
|---------------|---------|--------------|
| **Budget** | $0.03 | $3 |
| **Balanced** (recommended) | $0.05 | $5 |
| **Premium** | $0.10 | $10 |

**Tip**: Documents are cached automatically - subsequent lookups are FREE!

---

## 📂 File Locations

```
/home/eanhd/projects/vehicles/
├── .env                    # Your API configuration
├── venv/                   # Python virtual environment
├── data/
│   ├── vehicles.json       # 2,270+ vehicles
│   └── services.json       # Service catalog
├── service_docs/           # Generated HTML documents (cached)
├── tools/
│   ├── ai_client.py        # Unified AI client
│   └── service_doc_generator.py
└── research_tools/
    ├── torque_spec_finder.py
    └── wiring_diagram_helper.py
```

---

## 🆘 Troubleshooting

### "API key not found"
```bash
# Check configuration
python tools/ai_client.py

# Add key to .env
echo "PERPLEXITY_API_KEY=your-key" >> .env
```

### "Module not found"
```bash
# Make sure venv is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### "Could not parse JSON"
```bash
# Try different model
# Edit .env:
RESEARCH_AI_MODEL=sonar-pro  # Use better model
RESEARCH_MAX_TOKENS=6000     # Increase token limit
```

### High costs
```bash
# Use cheaper models
RESEARCH_AI_MODEL=sonar              # Instead of sonar-pro
FORMATTER_AI_MODEL=gpt-4o-mini       # Instead of gpt-4o

# Check cache
ls -lh service_docs/  # Cached docs are FREE!
```

---

## 🎯 API Keys Setup

### Perplexity (Best for Research)
1. Go to https://www.perplexity.ai/
2. Sign up → Settings → API
3. Generate key
4. Add to .env: `PERPLEXITY_API_KEY=pplx-...`

### OpenAI (Good for Formatting)
1. Go to https://platform.openai.com/
2. Sign up → API Keys
3. Create key
4. Add to .env: `OPENAI_API_KEY=sk-...`

### Anthropic (Premium Quality)
1. Go to https://www.anthropic.com/
2. Sign up for API access
3. Generate key
4. Add to .env: `ANTHROPIC_API_KEY=sk-ant-...`

---

## 📚 Documentation

- **[README.md](README.md)** - Main overview
- **[AI_CONFIGURATION_GUIDE.md](docs/AI_CONFIGURATION_GUIDE.md)** - Complete setup guide
- **[MIGRATION_TO_UNIFIED_AI.md](docs/MIGRATION_TO_UNIFIED_AI.md)** - Migration from old system
- **[STANDARDIZATION_COMPLETE.md](STANDARDIZATION_COMPLETE.md)** - What changed
- **`.env.example`** - Configuration template

---

## 🔑 Key Features

✅ **2,270+ vehicles** (1910s-2025)  
✅ **48 manufacturers**  
✅ **AI-powered research** with web access  
✅ **Automatic caching** (saves money)  
✅ **Professional HTML output**  
✅ **Torque specs & procedures**  
✅ **Mobile-friendly**  
✅ **Cost-effective** (~$0.05/doc)

---

## 🎨 Example Outputs

### Service Documentation
- Step-by-step procedures
- Torque specifications
- Parts lists with OEM numbers
- Safety warnings
- Common issues & tips
- Professional HTML format

### Torque Specs
- Component-specific values
- Imperial & metric units
- Tightening sequences
- Special requirements
- Common problems

### Wiring Diagrams
- Wire colors & routing
- Connector locations
- Voltage tests
- Diagnostic procedures
- Fuse/relay information

---

## ⚙️ Advanced Tips

### Pre-generate Popular Combinations
```bash
# Build cache for instant lookups
python tools/batch_generate.py --max 100
```

### Force Regenerate
```bash
# Update existing cached document
python tools/service_doc_generator.py ... --force
```

### Change Models On-the-Fly
```bash
# Edit .env to try different models
RESEARCH_AI_MODEL=claude-3-5-sonnet-20241022  # Try Claude
python tools/ai_client.py test                 # Verify
```

### Export to Different Formats
```bash
# HTML output is in service_docs/
# Can be:
# - Viewed in browser
# - Printed to PDF
# - Embedded in apps
# - Served via API
```

---

## 🚀 Performance

- **Generation time**: 5-15 seconds (first time)
- **Cache lookup**: Instant (< 1 second)
- **Cost per doc**: $0.03-0.10
- **Quality**: Professional-grade
- **Web access**: Yes (Perplexity)

---

## 📞 Support Checklist

If something isn't working:

1. [ ] Check you're in correct directory: `/home/eanhd/projects/vehicles`
2. [ ] Activate venv: `source venv/bin/activate`
3. [ ] Check configuration: `python tools/ai_client.py`
4. [ ] Test connections: `python tools/ai_client.py test`
5. [ ] Verify API keys on provider dashboards
6. [ ] Check `.env` file has correct keys
7. [ ] Read [AI_CONFIGURATION_GUIDE.md](docs/AI_CONFIGURATION_GUIDE.md)

---

## 🎯 One-Liner Cheat Sheet

```bash
# Complete workflow
cd /home/eanhd/projects/vehicles && \
source venv/bin/activate && \
python tools/service_doc_generator.py \
  --year 2020 --make Ford --model "F-150" --service "Oil Change"
```

---

**Happy Documenting! 🚗🔧**

*Need more details? See [AI_CONFIGURATION_GUIDE.md](docs/AI_CONFIGURATION_GUIDE.md)*
