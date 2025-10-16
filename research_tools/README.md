# Service Documentation Research Tools
**Swoop Service Auto - AI-Powered Repair Information System**

Replace expensive ALLDATA/ProDemand subscriptions with intelligent, on-demand research.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install anthropic
```

### 2. Set API Key
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 3. Generate Your First Service Document
```bash
cd research_tools
python service_doc_generator.py 2020 Chevrolet "Silverado 1500" "Brake Pads Replacement (Front)"
```

## 📚 Available Tools

### 1. Service Documentation Generator (`service_doc_generator.py`)
**Purpose**: Generate complete repair procedures with torque specs, parts lists, and troubleshooting

**Usage**:
```bash
python service_doc_generator.py <year> <make> <model> <service_name>
```

**Examples**:
```bash
# Brake service
python service_doc_generator.py 2020 Chevrolet "Silverado 1500" "Brake Pads Replacement (Front)"

# Oil change
python service_doc_generator.py 2022 Toyota Camry "Oil and Filter Change"

# Complex repair
python service_doc_generator.py 2019 Ford "F-150" "Timing Chain Replacement"

# Force refresh cached document
python service_doc_generator.py 2020 Honda Civic "Spark Plugs Replacement" --refresh
```

**Output**: 
- Cached JSON document in `service_docs/[make]/[model]_[year]/[service].json`
- Future lookups are instant (no API cost!)

---

### 2. Torque Spec Finder (`torque_spec_finder.py`)
**Purpose**: Quick lookup of torque specifications for specific components

**Usage**:
```bash
python torque_spec_finder.py <year> <make> <model> <component>
```

**Examples**:
```bash
# Cylinder head bolts
python torque_spec_finder.py 2020 Ford "F-150" "cylinder head"

# Wheel lug nuts
python torque_spec_finder.py 2018 Honda Civic "wheel lug nuts"

# Oil drain plug
python torque_spec_finder.py 2022 Toyota Camry "oil drain plug"

# Save results
python torque_spec_finder.py 2019 Chevrolet Silverado "intake manifold" --save
```

**Common Components**:
- cylinder head
- intake manifold
- exhaust manifold
- oil pan
- valve cover
- wheel lug nuts
- caliper bolts
- spark plugs
- oil drain plug
- timing cover

---

### 3. Wiring Diagram Helper (`wiring_diagram_helper.py`)
**Purpose**: Electrical diagnostics, wire colors, fuse locations, testing procedures

**Usage**:
```bash
python wiring_diagram_helper.py <year> <make> <model> <system> [issue]
```

**Examples**:
```bash
# Fuel system no-start diagnosis
python wiring_diagram_helper.py 2018 Honda Civic "fuel pump" "no start"

# Headlight system
python wiring_diagram_helper.py 2020 Ford F-150 "headlights"

# Starter circuit
python wiring_diagram_helper.py 2019 Toyota Camry "starter" "clicking noise"

# Power windows
python wiring_diagram_helper.py 2022 Chevrolet Silverado "power windows" "inoperative"

# Save results
python wiring_diagram_helper.py 2021 Honda Accord "fuel pump relay" --save
```

**Common Systems**:
- fuel pump
- starter motor
- alternator
- headlights
- power windows
- door locks
- ignition system
- cooling fans
- horn
- wipers

---

## 💰 Cost Analysis

### ALLDATA vs. This System

**ALLDATA Professional**:
- Annual subscription: $1,800-2,500
- Multi-vehicle shops: $3,600-7,200/year

**ProDemand**:
- Annual subscription: $2,400-3,600

**This AI System**:
- Setup cost: $0 (just API key)
- Per-document generation: $0.05-0.40 (Claude API)
- Cached documents: $0.00 (instant retrieval)
- Estimated annual cost: $50-200 (depending on usage)

**Break-even**: After generating ~50-100 unique service documents, you've saved money vs. subscriptions!

---

## 🔄 Caching System

The system automatically caches all generated documentation:

```
service_docs/
├── chevrolet/
│   ├── silverado_1500_2020/
│   │   ├── brake_pads_replacement_front.json
│   │   ├── oil_and_filter_change.json
│   │   └── spark_plugs_replacement.json
│   └── corvette_c8_2023/
│       └── brake_pads_replacement_front.json
├── ford/
│   └── f150_2021/
│       ├── brake_pads_replacement_front.json
│       └── oil_and_filter_change.json
└── toyota/
    └── camry_2022/
        └── oil_and_filter_change.json
```

**Benefits**:
- ✅ First lookup: ~5-30 seconds (AI research)
- ✅ Subsequent lookups: Instant (cached)
- ✅ Zero token cost for cached documents
- ✅ Build institutional knowledge over time

---

## 📋 Documentation Schema

Each generated service document includes:

### Vehicle Information
- Year, make, model, engine, generation
- Difficulty modifier from database

### Service Details
- Name, category, estimated time
- Mobile suitability

### Procedure
- Preparation steps
- Detailed step-by-step instructions
- Torque specifications for each fastener
- Tool requirements
- Safety warnings
- Inspection points

### Specifications
- Torque values (imperial + metric)
- Fluid types and capacities
- Measurements (rotor thickness, etc.)

### Parts List
- Required parts with OEM + aftermarket numbers
- Optional parts
- Estimated costs

### Tools Required
- Basic tools
- Specialized tools
- Optional tools

### Safety Information
- Critical warnings
- PPE requirements
- Common hazards

### Troubleshooting
- Common issues and solutions
- Diagnostic procedures
- Symptoms indicating service needed

### Metadata
- Generation date
- AI model used
- Research sources
- Verification status

---

## 🛠️ Integration with Your Workflow

### Scenario 1: Customer Calls for Quote
1. Customer: "I need front brake pads on my 2020 Silverado"
2. You: Run generator to get service doc
3. System: Returns procedure, parts list, estimated time
4. You: Calculate labor ($160) + parts ($80) = $240 quote
5. Customer: Approves
6. You: Follow documented procedure on-site

### Scenario 2: Unfamiliar Vehicle
1. Customer: "2018 Honda Civic won't start"
2. You: Check for codes, suspect fuel pump
3. Run wiring helper: `python wiring_diagram_helper.py 2018 Honda Civic "fuel pump" "no start"`
4. System: Returns fuse location, relay location, wire colors, test procedures
5. You: Diagnose using provided information
6. Found bad relay: Replace and invoice

### Scenario 3: Complex Repair
1. Customer: "Timing chain noise on 2015 Ford F-150 3.5L EcoBoost"
2. You: Generate service doc for timing chain replacement
3. System: Returns 20-step procedure with torque specs, special tools needed
4. You: Review procedure, determine if mobile-suitable (it's not!)
5. Refer to shop partner with documented procedure

---

## 🔍 Quality Control

### Documentation Review Process:
1. AI generates initial documentation
2. Status: "Pending human verification"
3. Technician performs service using doc
4. Technician notes any errors or additions
5. Update document and mark "Verified"
6. Future uses reference verified procedure

### Confidence Levels:
- **High**: Factory specifications found, well-documented vehicle
- **Medium**: General specifications, some assumptions
- **Low**: Limited information available, requires verification

---

## 📈 Future Enhancements

Planned features:
- [ ] Photo/video integration from YouTube
- [ ] Voice interface for hands-free lookup
- [ ] Parts ordering integration (RockAuto API)
- [ ] Service history tracking by VIN
- [ ] Customer communication templates
- [ ] TSB/recall automatic checks
- [ ] DTC (diagnostic trouble code) database
- [ ] Multi-language support (Spanish, French)
- [ ] Mobile app interface
- [ ] Offline mode with cached documents

---

## 🤝 Contributing to Knowledge Base

As you use the system:
1. Verify AI-generated specifications against actual work
2. Note any corrections needed
3. Add real-world tips from field experience
4. Build a library of verified procedures
5. Share with team members

Over time, you'll have a comprehensive, shop-specific knowledge base!

---

## 🆘 Troubleshooting

### "ANTHROPIC_API_KEY environment variable not set"
```bash
# Linux/Mac
export ANTHROPIC_API_KEY="your-key-here"

# Windows PowerShell
$env:ANTHROPIC_API_KEY="your-key-here"

# Make it permanent (Linux/Mac - add to ~/.bashrc or ~/.zshrc)
echo 'export ANTHROPIC_API_KEY="your-key-here"' >> ~/.bashrc
```

### "Vehicle not found in database"
- Check spelling of make/model
- Try partial model name: "F-150" vs "F150"
- Check if vehicle exists: `grep -i "ford" ../vehicles.json | head -20`
- Vehicle may not be in database yet - add it!

### "Service not found in catalog"
- Check spelling
- Try partial match: "Brake Pads" vs "Brake Pads Replacement (Front)"
- List available services: `jq '.[].name' ../services.json`

### "Could not parse JSON response"
- AI sometimes adds markdown formatting
- System creates fallback document with raw research
- Review and manually structure if needed

---

## 📞 Support

For questions or issues:
1. Check this README
2. Review SERVICE_DOCUMENTATION_SYSTEM.md in parent directory
3. Check example outputs in service_docs/

---

**Built with ❤️ for Swoop Service Auto**
*Replacing expensive subscriptions with intelligent, on-demand research*
