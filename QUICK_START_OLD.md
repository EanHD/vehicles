# Quick Start Guide - Service Documentation Generator

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements_service_docs.txt
```

### Step 2: Get API Key

**Option A: Perplexity (Recommended)**
1. Go to https://www.perplexity.ai/settings/api
2. Sign up (free $5 credit)
3. Create API key
4. Set environment variable:
   ```bash
   export PERPLEXITY_API_KEY="pplx-xxxxxxxxxxxxxxxx"
   ```

**Option B: OpenAI (Alternative)**
1. Go to https://platform.openai.com/api-keys
2. Create API key
3. Set environment variable:
   ```bash
   export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
   ```

### Step 3: Generate Your First Document

```bash
python service_doc_generator.py \
  --year 2015 \
  --make Ford \
  --model "F-150" \
  --service "Brake Pads Replacement (Front)"
```

**Output**: `service_docs/Ford/F-150/2015_Brake_Pads_Replacement_Front.html`

Open the HTML file in your browser to see the professional service guide!

---

## 📋 Usage Examples

### Example 1: Single Document
```bash
python service_doc_generator.py \
  --year 2020 \
  --make Toyota \
  --model "Camry" \
  --service "Oil Change"
```

### Example 2: Python Script
```python
from service_doc_generator import ServiceDocGenerator

gen = ServiceDocGenerator()

doc_path, from_cache = gen.generate(
    year=2020,
    make="Toyota",
    model="Camry",
    service="Oil Change"
)

print(f"Document ready: {doc_path}")
```

### Example 3: Batch Generate Popular Services
```bash
# Generate 50 documents for popular vehicles
python batch_generate.py --max 50 --delay 2.0
```

---

## 💰 Cost Estimation

**Using Perplexity Sonar Pro**:
- **Per document**: ~$0.05 (average)
- **50 documents**: ~$2.50
- **100 documents**: ~$5.00

**Free tier**: $5 credit = ~100 documents

**What you get per document**:
✅ Complete step-by-step procedure  
✅ Torque specifications  
✅ Parts list with OEM numbers  
✅ Special tools required  
✅ Common issues & troubleshooting  
✅ Safety warnings  
✅ Pro tips from research  
✅ Source citations  

---

## 🎯 Smart Caching

The system **automatically caches** every document generated. Second request = instant delivery!

**Example**:
```bash
# First time: Generates via AI (~20 seconds, $0.05)
python service_doc_generator.py --year 2015 --make Ford --model "F-150" --service "Oil Change"

# Second time: Instant from cache (~0.1 seconds, $0.00)
python service_doc_generator.py --year 2015 --make Ford --model "F-150" --service "Oil Change"
```

**Cache location**: `service_docs/cache_index.json`

---

## 🔍 Check What's Available

### List Your Vehicles
```bash
# How many vehicles in database?
jq 'length' vehicles.json

# List all Ford F-150 entries
jq '.[] | select(.make == "Ford" and (.model | contains("F-150")))' vehicles.json
```

### List Your Services
```bash
# How many services available?
jq 'length' services.json

# List all brake services
jq '.[] | select(.category == "Brakes") | .name' services.json
```

---

## 📱 Mobile-Friendly Output

Every generated HTML document is:
✅ Mobile-responsive (looks great on phones)  
✅ Print-optimized (for paper checklists)  
✅ Offline-capable (once cached, works without internet)  
✅ Swoop Service Auto branded  

**Test on mobile**: Open any generated HTML in your phone's browser!

---

## 🛠️ Advanced Features

### Force Regeneration
If you want fresh research (maybe vehicle specs changed):
```bash
python service_doc_generator.py \
  --year 2015 \
  --make Ford \
  --model "F-150" \
  --service "Oil Change" \
  --force
```

### View Cache Statistics
```python
from service_doc_generator import ServiceDocGenerator

gen = ServiceDocGenerator()
print(f"Total cached documents: {len(gen.cache_index)}")

# List all cached docs
for key, doc in gen.cache_index.items():
    print(f"{doc['year']} {doc['make']} {doc['model']} - {doc['service']}")
```

### Batch Pre-Generate
Build your cache overnight for instant service:
```bash
# Generate top 200 popular combos
python batch_generate.py --max 200 --delay 1.5

# Cost: ~$10 (200 docs × $0.05)
# Time: ~90 minutes (with 1.5s delay)
```

---

## 🚨 Troubleshooting

### "API key not found"
```bash
# Make sure you set the environment variable
export PERPLEXITY_API_KEY="pplx-xxxxx"

# Or add to your ~/.bashrc or ~/.zshrc
echo 'export PERPLEXITY_API_KEY="pplx-xxxxx"' >> ~/.bashrc
source ~/.bashrc
```

### "Vehicle not found"
Make sure the vehicle exists in `vehicles.json`:
```bash
# Search for your vehicle
grep -i "f-150" vehicles.json | grep -i "ford"
```

If not found, check `CHECKLIST.md` to see if the manufacturer is complete.

### "Service not found"
Check `services.json` for exact service name:
```bash
jq '.[].name' services.json | grep -i "brake"
```

Service names must match **exactly** (case-sensitive).

---

## 📊 Dataset Coverage

You currently have:
- **2,246 vehicles** across 50 manufacturers
- **153 services** covering all major categories

**Potential service documents**: 2,246 × 153 = **343,638 combinations**

**Strategy**: Cache on-demand (generate as needed) or pre-generate popular combos.

---

## 🎨 Customization

### Modify HTML Template
Edit the `_generate_html()` method in `service_doc_generator.py`:
- Change colors (search for `#1a73e8`, etc.)
- Add your logo (replace "🔧 Swoop Service Auto")
- Adjust layout (modify CSS grid/flexbox)

### Add Custom Sections
Add new research questions in `_build_research_prompt()`:
- Fluid capacities
- Filter part numbers
- Wiring diagrams (links)
- Recall information

---

## 💡 Pro Tips

1. **Pre-generate during downtime**: Run batch generator overnight to build cache
2. **Focus on your fleet**: If you service mostly trucks, pre-generate truck services first
3. **Update annually**: Regenerate popular docs each year for updated info
4. **Print-friendly**: Print PDFs from HTML for job site reference (File → Print → Save as PDF)
5. **Share with team**: Put generated docs in Dropbox/Drive for team access

---

## 🚀 Next Steps

**Starter workflow**:
1. Generate 20-50 docs for your most common jobs
2. Use them in the field for 1-2 weeks
3. Note quality issues (missing specs, wrong procedures)
4. Adjust prompts and regenerate with `--force`
5. Scale up to 100-200 cached docs

**Cost estimate for starter**: $2.50-$10 (50-200 docs)

---

## 📞 Need Help?

Check these files:
- **Full documentation**: `SERVICE_DOC_GENERATOR.md`
- **Example code**: `example_usage.py`
- **Batch generation**: `batch_generate.py`

**Common issues**:
- API rate limits: Increase `--delay` in batch_generate.py
- Inaccurate specs: Try OpenAI GPT-4o as alternative (`--api-provider openai`)
- Missing vehicles: Check `CHECKLIST_STATUS.md` for completion status
