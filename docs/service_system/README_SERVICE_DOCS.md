# 🚀 Service Documentation Generation System

**Complete, production-ready AI-powered service documentation for Swoop Service Auto**

---

## 📦 What This Is

A comprehensive system that combines your **vehicles.json** (2,246 vehicles) with **services.json** (153 services) to generate professional, AI-researched repair documentation on-demand.

### Key Features

✅ **AI-Powered Research** - Uses Perplexity Sonar Pro to research torque specs, procedures, common issues  
✅ **Smart Caching** - Generates once, retrieves instantly forever  
✅ **Mobile-Optimized** - Beautiful HTML that works on phones, tablets, computers  
✅ **Cost-Effective** - ~$0.05 per document, 90% cheaper than AllData  
✅ **Professional Branding** - Swoop Service Auto watermarked documents  
✅ **Offline-Capable** - Cached docs work without internet  

---

## 📁 Files Included

### Core System
- **`service_doc_generator.py`** - Main generator engine (640 lines)
- **`service_api.py`** - Flask web API for mobile access (270 lines)
- **`example_usage.py`** - Usage examples (40 lines)
- **`batch_generate.py`** - Batch pre-caching tool (180 lines)

### Documentation
- **`SERVICE_DOC_GENERATOR.md`** - Complete technical documentation
- **`QUICK_START.md`** - 5-minute quick start guide
- **`SYSTEM_SUMMARY.md`** - Comprehensive system overview
- **`DEMO_WALKTHROUGH.md`** - Step-by-step demo with examples
- **`README_SERVICE_DOCS.md`** - This file

### Dependencies
- **`requirements_service_docs.txt`** - Python package requirements

---

## ⚡ Quick Start (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements_service_docs.txt
```

### 2. Get API Key
Sign up at https://www.perplexity.ai/settings/api (free $5 credit)

```bash
export PERPLEXITY_API_KEY="pplx-xxxxxxxxxxxxxxxx"
```

### 3. Generate First Document
```bash
python service_doc_generator.py \
  --year 2015 \
  --make Ford \
  --model "F-150" \
  --service "Brake Pads Replacement (Front)"
```

**Output**: Professional HTML document in `service_docs/`

---

## 💡 Usage Examples

### Command Line
```bash
# Generate single document
python service_doc_generator.py \
  --year 2020 \
  --make Toyota \
  --model "Camry" \
  --service "Oil Change"

# Force regenerate (get fresh research)
python service_doc_generator.py \
  --year 2020 \
  --make Toyota \
  --model "Camry" \
  --service "Oil Change" \
  --force
```

### Python Script
```python
from service_doc_generator import ServiceDocGenerator

gen = ServiceDocGenerator()

# Generate document
doc_path, from_cache = gen.generate(
    year=2020,
    make="Toyota", 
    model="Camry",
    service="Oil Change"
)

print(f"Ready: {doc_path} (cached: {from_cache})")
```

### Web API
```bash
# Start server
python service_api.py --port 5000

# Access from mobile browser
http://your-ip:5000/api/service_doc?year=2020&make=Toyota&model=Camry&service=Oil%20Change
```

---

## 📄 Document Contents

Every generated service guide includes:

1. **Vehicle Information** - Year, make, model, engines, transmissions, difficulty
2. **Service Overview** - Category, labor time, cost estimates
3. **Safety Warnings** - Critical safety information (highlighted)
4. **Step-by-Step Procedure** - Numbered steps with time estimates
5. **Torque Specifications** - All critical fasteners with values
6. **Parts List** - Required parts with OEM numbers (checkboxes for job site)
7. **Special Tools** - Specific tools needed
8. **Common Issues** - Known problems for this model/year
9. **Pro Tips** - Professional insights and shortcuts
10. **Source Citations** - Research sources for verification

---

## 💰 Cost Analysis

### Per Document
- **First generation**: ~$0.05 (one-time)
- **Every retrieval after**: $0.00 (cached forever)

### Realistic Scenarios

| Scenario | Documents | One-Time Cost | Annual Cost |
|----------|-----------|---------------|-------------|
| **Starter** (test phase) | 20-50 | $1-2.50 | $0 |
| **Small shop** (core cache) | 100-200 | $5-10 | $50-100 |
| **Mobile fleet** (extensive) | 500-1,000 | $25-50 | $100-200 |

**Compare to AllData**: $2,000+/year subscription

**Savings**: 90-95% cost reduction

---

## 🎨 Output Design

### Professional, Mobile-First Layout
- Clean, modern design
- Swoop Service Auto branding
- Color-coded sections (blue headers, yellow warnings, red dangers, green tips)
- Responsive grid layout
- Print-optimized (save as PDF)
- Touch-friendly (large buttons/checkboxes)

### Accessibility
- High contrast text
- Readable fonts (system fonts)
- Logical structure
- Keyboard navigation
- Screen reader compatible

---

## 🔧 Customization

### Change Branding
Edit `service_doc_generator.py`, modify `_generate_html()` method:
- Company name
- Logo
- Color scheme
- Header/footer text

### Add Research Topics
Edit `_build_research_prompt()` to request additional information:
- Fluid capacities
- Wiring diagram links
- Recall information
- Maintenance intervals

### Modify Layout
CSS is inline in the HTML template - easy to customize:
- Grid layout
- Color palette
- Font sizes
- Section order

---

## 🚀 Deployment Options

### Option 1: Local CLI (Simplest)
- Run on laptop
- Generate as needed
- Store in Dropbox/Drive for team access

### Option 2: Web API (Scalable)
- Flask server on cheap VPS ($5/month)
- Access from mobile browser
- Team-wide access
- Cloud backup of cache

### Option 3: Mobile App (Professional)
- React Native/Flutter app
- Embed WebView for documents
- Offline-first with background sync
- Full mobile experience

---

## 📊 Data Coverage

### Current Dataset
- **Vehicles**: 2,246 entries (50 manufacturers, 1903-2025)
- **Services**: 153 entries (all major categories)
- **Potential combinations**: 343,638 unique service docs

### Manufacturers Included
All major North American brands:
- Domestic: Ford, Chevrolet, GMC, Ram, Dodge, Chrysler, Jeep
- Japanese: Toyota, Honda, Nissan, Mazda, Subaru, Mitsubishi
- Korean: Hyundai, Kia, Genesis
- European: Volkswagen, BMW, Mercedes-Benz, Audi, Volvo
- Luxury: Lexus, Acura, Infiniti, Porsche, Jaguar, Land Rover
- Historic: Saturn, Pontiac, Oldsmobile, Mercury, Plymouth, Saab

### Service Categories
- Brakes
- Engine
- Electrical
- Cooling System
- Fuel System
- Exhaust
- Suspension
- Steering
- Transmission
- Drivetrain
- Fluid Maintenance
- Filters
- Belts & Hoses
- Lighting
- HVAC
- Body & Trim
- Diagnostic

---

## 🎯 Recommended Workflow

### Week 1: Test & Validate
1. Generate 10-20 docs for known jobs
2. Verify accuracy against your knowledge
3. Use in field on actual jobs
4. **Cost**: $0.50-$1.00

### Week 2: Build Core Cache
1. Identify 5 most common vehicles
2. Generate 10 most common services each
3. 50 documents covering majority of jobs
4. **Cost**: $2.50

### Week 3: Expand Coverage
1. Pre-generate popular combinations
2. Target 100-200 documents
3. Batch generate overnight
4. **Cost**: $5-10

### Ongoing: On-Demand Generation
1. Generate new combos as needed
2. Cache grows organically
3. Monthly updates for new vehicles
4. **Cost**: $5-10/month

---

## 📱 Mobile Access

### Via Web API
```bash
# Start server
python service_api.py --port 5000

# Find your IP
ifconfig | grep "inet "

# Access from phone
http://192.168.1.100:5000/api/service_doc?year=2020&make=Toyota&model=Camry&service=Oil%20Change
```

### API Endpoints
- **`/api/service_doc`** - Generate/retrieve document (HTML or JSON)
- **`/api/vehicles`** - Search vehicles
- **`/api/services`** - List services
- **`/api/cache/stats`** - Cache statistics
- **`/api/popular`** - Popular combinations for pre-caching

---

## 🔍 Quality Assurance

### What AI Does Well
✅ Comprehensive procedures  
✅ General torque specifications  
✅ Common issues research  
✅ Parts identification  
✅ Safety warnings  
✅ Time estimates  

### What Requires Verification
⚠️ Model-specific torque specs (verify with manual)  
⚠️ OEM part numbers (may vary by trim)  
⚠️ Wiring diagrams (AI provides links, not diagrams)  
⚠️ TSBs (subscription-only data)  

### Best Practices
1. **Verify critical specs** - Always double-check torque values
2. **Cross-reference** - Compare with known-good sources
3. **Use as guide** - Not a replacement for OEM manual
4. **Update when wrong** - Regenerate with `--force` if inaccurate

---

## 🚨 Troubleshooting

### Common Issues

**"API key not found"**
```bash
export PERPLEXITY_API_KEY="pplx-xxxxx"
echo $PERPLEXITY_API_KEY  # Verify it's set
```

**"Vehicle not found"**
```bash
# Search your database
jq '.[] | select(.make == "Ford" and (.model | contains("F-150")))' vehicles.json
```

**"Service not found"**
```bash
# List available services
jq -r '.[].name' services.json | grep -i brake
```

**"Rate limit exceeded"**
```bash
# Increase delay in batch generation
python batch_generate.py --max 50 --delay 3.0
```

---

## 📈 Success Metrics

Track these to measure system effectiveness:

- **Cache hit rate**: Target >80% (requests served from cache)
- **Cost per job**: Target <$0.10 (including regenerations)
- **Time saved**: Minutes not spent searching
- **Quality score**: Accuracy of specs/procedures (spot-check)
- **Coverage**: % of jobs with cached docs (target >90%)

---

## 🔮 Future Enhancements

### Short Term (Easy)
- [ ] Vehicle images from Wikipedia
- [ ] Fluid capacity charts
- [ ] Recall check integration
- [ ] PDF export option

### Medium Term (Moderate)
- [ ] Wiring diagram search
- [ ] TSB lookup (if API available)
- [ ] Parts price comparison
- [ ] Video tutorial links

### Long Term (Complex)
- [ ] Native mobile app
- [ ] Diagnostic code database
- [ ] Maintenance schedule generator
- [ ] Customer-facing quotes

---

## 📚 Documentation Index

**Getting Started**:
- `QUICK_START.md` - 5-minute setup guide
- `DEMO_WALKTHROUGH.md` - Complete step-by-step demo

**Technical Details**:
- `SERVICE_DOC_GENERATOR.md` - Full system documentation
- `SYSTEM_SUMMARY.md` - Comprehensive overview

**Code**:
- `service_doc_generator.py` - Core generator (read docstrings)
- `service_api.py` - Web API (read docstrings)
- `example_usage.py` - Working examples
- `batch_generate.py` - Batch tool

---

## 💎 Pro Tips

1. **Batch generate overnight** - Build cache while you sleep
2. **Focus on your fleet** - Pre-generate for vehicles you actually service
3. **Print to PDF** - Create offline references (File → Print → Save as PDF)
4. **Version control** - Backup cache before major updates
5. **Spot-check quality** - Verify critical specs against known sources

---

## 🎉 You're Ready!

You now have a **complete, production-ready** system for generating professional service documentation!

### What You Can Do Right Now

1. **Generate 5 documents** for tomorrow's jobs (~$0.25, 3 minutes)
2. **Start web API** for mobile access (instant setup)
3. **Batch generate** popular services overnight (~$5, 100 docs)
4. **Customize branding** to match your company
5. **Share with team** via Dropbox/Drive/VPS

### ROI Summary

**Investment**: $10-50 (initial cache)  
**Ongoing**: $5-10/month  
**Savings vs AllData**: $2,000/year  
**Break-even**: First month  

---

## 📞 Support

**Documentation**: Read the included `.md` files  
**Issues**: Check troubleshooting sections  
**Customization**: Edit Python files (well-commented)  

**You have everything you need to deploy this system in production!** 🚀

---

**Built for**: Swoop Service Auto  
**Purpose**: Professional mobile mechanic documentation  
**Status**: Production-ready  
**License**: Your proprietary system  

**Last Updated**: January 2025
