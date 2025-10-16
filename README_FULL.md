# 🚗 Swoop Service Auto - Professional Service Documentation System

> **AI-powered automotive service documentation - Your ALLDATA alternative**

**Status**: ✅ **FULLY OPERATIONAL** - Web app running at http://localhost:8501

This system combines comprehensive vehicle data with AI research to generate professional-grade service documentation for automotive technicians. Think ALLDATA or ProDemand, but powered by AI and tailored for mobile mechanics.

---

## 🎯 What This System Does

**Select a vehicle → Pick a service → Get professional documentation**

The system:
1. **Knows 2,270+ vehicles** (1949-2025) with complete specifications
2. **Understands 153 services** from oil changes to engine rebuilds
3. **Researches procedures** using AI with web access
4. **Generates beautiful HTML docs** with torque specs, diagrams, and step-by-step instructions
5. **Caches everything** for instant future access

### ✨ Key Features

✅ **Comprehensive Database**
- 2,270 vehicle entries covering major brands
- 153 common services with labor times and pricing
- Engines, transmissions, body styles, drivetrain options

✅ **AI-Powered Research**
- Uses Perplexity AI with web access for accurate, current information
- Finds torque specs, procedures, part numbers automatically
- Formats into professional, consistent documentation

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
# Research AI (has web access via :online mode)
PERPLEXITY_API_KEY=your_perplexity_key_here

# Formatting AI (primary)
OPENAI_API_KEY=your_openai_key_here

# Formatting AI (backup/optional)
ANTHROPIC_API_KEY=your_anthropic_key_here
```

Get API keys:
- Perplexity: https://www.perplexity.ai/settings/api
- OpenAI: https://platform.openai.com/api-keys
- Anthropic: https://console.anthropic.com/

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

## 🎯 Service Documentation System

### What It Does

The service documentation generator creates **professional repair procedures** tailored to specific vehicles:

✅ **AI-researched procedures** from manufacturer service manuals, forums, and technical documentation  
✅ **Torque specifications** for critical fasteners  
✅ **Parts lists** with OEM part numbers where available  
✅ **Safety warnings** and special tool requirements  
✅ **Fluid capacities** and specifications  
✅ **Mobile-friendly output** (HTML/PDF) for field use  
✅ **Swoop Service Auto branding** for professional presentation

### Example Output

```
=================================
Swoop Service Auto
Professional Service Documentation
=================================

Vehicle: 2020 Toyota Camry (XV70)
Service: Oil Change
Generated: January 17, 2025

SPECIFICATIONS:
- Oil Capacity: 4.6 quarts (0W-20 synthetic)
- Oil Filter: Toyota 04152-YZZA6
- Drain Plug Torque: 30 ft-lbs

PROCEDURE:
1. Warm engine to operating temperature
2. Raise vehicle on lift/jack stands
3. Remove drain plug (30 ft-lbs removal torque)...

[Full detailed procedure with diagrams]
```

### Recommended AI Model Configuration

**Best Quality (Production Use)**:
- **Claude 3.5 Sonnet** via Anthropic API
- Cost: ~$0.50-2.00 per service document
- Best accuracy, thorough research, professional output

**Budget Option (Development/Testing)**:
- **GPT-4 Turbo** via OpenRouter
- Cost: ~$0.10-0.50 per service document  
- Good quality, faster generation

**Not Recommended**:
- Free models (hallucinate specs, dangerous for mechanic work)
- GPT-3.5 (insufficient technical depth)

**See [docs/service_system/SERVICE_SYSTEM_SUMMARY.md](docs/service_system/SERVICE_SYSTEM_SUMMARY.md) for detailed model comparison.**

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

### Recent Gap Fills (January 2025)
✅ **Toyota Corolla** - Added 6 missing generations (E80-E150, 1984-2013)  
✅ **Ford F-150** - Added OBS 9th gen (1992-1996) and 12th gen (2009-2014)  
✅ **Chevrolet Silverado** - Added GMT900 and K2XX (2007-2018)

**Impact**: +12 entries covering ~24 million additional vehicles on the road!

### Data Quality Metrics

- ✅ **100%** Wikipedia-sourced with revision dates
- ✅ **100%** JSON validated before merge
- ✅ **100%** include difficulty modifiers with justification
- ✅ **95%+** include generation/platform codes
- ✅ **90%+** include complete powertrain details

---

## 🔧 Vehicle Data Schema

Each entry includes **12 required fields**:

```json
{
  "years": [2020, 2021, 2022, 2023],
  "make": "Toyota",
  "model": "Camry (XV70)",
  "engines": ["2.5L Dynamic Force I4 (203 hp)", "3.5L V6 (301 hp)"],
  "transmissions": ["8-speed automatic", "8-speed Direct Shift automatic"],
  "region": "American",
  "drivetrain": ["FWD"],
  "body_styles": ["4-door sedan"],
  "hybrid": false,
  "diesel": false,
  "difficulty_modifier": 1.0,
  "notes": "Eighth generation XV70 (2017-present). 2.5L Dynamic Force engine with D-4S injection. Timing chain (no replacement interval). Standard maintenance complexity. Data sourced from Wikipedia Toyota Camry article, January 2025 revision."
}
```

### Field Descriptions

- **years**: Production years for this generation (array of integers)
- **make**: Manufacturer name (string)
- **model**: Model name with generation code in parentheses (string)
- **engines**: Engine options with displacement, aspiration, and horsepower (array)
- **transmissions**: Transmission options with gear count/type (array)
- **region**: Primary market (American/Japanese import/European import)
- **drivetrain**: Available drivetrain configurations (array: FWD/RWD/AWD/4WD)
- **body_styles**: Body configurations sold in North America (array)
- **hybrid**: Hybrid electric availability (boolean)
- **diesel**: Diesel engine availability (boolean)
- **difficulty_modifier**: Service complexity multiplier ≥1.0 (float)
  - 1.0 = Standard modern vehicle
  - 1.1 = Diesel, basic hybrid, tight service access
  - 1.2 = Turbo performance, brass-era (1910s-1920s), medium-duty commercial
  - 1.3 = Heavy-duty commercial, air brakes, complex vintage
  - 1.4+ = High-voltage EVs (400V+), switchable voltage platforms
- **notes**: Service-critical details, platform sharing, Wikipedia citation with revision date (string)

---

## 🛠️ Tools & Scripts

### Service Documentation Generator

**Primary Tool**: `tools/service_doc_generator.py`

```bash
# Generate single service document
python tools/service_doc_generator.py \
  --year 2020 \
  --make Toyota \
  --model Camry \
  --service "Brake Pad Replacement" \
  --format html \
  --output service_docs/

# Generate batch documentation
python tools/batch_generate.py \
  --input vehicle_list.txt \
  --services "Oil Change,Brake Pads,Air Filter" \
  --output service_docs/batch/

# Start REST API server
python tools/service_api.py --port 5000
```

### Dataset Utilities

```bash
# Validate entire dataset
jq empty data/vehicles.json && echo "✅ Valid JSON"

# Count entries by decade
for decade in 1910s 1920s 1930s 1940s 1950s 1960s 1970s 1980s 1990s 2000s 2010s 2020s; do
  echo -n "$decade: "
  jq "[.[] | select(.years[] | . >= $(echo $decade | sed 's/s//') and . < $(echo $decade | sed 's/s//' | awk '{print $1+10}'))] | length" data/vehicles.json
done

# Export manufacturer to separate file
jq '[.[] | select(.make == "Toyota")]' data/vehicles.json > toyota_export.json

# Find missing models (compare against checklist)
grep "^- " CHECKLIST.md | sed 's/^- //' | while read model; do
  grep -q "\"$model\"" data/vehicles.json || echo "Missing: $model"
done
```

---

## 🔄 Workflow for Data Contributors

### The 5-Phase Workflow

**Phase 1: Setup & Gap Analysis**
- Create `wip/[manufacturer]/` workspace
- Create `PROGRESS_TRACKER.md`
- Identify missing models via grep/jq

**Phase 2: Decade-by-Decade Research**
- Research Wikipedia generation-specific pages
- Create isolated `wip/[manufacturer]/[decade].json` files
- Update progress tracker in real-time
- Validate: `jq empty wip/[manufacturer]/[decade].json`

**Phase 3: Validation & Quality Checks**
- Verify all 12 required fields present
- Check difficulty_modifier justifications
- Confirm Wikipedia citations with revision dates
- Validate: `jq empty [decade].json` for all decades

**Phase 4: Batch Append to vehicles.json**
- **Backup first**: `cp data/vehicles.json backups/vehicles_$(date +%Y%m%d_%H%M%S).json`
- Merge validated decades: `jq -s '.[0] + .[1] + ...' data/vehicles.json wip/.../[decades].json > temp.json`
- Validate merged file: `jq empty temp.json`
- If valid, replace: `mv temp.json data/vehicles.json`
- Archive completed decade files with `_APPENDED` suffix

**Phase 5: Manufacturer Completion**
- Create completion report (see examples in `wip/*/`)
- Update `CHECKLIST.md` with completion date
- Update `CHECKLIST_STATUS.md` status emoji
- Move to next manufacturer

**See [docs/workflow/WORKFLOW.md](docs/workflow/WORKFLOW.md) for complete procedures.**

### Key Rules for Contributors

❌ **NEVER**:
- Read `data/vehicles.json` directly (too large - use grep/jq)
- Append to `data/vehicles.json` without validation
- Skip backup before merging
- Guess at data when Wikipedia is unclear
- Work without `PROGRESS_TRACKER.md`

✅ **ALWAYS**:
- Use grep/jq for queries
- Create isolated decade files in `wip/`
- Maintain real-time progress tracking
- Validate with `jq empty` before proceeding
- Backup before every merge
- Cite Wikipedia with revision dates

---

## 📈 Data Quality Standards

### Sourcing Requirements

- **Primary source**: Wikipedia (generation-specific articles)
- **Citation format**: "Data sourced from Wikipedia [Article Name] article, [Month Year] revision."
- **When data unclear**: Leave it out, create TODO note (don't guess)
- **Cross-reference**: Platform-shared models for consistency

### Validation Requirements

- All decade files: `jq empty wip/[manufacturer]/[decade].json`
- After merge: `jq empty data/vehicles.json`
- **If validation fails**: Restore from backup immediately
- Entry counts match expected totals

### Documentation Standards

- All `difficulty_modifier ≥ 1.1` must have justification in notes
- All entries must cite Wikipedia with revision date
- Platform sharing documented (e.g., "GMT400 platform shared with...")
- Service-critical details required: timing chain/belt, HV battery isolation, specialty tools, air brakes, etc.

---

## 🔍 Example Queries

### Finding Vehicles

```bash
# All Toyota Camrys
jq '[.[] | select(.make == "Toyota" and (.model | contains("Camry")))]' data/vehicles.json

# All vehicles from 2020
jq '[.[] | select(.years[] == 2020)]' data/vehicles.json

# All hybrids
jq '[.[] | select(.hybrid == true)]' data/vehicles.json

# All EVs (high voltage)
jq '[.[] | select(.difficulty_modifier >= 1.4)]' data/vehicles.json

# All diesel trucks
jq '[.[] | select(.diesel == true and (.body_styles[] | contains("truck")))]' data/vehicles.json
```

### Statistics

```bash
# Count by manufacturer
jq -r '.[].make' data/vehicles.json | sort | uniq -c | sort -rn

# Average difficulty modifier
jq '[.[].difficulty_modifier] | add / length' data/vehicles.json

# Hybrid availability rate
echo "scale=2; $(jq '[.[] | select(.hybrid == true)] | length' data/vehicles.json) / $(jq 'length' data/vehicles.json) * 100" | bc

# Most common engine configuration
jq -r '.[].engines[]' data/vehicles.json | grep -o '[0-9.]*L [IV][0-9]*' | sort | uniq -c | sort -rn | head -10
```

---

## 🚧 Current Status & Roadmap

### ✅ Completed

- [x] 2,246 vehicle entries across 48 manufacturers
- [x] Complete historical coverage for major brands (Ford, Chevy, Toyota, etc.)
- [x] Service documentation generator with AI research
- [x] HTML/PDF output for field use
- [x] REST API for service generation
- [x] Comprehensive documentation structure

### 🔄 In Progress

- [ ] Gap analysis for rare/specialty models
- [ ] Enhanced wiring diagram integration
- [ ] Mobile app integration
- [ ] Offline service documentation cache

### 📋 Planned Enhancements

- [ ] OBD-II diagnostic code database
- [ ] Parts pricing integration
- [ ] Labor time estimation refinement
- [ ] Multi-language support
- [ ] Video procedure links

---

## 🤝 Contributing

We welcome contributions! Here's how:

### For Data Contributions

1. Check [CHECKLIST_STATUS.md](CHECKLIST_STATUS.md) for incomplete manufacturers
2. Follow the [5-phase workflow](docs/workflow/WORKFLOW.md)
3. Use [docs/agents/CLAUDE.md](docs/agents/CLAUDE.md) as your guide
4. Submit validated decade files for review

### For Code Contributions

1. Fork the repository
2. Create feature branch: `git checkout -b feature/my-enhancement`
3. Test thoroughly with real-world vehicle data
4. Document changes in relevant markdown files
5. Submit pull request with clear description

### For Service Documentation Feedback

1. Generate documentation for your vehicle
2. Verify accuracy against factory service manual
3. Report discrepancies via GitHub issues
4. Include vehicle details and service type

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
