# 🎬 Demo Walkthrough - Service Documentation System

This is a **complete walkthrough** showing you exactly how to use your new service documentation system.

---

## ⚡ Quick Demo (5 Minutes)

### Step 1: Install Dependencies

```bash
pip install requests openai flask flask-cors
```

**What this installs**:
- `requests` - HTTP library for API calls
- `openai` - SDK for Perplexity/OpenAI APIs  
- `flask` - Web server (if you want the API)
- `flask-cors` - Cross-origin support (for mobile)

### Step 2: Get Your API Key

**Option A: Perplexity (Recommended)**

1. Go to: https://www.perplexity.ai/settings/api
2. Sign up (free account gets $5 credit = ~100 documents)
3. Click "Generate API Key"
4. Copy the key (starts with `pplx-`)

**Option B: OpenAI (Alternative)**

1. Go to: https://platform.openai.com/api-keys
2. Create account
3. Add payment method ($5 minimum)
4. Create API key (starts with `sk-`)

### Step 3: Set API Key

**Mac/Linux**:
```bash
export PERPLEXITY_API_KEY="pplx-xxxxxxxxxxxxxxxxxxxxxxxx"

# Make it permanent:
echo 'export PERPLEXITY_API_KEY="pplx-xxxxx"' >> ~/.bashrc
source ~/.bashrc
```

**Windows**:
```cmd
set PERPLEXITY_API_KEY=pplx-xxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 4: Generate Your First Document

```bash
python service_doc_generator.py \
  --year 2015 \
  --make Ford \
  --model "F-150" \
  --service "Brake Pads Replacement (Front)"
```

**Expected output**:
```
⚡ Generating new document for 2015 Ford F-150 - Brake Pads Replacement (Front)
🔍 Researching with Perplexity Sonar Pro...
✓ Document generated: service_docs/Ford/F-150/2015_Brake_Pads_Replacement_Front.html

✨ Document ready: service_docs/Ford/F-150/2015_Brake_Pads_Replacement_Front.html
(newly generated)
```

**Time**: 20-30 seconds  
**Cost**: ~$0.05

### Step 5: Open the Document

```bash
# Mac
open service_docs/Ford/F-150/2015_Brake_Pads_Replacement_Front.html

# Linux
xdg-open service_docs/Ford/F-150/2015_Brake_Pads_Replacement_Front.html

# Windows
start service_docs/Ford/F-150/2015_Brake_Pads_Replacement_Front.html
```

**You should see**:
- ✅ Professional layout with Swoop Service Auto branding
- ✅ Vehicle information (year, make, model, engines, etc.)
- ✅ Service overview (cost, time, category)
- ✅ Safety warnings (highlighted in red)
- ✅ Step-by-step procedure (numbered, with time estimates)
- ✅ Torque specifications (all critical bolts)
- ✅ Parts list (with checkboxes)
- ✅ Special tools required
- ✅ Common issues specific to this model
- ✅ Pro tips
- ✅ Source citations

### Step 6: Generate Another Document (Tests Cache)

```bash
# Same request again
python service_doc_generator.py \
  --year 2015 \
  --make Ford \
  --model "F-150" \
  --service "Brake Pads Replacement (Front)"
```

**Expected output**:
```
✓ Using cached document: service_docs/Ford/F-150/2015_Brake_Pads_Replacement_Front.html

📋 Document ready: service_docs/Ford/F-150/2015_Brake_Pads_Replacement_Front.html
(from cache)
```

**Time**: <1 second  
**Cost**: $0.00

🎉 **Cache works!** Second request is instant and free.

---

## 🔍 Exploring Your Data

### Find Available Vehicles

```bash
# How many total vehicles?
jq 'length' vehicles.json
# Output: 2246

# List all Ford F-150 entries
jq '.[] | select(.make == "Ford" and (.model | contains("F-150")))' vehicles.json

# Count vehicles by make
jq -r '.[].make' vehicles.json | sort | uniq -c | sort -rn | head -10

# Find specific vehicle
jq '.[] | select(.make == "Toyota" and (.model | contains("Camry")) and (.years[] == 2020))' vehicles.json
```

### Find Available Services

```bash
# How many services?
jq 'length' services.json
# Output: 153

# List all service names
jq -r '.[].name' services.json

# List services by category
jq -r '.[] | select(.category == "Brakes") | .name' services.json

# Find mobile-capable services
jq -r '.[] | select(.mobile == true) | .name' services.json

# Get service categories
jq -r '.[].category' services.json | sort | uniq
```

---

## 📝 Real-World Examples

### Example 1: Oil Change for Toyota Camry

```bash
python service_doc_generator.py \
  --year 2020 \
  --make Toyota \
  --model "Camry" \
  --service "Oil Change"
```

**What you'll get**:
- Oil capacity for 2020 Camry engines
- Oil filter part numbers
- Drain plug torque spec
- Filter torque spec
- Oil grade recommendations
- Reset procedure for maintenance light
- Common issues (oil consumption, leaks)

### Example 2: Brake Job for Chevrolet Silverado

```bash
python service_doc_generator.py \
  --year 2019 \
  --make Chevrolet \
  --model "Silverado 1500" \
  --service "Brake Pads Replacement (Front)"
```

**What you'll get**:
- Caliper bolt torque specs
- Caliper bracket torque specs
- Pad type (semi-metallic vs ceramic)
- Rotor thickness specs
- Brake bleeding procedure
- Common issues (premature wear, noise)

### Example 3: Spark Plugs for Honda Civic

```bash
python service_doc_generator.py \
  --year 2020 \
  --make Honda \
  --model "Civic" \
  --service "Spark Plugs Replacement"
```

**What you'll get**:
- Spark plug gap specification
- Plug torque spec (critical!)
- Ignition coil removal procedure
- Plug part numbers (NGK/Denso)
- Replacement interval
- Common issues (misfires, coil failure)

---

## 🚀 Batch Generation (Build Your Cache)

### Pre-Generate Popular Services

Edit `batch_generate.py` to match YOUR most common jobs:

```python
POPULAR_VEHICLES = [
    # Your fleet (customize this!)
    (2020, "Ford", "F-150"),
    (2019, "Ford", "F-150"),
    (2018, "Chevrolet", "Silverado 1500"),
    (2020, "Toyota", "Camry"),
    (2019, "Honda", "Civic"),
    # Add your common vehicles here
]

POPULAR_SERVICES = [
    # Your common services (customize this!)
    "Oil Change",
    "Brake Pads Replacement (Front)",
    "Brake Pads Replacement (Rear)",
    "Air Filter Replacement",
    "Battery Replacement",
    # Add your common services here
]
```

### Run Batch Generation

```bash
# Generate 50 documents (will skip already cached)
python batch_generate.py --max 50 --delay 2.0

# Wait ~15-20 minutes
# Cost: ~$2.50 (for new docs only)
```

**Output**:
```
🚀 Starting batch generation
Vehicles: 5
Services: 5
Total combinations: 25
Max documents to generate: 50
------------------------------------------------------------
✨ [1/25] GENERATED: 2020 Ford F-150 - Oil Change
✨ [2/25] GENERATED: 2020 Ford F-150 - Brake Pads Replacement (Front)
✨ [3/25] GENERATED: 2020 Ford F-150 - Air Filter Replacement
...
📋 [20/25] CACHED: 2019 Honda Civic - Oil Change
...
============================================================
📊 Batch Generation Summary
============================================================
Total processed: 25/25
✨ Newly generated: 22
📋 From cache: 3
❌ Errors: 0
⏱️  Time elapsed: 960.5 seconds
⚡ Average per doc: 43.7 seconds
💰 Estimated cost: $1.10 (at $0.05/doc)
============================================================
```

---

## 🌐 Web API (Mobile Access)

### Start the API Server

```bash
python service_api.py --port 5000
```

**Output**:
```
🚀 Starting Swoop Service Auto Documentation API
📡 Listening on http://0.0.0.0:5000
📋 Total vehicles: 2246
🔧 Total services: 153
💾 Cached documents: 25

✅ API ready for requests!
```

### Test API Endpoints

**1. Generate Document (HTML)**:
```bash
curl "http://localhost:5000/api/service_doc?year=2015&make=Ford&model=F-150&service=Oil%20Change" > test.html

open test.html
```

**2. Search Vehicles (JSON)**:
```bash
curl "http://localhost:5000/api/vehicles?make=Ford&model=F-150" | jq

# Output:
{
  "count": 8,
  "limit": 50,
  "results": [
    {
      "years": [2015, 2016, 2017, 2018, 2019, 2020],
      "make": "Ford",
      "model": "F-150 (thirteenth generation)",
      "engines": [...],
      "transmissions": [...],
      "difficulty": 1.2
    },
    ...
  ]
}
```

**3. List Services (JSON)**:
```bash
curl "http://localhost:5000/api/services?category=Brakes" | jq

# Output:
{
  "count": 12,
  "results": [
    {
      "name": "Brake Pads Replacement (Front)",
      "category": "Brakes",
      "labor_hours": 1.0,
      "labor_cost": [100, 160],
      "parts_cost": [50, 120],
      "mobile": true
    },
    ...
  ]
}
```

**4. Cache Stats**:
```bash
curl "http://localhost:5000/api/cache/stats" | jq

# Output:
{
  "total_documents": 25,
  "cache_directory": "service_docs",
  "by_make": {
    "Ford": 10,
    "Toyota": 7,
    "Chevrolet": 5,
    "Honda": 3
  },
  "by_service": {
    "Oil Change": 8,
    "Brake Pads Replacement (Front)": 6,
    "Air Filter Replacement": 5,
    ...
  }
}
```

### Access from Mobile

**Find your computer's IP**:
```bash
# Mac/Linux
ifconfig | grep "inet " | grep -v 127.0.0.1

# Output: inet 192.168.1.100 ...
```

**On your phone's browser**:
```
http://192.168.1.100:5000/api/service_doc?year=2015&make=Ford&model=F-150&service=Oil%20Change
```

The HTML document will render perfectly on your phone!

---

## 📱 Mobile App Integration Ideas

### React Native Example

```javascript
// ServiceDocViewer.js
import React, { useState } from 'react';
import { WebView } from 'react-native-webview';

const ServiceDocViewer = ({ year, make, model, service }) => {
  const apiUrl = 'http://your-server-ip:5000';
  const docUrl = `${apiUrl}/api/service_doc?year=${year}&make=${make}&model=${model}&service=${service}`;
  
  return (
    <WebView
      source={{ uri: docUrl }}
      style={{ flex: 1 }}
    />
  );
};
```

### Flutter Example

```dart
// service_doc_viewer.dart
import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class ServiceDocViewer extends StatelessWidget {
  final String year, make, model, service;
  
  String get docUrl => 
    'http://your-server-ip:5000/api/service_doc?year=$year&make=$make&model=$model&service=$service';
  
  @override
  Widget build(BuildContext context) {
    return WebView(
      initialUrl: docUrl,
      javascriptMode: JavascriptMode.unrestricted,
    );
  }
}
```

---

## 🎨 Customization Examples

### Change Branding

Edit `service_doc_generator.py`, find `_generate_html()` method:

```python
# Change header
html = f"""
<div class="header">
    <h1>🔧 Your Company Name</h1>
    <div class="subtitle">Professional Mobile Mechanic Service</div>
</div>
"""

# Change colors
"""
.header {{
    background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);  /* Your colors */
    color: white;
}}
"""
```

### Add Logo

```html
<div class="header">
    <img src="https://your-site.com/logo.png" alt="Logo" style="max-width: 200px;">
    <h1>Your Company Name</h1>
</div>
```

### Modify Research Prompt

Edit `_build_research_prompt()` to add more questions:

```python
prompt = f"""
...existing prompt...

Also research and provide:
9. FLUID CAPACITIES (oil, coolant, brake fluid, etc.)
10. MAINTENANCE INTERVALS (when to replace this)
11. RECALL INFORMATION (any recalls related to this service)
12. WIRING DIAGRAMS (links if available)
"""
```

---

## 💰 Cost Tracking

### Monitor API Usage

**Perplexity Dashboard**:
- https://www.perplexity.ai/settings/api
- Shows: Total tokens used, cost, remaining credit

**Track in Code**:
```python
# Add to service_doc_generator.py
def generate(self, ...):
    ...
    # After generation
    tokens_used = len(prompt) / 4 + len(result) / 4  # Rough estimate
    cost = (tokens_used / 1_000_000) * 15  # $15 per 1M output tokens
    print(f"💰 Estimated cost: ${cost:.4f}")
```

### Calculate ROI

**Your cost**: ~$0.05 per document  
**AllData subscription**: ~$2,000/year  
**Break-even**: 40,000 documents/year = 109 docs/day

**Realistic usage**:
- 5-10 unique jobs per day = 5-10 new docs
- Rest are cached (free)
- **Annual cost**: $100-200 vs $2,000 = **90% savings**

---

## 🔧 Troubleshooting

### Issue: "API key not found"

**Fix**:
```bash
# Check if set
echo $PERPLEXITY_API_KEY

# If empty, set it
export PERPLEXITY_API_KEY="pplx-xxxxx"

# Verify
python3 -c "import os; print(os.getenv('PERPLEXITY_API_KEY'))"
```

### Issue: "Vehicle not found: 2015 Ford F-150"

**Fix**:
```bash
# Search for the vehicle
jq '.[] | select(.make == "Ford" and (.model | contains("F-150")) and (.years[] == 2015))' vehicles.json

# If not found, check year range
jq '.[] | select(.make == "Ford" and (.model | contains("F-150")))' vehicles.json | jq -r '.years'

# Use correct year from the range
```

### Issue: "Service not found: Oil Change"

**Fix**:
```bash
# Check exact service name
jq -r '.[].name' services.json | grep -i oil

# Common services:
# - "Oil Change"  ✅
# - "Engine Oil Change"  ❌ (not in your DB)
# - "oil change"  ❌ (case-sensitive)
```

### Issue: "Rate limit exceeded"

**Fix**:
```bash
# Increase delay in batch generation
python batch_generate.py --max 50 --delay 3.0

# Or pause between manual generations
sleep 2
```

### Issue: "Document looks wrong/incomplete"

**Fix**:
```bash
# Regenerate with --force
python service_doc_generator.py \
  --year 2015 \
  --make Ford \
  --model "F-150" \
  --service "Oil Change" \
  --force

# AI research varies; try again for better results
```

---

## 📈 Recommended Workflow

### Week 1: Learning Phase
- Generate 10-20 docs for jobs you know well
- Compare AI research vs your knowledge
- Note accuracies and errors
- **Cost**: $0.50-$1.00

### Week 2: Building Phase
- Identify your 10 most common jobs
- Pre-generate for 5-10 common vehicles
- Build core cache (50-100 docs)
- **Cost**: $2.50-$5.00

### Week 3: Testing Phase
- Use docs in the field
- Get feedback from techs
- Note missing info
- Regenerate with improvements
- **Cost**: $1-2 (regenerations)

### Month 2+: Production Phase
- Generate on-demand as new jobs arrive
- Cache grows organically
- Monthly batch update for new vehicles
- **Cost**: $5-10/month

---

## 🎯 Success Metrics

Track these to measure success:

- **Cache hit rate**: % of requests served from cache (target: >80%)
- **Cost per job**: Total API cost / jobs completed (target: <$0.10)
- **Time saved**: Minutes not spent searching YouTube/forums
- **Quality**: Accuracy of torque specs/procedures (spot-check)
- **Coverage**: % of your jobs with cached docs (target: >90% of common jobs)

---

## 🚀 You're Ready!

Follow this walkthrough and you'll have:

✅ Professional service documentation  
✅ Smart caching for instant re-access  
✅ Mobile-friendly HTML  
✅ Cost-effective research  
✅ Swoop Service Auto branding  

**Start with**: Generate 5 documents for tomorrow's jobs!

```bash
# Your first 5 docs
python service_doc_generator.py --year 2020 --make Ford --model "F-150" --service "Oil Change"
python service_doc_generator.py --year 2019 --make Toyota --model "Camry" --service "Brake Pads Replacement (Front)"
python service_doc_generator.py --year 2018 --make Honda --model "Civic" --service "Air Filter Replacement"
python service_doc_generator.py --year 2021 --make Chevrolet --model "Silverado 1500" --service "Battery Replacement"
python service_doc_generator.py --year 2020 --make Ram --model "1500" --service "Spark Plugs Replacement"
```

**Cost**: ~$0.25 (5 docs × $0.05)  
**Time**: 2-3 minutes  
**Value**: Professional documentation for your next 5 jobs! 🎉

---

**Need help?** Re-read:
- `QUICK_START.md` - Fast setup
- `SYSTEM_SUMMARY.md` - Complete overview
- `SERVICE_DOC_GENERATOR.md` - Full technical docs
