# 🚗 Swoop Service Auto - Professional Service Documentation System

> **AI-powered automotive service documentation - Your ALLDATA alternative**

**Status**: ✅ **FULLY OPERATIONAL** - Web app running at http://localhost:8501

This system combines comprehensive vehicle data with AI research to generate professional-grade service documentation for automotive technicians. Think ALLDATA or ProDemand, but powered by AI and tailored for mobile mechanics.

---

## 🎯 What This System Does

**Select a vehicle → Pick a service → Get professional documentation**

The system:
1. **Knows 2,270+ vehicles** (1950-2025) with complete specifications
2. **Understands 780+ services** from oil changes to complex diagnostics
3. **Researches procedures** using AI with web access (Perplexity Sonar Pro)
4. **Generates beautiful HTML docs** with torque specs, diagrams, and step-by-step instructions
5. **Caches everything** for instant future access

### ✨ Key Features

✅ **Comprehensive Database**
- 2,270 vehicle entries covering 33+ major brands
- 780+ services with labor times and pricing
- Engines, transmissions, body styles, drivetrain options

✅ **AI-Powered Research**
- Uses Perplexity Sonar Pro with web access for accurate, current information
- OpenAI GPT-4o-mini for clean, professional formatting
- Finds torque specs, procedures, part numbers automatically
- Hybrid approach: quality + cost-effectiveness

✅ **Web Interface**
- Beautiful Streamlit web app
- Select vehicle by make/model/year
- Choose service by category
- Generate docs with one click

✅ **Professional Output**
- HTML documents styled for readability
- Mobile-friendly for shop floor use
- Swoop Service Auto branding
- Cached for instant retrieval

---

## 🚀 Quick Start

### 1. Start the Web App

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

Or use the convenience script:
```bash
./start_web_app.sh
```

### 2. Access the App

Open your browser to:
- **Local**: http://localhost:8501
- **Network**: http://172.31.17.60:8501
- **Tailscale**: http://73.151.108.165:8501

### 3. Generate Documentation

1. Select a vehicle (Make → Model → Year)
2. Choose a service from the catalog
3. Click "Generate Service Documentation"
4. Get professional docs in 10-30 seconds!

**See detailed walkthrough**: [`QUICK_START_APP.md`](QUICK_START_APP.md)

---

## 📊 Database Coverage

### Vehicles: 2,270 Entries

**American Brands** (1,200+ vehicles):
- Ford, Chevrolet, Dodge, RAM, GMC, Jeep, Chrysler
- Cadillac, Buick, Lincoln, Mercury, Plymouth, Pontiac, Oldsmobile

**Japanese Brands** (700+ vehicles):
- Toyota, Honda, Nissan, Mazda, Subaru, Mitsubishi
- Lexus, Acura, Infiniti

**Korean Brands** (200+ vehicles):
- Hyundai, Kia, Genesis

**European Luxury** (150+ vehicles):
- Mercedes-Benz, BMW, Audi, Volkswagen
- Volvo, Land Rover, Jaguar, Porsche

**Electric/Modern** (20+ vehicles):
- Tesla, Rivian, Lucid

**Time Period**: 1949-2025

### Services: 153 Categories

**Maintenance**: Oil changes, filters, fluid services, inspections  
**Brakes**: Pads, rotors, calipers, fluid, lines  
**Engine**: Spark plugs, belts, hoses, cooling, timing  
**Transmission**: Fluid service, filter, repairs  
**Suspension**: Shocks, struts, springs, bushings  
**Steering**: Tie rods, power steering, alignment  
**Electrical**: Battery, alternator, starter, diagnostics  
**Exhaust**: Catalytic converter, muffler, sensors  
**HVAC**: AC service, heater, blower  
**Wheels/Tires**: Rotation, balance, TPMS

---

## 🗂️ Project Structure

```
vehicles/
├── 📱 app.py                          # ⭐ Streamlit web interface (START HERE!)
├── 📁 data/                           # Core databases
│   ├── vehicles.json                  # 2,270 vehicles with specs
│   └── services.json                  # 153 services with labor/pricing
│
├── 📁 tools/                          # Python modules
│   ├── service_doc_generator.py       # Main doc generator
│   ├── ai_client.py                   # Multi-provider AI client
│   ├── service_api.py                 # REST API wrapper
│   └── batch_generate.py              # Batch generation tool
│
├── 📁 service_docs/                   # Generated documentation (cache)
│   └── [make]/[model]/[year]/        # Organized by vehicle
│       └── [service].html             # HTML documents
│
├── 📁 docs/                           # System documentation
│   ├── workflow/                      # Research workflow
│   ├── agents/                        # AI agent instructions
│   └── service_system/                # Service system docs
│
├── 📁 wip/                            # Research workspace
│   └── [manufacturer]/                # Per-brand work folders
│       ├── PROGRESS_TRACKER.md
│       └── [decade].json              # Decade research files
│
├── 📁 backups/                        # Timestamped backups
├── 📁 reports/                        # Completion reports
│
├── 📋 README.md                       # ⭐ This file
├── 📋 QUICK_START_APP.md              # ⭐ User guide
├── 📋 APP_STATUS.md                   # ⭐ Current status
├── 📋 IMPLEMENTATION_GUIDE.md         # Technical implementation
├── 📋 SYSTEM_COMPLETE.md              # Architecture overview
├── 📋 CHECKLIST.md                    # Manufacturer coverage checklist
└── .env                               # API keys (DO NOT COMMIT!)
```

---

## 💡 How It Works

### Architecture Overview

```
User Input (Web App)
    ↓
Vehicle Selection (Make/Model/Year)
    ↓
Service Selection (from 153 services)
    ↓
Check Cache (service_docs/)
    ↓
┌─────────────┐
│ Cache Hit?  │
└─────────────┘
      ↓ No
Research AI (Perplexity + Web Access)
    ↓
Gather: specs, procedures, torque values
    ↓
Formatter AI (OpenAI GPT-4)
    ↓
Generate: Beautiful HTML document
    ↓
Save to Cache
    ↓
Display to User (10-30 seconds)
```

### AI Strategy: Hybrid Approach

**Why Two AIs?**

1. **Research AI** (Perplexity Sonar)
   - Has real-time web access
   - Finds current, accurate information
   - Cost: ~$0.001-0.003 per document
   - Fast and accurate

2. **Formatter AI** (OpenAI GPT-4)
   - Creates consistent, professional output
   - Better formatting and structure
   - Cost: ~$0.005-0.015 per document
   - High quality results

**Total Cost**: ~$0.01-0.02 per NEW document  
**Cached Docs**: $0.00 (instant!)

### Environment Variables

Required in `.env`:
```bash
# Research AI (with web access - REQUIRED)
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro
PERPLEXITY_API_KEY=your_perplexity_key_here

# Formatter AI (REQUIRED)
FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
OPENAI_API_KEY=your_openai_key_here

# AI Parameters (optional - these are defaults)
RESEARCH_TEMPERATURE=0.2
RESEARCH_MAX_TOKENS=4000
FORMATTER_TEMPERATURE=0.3
FORMATTER_MAX_TOKENS=8000

# Diagram Generation (DISABLED by default)
# AI-generated diagrams are experimental and low quality
# Not recommended for production use
# DIAGRAM_AI_PROVIDER=
# TOGETHER_API_KEY=
```

Get API keys:
- Perplexity: https://www.perplexity.ai/settings/api
- OpenAI: https://platform.openai.com/api-keys

---

## 🎨 Usage Examples

### Web App Interface

Perfect for daily use:

1. **Quick Oil Change Lookup**
   - Vehicle: 2021 Toyota Camry
   - Service: Engine Oil and Filter Change
   - Result: Oil capacity, filter part#, torque specs

2. **Brake Job Planning**
   - Vehicle: 2018 Ford F-150
   - Service: Brake Pad Replacement (Front)
   - Result: Procedure, torque specs, special tools

3. **Complex Repair**
   - Vehicle: 2015 Honda Civic
   - Service: Timing Belt Replacement
   - Result: Full procedure, alignment marks, tensioner specs

### Command Line (Advanced)

```python
from tools.service_doc_generator import ServiceDocGenerator

gen = ServiceDocGenerator()

# Generate single document
doc_path, from_cache = gen.generate(
    year=2020,
    make="Ford",
    model="F-150",
    service="Engine Oil and Filter Change"
)

print(f"Document: {doc_path}")
print(f"From cache: {from_cache}")
```

### Batch Processing

```python
# Generate docs for common services on your fleet
vehicles = [
    ("2019", "Toyota", "Camry"),
    ("2020", "Honda", "Accord"),
    ("2021", "Ford", "F-150")
]

services = [
    "Engine Oil and Filter Change",
    "Brake Pads Replacement (Front)",
    "Tire Rotation"
]

for year, make, model in vehicles:
    for service in services:
        gen.generate(year, make, model, service)
```

---

## 🔄 Managing Cached Documents

### Regenerating Documents

To regenerate all cached documents (for example, after updating styling or AI prompts):

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
python3 regenerate_docs.py
```

This script will:
- Clear the existing cache
- Generate fresh versions of 6 common service documents
- Useful after updates to templates or AI prompts

You can also force regeneration of individual documents in the web app by checking the "Force Regenerate" option.

### Deleting Cached Documents

From the **📚 Browse Cache** page in the web app:
1. Select a document from the list
2. Click "🗑️ Delete Selected Document"  
3. Confirm deletion
4. The document will be removed from cache

The next time you request that service/vehicle combination, it will be freshly generated.

---

## 📖 Documentation

### Quick References
- **[QUICK_START_APP.md](QUICK_START_APP.md)** - Get started in 60 seconds ⭐
- **[APP_STATUS.md](APP_STATUS.md)** - Current system status
- **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - Technical details

### System Documentation
- **[SYSTEM_COMPLETE.md](SYSTEM_COMPLETE.md)** - Full architecture
- **[CHECKLIST.md](CHECKLIST.md)** - Manufacturer coverage
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues

### Developer Docs
- **[docs/agents/CLAUDE.md](docs/agents/CLAUDE.md)** - AI agent workflows
- **[docs/workflow/WORKFLOW.md](docs/workflow/WORKFLOW.md)** - Research process
- **[docs/service_system/](docs/service_system/)** - Service system details

---

## 🔧 Installation

### Prerequisites
- Python 3.8+
- Internet connection (for AI research)
- API keys (Perplexity + OpenAI recommended)

### Setup

```bash
# 1. Clone repository (if not already)
cd /home/eanhd/projects/vehicles

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your API keys

# 5. Verify installation
python3 -c "from tools.service_doc_generator import ServiceDocGenerator; print('✅ Setup complete!')"

# 6. Start web app
streamlit run app.py
```

### Dependencies

Key packages:
- `streamlit` - Web interface
- `anthropic` - Claude AI (optional)
- `openai` - GPT-4 (formatting)
- Custom: Perplexity client (in ai_client.py)

See [`requirements.txt`](requirements.txt) for full list.

---

## 🔍 Advanced Usage

### Command Line (For Developers)

```python
from tools.service_doc_generator import ServiceDocGenerator

gen = ServiceDocGenerator()

# Generate single document
doc_path, from_cache = gen.generate(
    year=2020,
    make="Ford",
    model="F-150",
    service="Engine Oil and Filter Change"
)
```

### Querying the Dataset

```bash
# Count total entries
jq 'length' data/vehicles.json

# Get all Ford F-150 entries
jq '[.[] | select(.make == "Ford" and (.model | contains("F-150")))]' data/vehicles.json

# List all makes
jq -r '.[].make' data/vehicles.json | sort -u

# Find all EVs (high voltage)
jq '[.[] | select(.difficulty_modifier >= 1.4)]' data/vehicles.json
```

---

## 📖 Documentation

### Quick References
- **[QUICK_START_APP.md](QUICK_START_APP.md)** - Get started in 60 seconds ⭐
- **[APP_STATUS.md](APP_STATUS.md)** - Current system status
- **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - Technical details
- **[CHECKLIST_STATUS.md](CHECKLIST_STATUS.md)** - Database coverage

### System Documentation  
- **[SYSTEM_COMPLETE.md](SYSTEM_COMPLETE.md)** - Full architecture
- **[docs/workflow/WORKFLOW.md](docs/workflow/WORKFLOW.md)** - Research process
- **[docs/agents/CLAUDE.md](docs/agents/CLAUDE.md)** - AI agent workflows

---

## 📊 Key Statistics

- **2,270 vehicles** across 48 manufacturers
- **153 services** with labor times and pricing
- **Coverage**: 1949-2025 model years
- **Cost**: ~$0.01-0.02 per new document (cached: free!)

---

## 📊 Dataset Statistics

### Coverage by Manufacturer (Top 15)

| Manufacturer | Entries | Status |
|--------------|---------|--------|
| Ford | 178 | ✅ Complete |
| Chevrolet | 173 | ✅ Complete |
| Audi | 105 | ✅ Complete |
| Nissan | 96 | ✅ Complete |
| Lexus | 82 | ✅ Complete |
| Chrysler | 79 | ✅ Complete |
| Volkswagen | 78 | ✅ Complete |
| Mercedes-Benz | 76 | ✅ Complete |
| Mazda | 73 | ✅ Complete |
| Jeep | 70 | ✅ Complete |
| BMW | 68 | ✅ Complete |
| Cadillac | 68 | ✅ Complete |
| Buick | 67 | ✅ Complete |
| Dodge | 64 | ✅ Complete |
| Volvo | 63 | ✅ Complete |

**Total: 48 manufacturers, 2,270 entries**

See [CHECKLIST_STATUS.md](CHECKLIST_STATUS.md) for complete breakdown.

---

## 📄 License

### Dataset
Wikipedia-sourced data used under **CC BY-SA 4.0** license with proper attribution. All Wikipedia citations include article names and revision dates.

### Code
Service documentation generator and tools released under **MIT License**.

### Service Documentation Output
Generated service documentation is provided **as-is for informational purposes**. Always verify critical specifications (torque values, fluid capacities, etc.) against manufacturer service manuals. Swoop Service Auto assumes no liability for errors in generated documentation.

---

---

## 🆘 Troubleshooting

### Common Issues

**App won't start**:
```bash
pkill -f streamlit
cd /home/eanhd/projects/vehicles && source venv/bin/activate
streamlit run app.py
```

**Missing API keys**:
```bash
# Check .env exists and has keys
cat .env | grep API_KEY
# Should show PERPLEXITY_API_KEY, OPENAI_API_KEY, etc.
```

**Generation fails**:
- Verify internet connection
- Check API key validity
- Try with different vehicle/service combination
- Check `service_docs/` for error logs

### Getting Help

- **Quick Start**: [QUICK_START_APP.md](QUICK_START_APP.md)
- **Current Status**: [APP_STATUS.md](APP_STATUS.md)
- **Full Troubleshooting**: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Technical Details**: [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)

---

## 📄 License

**Dataset**: Wikipedia-sourced data under CC BY-SA 4.0  
**Code**: MIT License  
**Generated Docs**: Informational purposes - verify critical specs with manufacturer manuals

---

## 🎉 Project Status

✅ **2,270 vehicles** across 48 manufacturers  
✅ **153 services** with labor times and pricing  
✅ **Web app** running and operational  
✅ **AI research** configured and tested  
✅ **Documentation** complete and up-to-date  

**Ready for production use!**

---

**Last Updated**: January 17, 2025  
**System Version**: 2.1  
**Maintainer**: Swoop Service Auto  

*Built with ❤️ for mobile mechanics who deserve quality tools*

---

**🚀 [Start Using The App Now →](QUICK_START_APP.md)**
