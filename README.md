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
- **NEW: AI Document Editor** - Edit and improve cached docs with guided AI assistant

✅ **REST API**
- FastAPI-based REST API for mobile app integration
- Full vehicle/service database access
- Automatic documentation generation
- Smart caching for performance
- OpenAPI/Swagger documentation

✅ **Professional Output**
- HTML documents styled for readability
- Mobile-friendly for shop floor use
- Swoop Service Auto branding
- Cached for instant retrieval

---

## 🚀 Quick Start

### Option 1: Web Interface (Recommended for Quick Testing)

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
./start_app.sh  # or: streamlit run app.py
```

Open your browser to http://localhost:8501

**See detailed walkthrough**: [`docs/app/QUICK_START_APP.md`](docs/app/QUICK_START_APP.md)

### Option 2: REST API (Recommended for Mobile App Integration)

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
./start_api.sh  # or: python api.py
```

Open your browser to http://localhost:8000/docs for interactive API documentation

**See API guide**: [`docs/api/API_QUICK_START.md`](docs/api/API_QUICK_START.md)

### 3. Generate Documentation

**Web Interface:**
1. Select a vehicle (Make → Model → Year)
2. Choose a service from the catalog
3. Click "Generate Service Documentation"
4. Get professional docs in 10-30 seconds!

**API:**
```bash
curl -X POST http://localhost:8000/api/v1/documentation/generate \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"year":2015,"make":"Toyota","model":"Camry","service":"Oil Change"}'
```

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
├── 📱 app.py                          # ⭐ Streamlit web interface
├── 🔌 api.py                          # ⭐ FastAPI REST API (for mobile app integration)
├── 📁 data/                           # Core databases
│   ├── vehicles.json                  # 2,270 vehicles with specs
│   └── services.json                  # 153 services with labor/pricing
│
├── 📁 tools/                          # Python modules
│   ├── service_doc_generator.py       # Main doc generator
│   ├── doc_editor_assistant.py        # AI document editor
│   ├── ai_client.py                   # Multi-provider AI client
│   ├── diagram_generator.py           # Technical diagram generation
│   ├── service_api.py                 # Legacy Flask API
│   └── batch_generate.py              # Batch generation tool
│
├── 📁 service_docs/                   # Generated documentation (cache)
│   └── [make]/[model]/[year]/        # Organized by vehicle
│       └── [service].html             # HTML documents
│
├── 📁 docs/                           # System documentation
│   ├── archive/                       # Historical agent notes
│   │   └── agent_notes/               # Legacy reports & handoffs
│   ├── agents/                        # AI agent instructions
│   ├── service_system/                # Service system docs
│   └── workflow/                      # Research workflow
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
├── 📋 QUICK_START_APP.md              # ⭐ Web app user guide
├── 📋 API_DOCUMENTATION.md            # ⭐ REST API reference
├── 📋 API_QUICK_START.md              # ⭐ API quick start guide
├── 📋 AI_ASSISTANT_GUIDE.md           # ⭐ NEW: AI Editor guide
├── 📋 APP_STATUS.md                   # Current web app status
├── 📋 IMPLEMENTATION_GUIDE.md         # Technical implementation
├── 📋 SYSTEM_COMPLETE.md              # Architecture overview
├── 📋 CHECKLIST.md                    # Manufacturer coverage checklist
├── 📋 ACCESS_INFO.md                  # Access URLs & walkthrough
├── 📋 TODO.md                         # Open tasks
├── 📋 TROUBLESHOOTING.md              # Common issues
├── 📄 tracking.md                     # Research priorities & notes
├── 🚀 start_app.sh                    # Start Streamlit web app
├── 🚀 start_api.sh                    # Start REST API server
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

## 🤖 AI Document Editor

**NEW FEATURE**: The AI Document Editor Assistant helps you refine and improve your cached service documents with verified information.

### Key Features

- **📝 Guided Editing** - Step-by-step workflow for adding/modifying information
- **✅ Automatic Verification** - AI fact-checks all changes before applying
- **📎 Source Upload** - Upload PDFs, URLs, or text to verify your edits
- **💰 Token Efficient** - Minimal API usage (~$0.001-0.003 per edit)
- **🎯 Focused** - Designed specifically for document editing, not general chat

### How to Use

1. Navigate to **💬 AI Assistant** in the web app
2. Select a cached document to edit
3. Type your request: *"Add oil drain plug torque: 18 ft-lbs"*
4. Assistant verifies the information
5. Confirm to apply the change

### Example Workflow

```
User: "Add oil drain plug torque: 18 ft-lbs"

Assistant: 🔍 Analyzing and verifying...
✅ Verification Passed (confidence: 95%)

Information to add: Oil drain plug torque: 18 ft-lbs (24 Nm)
Target section: torque-specifications
Sources: Toyota FSM, TorqueSpec DB

Reply "yes" to confirm.

User: "yes"


Assistant: ✅ Successfully added information to torque-specifications section!
```

**See full guide**: [`docs/ai-assistant/AI_ASSISTANT_GUIDE.md`](docs/ai-assistant/AI_ASSISTANT_GUIDE.md)

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

### Quick Start Guides

- **[docs/app/QUICK_START_APP.md](docs/app/QUICK_START_APP.md)** - Web app quick start ⭐
- **[docs/api/API_QUICK_START.md](docs/api/API_QUICK_START.md)** - REST API quick start ⭐
- **[docs/ai-assistant/AI_ASSISTANT_GUIDE.md](docs/ai-assistant/AI_ASSISTANT_GUIDE.md)** - AI Editor guide ⭐

### API & Integration

- **[docs/api/API_DOCUMENTATION.md](docs/api/API_DOCUMENTATION.md)** - Full API reference
- **[docs/api/MOBILE_APP_INTEGRATION.md](docs/api/MOBILE_APP_INTEGRATION.md)** - Mobile app setup

### Web App & Usage

- **[docs/app/APP_STATUS.md](docs/app/APP_STATUS.md)** - Current system status
- **[docs/app/TROUBLESHOOTING.md](docs/app/TROUBLESHOOTING.md)** - Common issues
- **[docs/app/TESTING_GUIDE.md](docs/app/TESTING_GUIDE.md)** - Testing procedures

### System Architecture & Development

- **[docs/architecture/SYSTEM_ARCHITECTURE.md](docs/architecture/SYSTEM_ARCHITECTURE.md)** - Full architecture
- **[docs/architecture/IMPLEMENTATION_GUIDE.md](docs/architecture/IMPLEMENTATION_GUIDE.md)** - Technical details
- **[docs/agents/](docs/agents/)** - AI agent workflows
- **[docs/workflow/](docs/workflow/)** - Research process

### Project History & Archives

- **[docs/archive/](docs/archive/)** - Previous handoffs, status reports, summaries, and project notes

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
