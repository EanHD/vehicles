# Quick Start Guide
**Swoop Service Auto - Professional Service Documentation System**

## 🚀 Quick Start (3 Commands)

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

Then open: **http://localhost:8501**

---

## 📖 Basic Workflow

### Generate Your First Service Document

1. **Select Vehicle**
   - Make: Ford
   - Year: 2020
   - Model: F-150
   - Engine: 5.0L V8

2. **Choose Service**
   - Category: Brakes
   - Service: Brake Pads Replacement (Front)

3. **Click "Generate Documentation"**
   - Wait 30-60 seconds (first time)
   - AI researches and creates professional guide
   - Document auto-saves to cache
   - Future lookups are instant!

4. **View Your Document**
   - Scroll through comprehensive procedure
   - Note torque specifications
   - Review safety warnings
   - Save/print as needed

---

## 🎯 Common Tasks

### Task 1: Look Up Torque Specs
```
1. Generate Service Doc
2. Select vehicle + service
3. Look for "Torque Specifications" section
4. Note values for your job
```

### Task 2: Get AI Help
```
1. Go to "💬 AI Assistant" tab
2. Ask: "What's the correct torque for 2020 F-150 brake caliper bolts?"
3. Get instant expert answer
```

### Task 3: Re-Use Old Documentation
```
1. Go to "📚 Browse Cache" tab
2. Search for vehicle/service
3. Click to view instantly
4. No re-generation needed!
```

---

## 💡 Pro Tips

**Tip 1: Generate Common Jobs First**
Build your cache with frequent services:
- Oil changes (by engine type)
- Brake pad replacements
- Alternator replacements
- Spark plug changes

**Tip 2: Force Regenerate for Updates**
If specs change or you want fresh research:
- Check "Force Regenerate" box
- System will research again with latest info

**Tip 3: Print to PDF**
- Open generated HTML in browser
- Print → Save as PDF
- Keep offline copy on phone/tablet

**Tip 4: Ask Specific Questions**
In AI Assistant:
- ❌ "How do I fix brakes?"
- ✅ "What's the bleeding sequence for 2018 Toyota Camry ABS brakes?"

---

## 🔧 Supported Services (780+)

### Brakes
- Pad replacement (front/rear)
- Rotor replacement
- Caliper replacement
- Master cylinder
- Brake fluid flush
- Drum brakes

### Engine & Cooling
- Spark plug replacement
- Ignition coil replacement
- Thermostat replacement
- Water pump
- Radiator replacement
- Serpentine belt

### Electrical & Charging
- Battery replacement
- Alternator replacement
- Starter replacement
- Fuse box work

### Transmission & Drivetrain
- Transmission fluid change
- CV axle replacement
- Differential service
- Transfer case service

### Suspension & Steering
- Strut replacement
- Control arm replacement
- Ball joint replacement
- Tie rod replacement
- Power steering pump

### HVAC
- AC recharge
- Compressor replacement
- Blower motor
- Heater core

### Exhaust
- Catalytic converter
- Muffler replacement
- O2 sensor replacement

...and 700+ more!

---

## 🎨 What You Get in Each Document

### 1. Vehicle Information
- Year, Make, Model, Engine
- Trim level if applicable
- Special notes for this vehicle

### 2. Service Overview
- Description of service
- Estimated time
- Difficulty level
- Required skills

### 3. Step-by-Step Procedure
- Numbered steps
- Clear instructions
- Time estimates per step
- Torque specs inline

### 4. Torque Specifications Table
- Component name
- Torque value (ft-lbs)
- Pattern if applicable
- Special notes

### 5. Parts & Tools Required
- Complete parts list
- OEM part numbers
- Tool requirements
- Special tools needed

### 6. Safety Warnings
- Critical safety info
- OSHA guidelines
- PPE requirements
- Common hazards

### 7. Common Issues & Tips
- Known problems
- Troubleshooting steps
- Pro mechanic tips
- What to avoid

### 8. Diagram Placeholders
- Marked where diagrams help
- References to service manuals
- Key components identified

---

## 📊 System Stats (Current)

| Metric | Count |
|--------|-------|
| Vehicles in Database | 2,270 |
| Services Available | 780 |
| Years Covered | 1950-2025 |
| Makes Covered | 33+ |

### Top Makes:
- Ford, Chevrolet, Toyota, Honda
- Dodge, RAM, GMC, Nissan
- Jeep, Chrysler, Lexus, Acura
- BMW, Mercedes-Benz, Audi
- Volkswagen, Mazda, Subaru
- Kia, Hyundai, Genesis
- Infiniti, Cadillac, Lincoln
- Buick, Volvo, Tesla

---

## 💰 Cost Comparison

### ALLDATA Professional:
- **$3,600/year** subscription
- Limited to 1 user
- Internet required
- Can't export documentation

### Swoop Service Auto:
- **~$0.001-0.003 per document**
- Unlimited users
- Works offline (cached docs)
- Export/print freely
- **Save $3,500+/year!**

### Example Cost Breakdown:
- 100 documents: **$0.30**
- 500 documents: **$1.50**  
- 1000 documents: **$3.00**
- 5000 documents: **$15.00**

Even generating 5000 documents = 1% of ALLDATA cost!

---

## 🛠️ Customization

### Change AI Models
Edit `.env` file:
```env
# Want more detailed research?
RESEARCH_AI_MODEL=gpt-4o  # More expensive but better

# Want cheaper generation?
FORMATTER_AI_MODEL=gpt-3.5-turbo  # Cheaper but less polish

# Want different provider?
RESEARCH_AI_PROVIDER=anthropic
RESEARCH_AI_MODEL=claude-3-5-sonnet-20241022
```

### Adjust Response Length
```env
RESEARCH_MAX_TOKENS=8000  # Longer, more detailed
FORMATTER_MAX_TOKENS=12000  # More comprehensive
```

### Change Temperature (Creativity)
```env
RESEARCH_TEMPERATURE=0.1   # More factual (recommended)
RESEARCH_TEMPERATURE=0.5   # More creative (not recommended)
```

---

## 📱 Access Options

### Option 1: Local (Current Setup)
```
URL: http://localhost:8501
Access: This computer only
```

### Option 2: LAN Access
```
URL: http://192.168.x.x:8501
Access: Any device on your network
```

### Option 3: Tailscale (Recommended for Remote)
1. Install Tailscale on server
2. Access from anywhere: http://100.x.x.x:8501
3. Secure, encrypted connection
4. Works on phone, tablet, laptop

### Option 4: Cloud Deployment
- Deploy to AWS/Azure/GCP
- Professional domain
- HTTPS encryption
- Scale to team

---

## ⚡ Performance Tips

### Speed Up Generation
1. **Build cache first**: Generate common jobs
2. **Use cache**: Most lookups are instant
3. **Batch generation**: Generate multiple docs in session

### Reduce Costs
1. **Cache aggressively**: Rarely force regenerate
2. **Use GPT-4o-mini**: Cheaper than GPT-4
3. **Optimize prompts**: Shorter = cheaper

### Improve Quality
1. **Use Perplexity for research**: Web access = better specs
2. **Use Claude for formatting**: Best at structure
3. **Increase max_tokens**: More detailed responses

---

## 🆘 Quick Troubleshooting

### "Service not found"
✅ Use exact service name from dropdown menu

### "Vehicle not found"
✅ Select from dropdown menus (don't type manually)

### Generation takes forever
✅ First gen: 30-60s is normal (AI research)
✅ Cached: Should be <1 second
✅ Check internet connection

### AI Assistant not responding
✅ Check .env has API keys
✅ Run: `python tools/ai_client.py test`
✅ Verify API provider is up

### Can't access on phone
✅ Use your computer's IP address
✅ Or set up Tailscale (recommended)

---

## 📞 Support Resources

### Documentation
- `README.md` - Complete system overview
- `FIXES_AND_IMPROVEMENTS.md` - Technical details
- `IMPLEMENTATION_GUIDE.md` - Setup guide
- `.env.example` - Configuration template

### Testing
```bash
# Test AI connections
python tools/ai_client.py test

# Test generator
python -c "from tools.service_doc_generator import ServiceDocGenerator; gen = ServiceDocGenerator(); print('OK')"
```

---

## 🎓 Learning Resources

### Understanding the System
1. **AI Client**: `tools/ai_client.py`
   - Handles all AI communication
   - Supports multiple providers
   - Unified interface

2. **Generator**: `tools/service_doc_generator.py`
   - Core documentation engine
   - Research + formatting workflow
   - Caching system

3. **Web App**: `app.py`
   - Streamlit interface
   - 4 main pages
   - Real-time generation

### Modifying the System
```python
# Add a new AI provider
# Edit: tools/ai_client.py
# Add to _get_api_key() and _get_api_url()

# Change HTML styling
# Edit: tools/service_doc_generator.py
# Modify the <style> section in _generate_html()

# Add new service fields
# Edit: data/services.json
# Update _generate_html() to display new fields
```

---

## ✅ Daily Workflow Example

**Morning:**
```
1. Start app: streamlit run app.py
2. Check today's jobs
3. Generate docs for each job
4. Print/save to tablet
```

**On the Job:**
```
1. Open cached HTML on phone/tablet
2. Follow step-by-step procedure
3. Check torque specs as needed
4. Use AI Assistant for questions
```

**End of Day:**
```
1. Review generated documents
2. Note any issues/updates needed
3. Stop app (Ctrl+C)
```

---

## 🚀 Ready to Go!

You now have everything you need:
- ✅ Professional service documentation
- ✅ AI technical assistant
- ✅ Comprehensive vehicle database
- ✅ Cost-effective operation
- ✅ Offline capability (cached docs)

**Start generating documentation and save thousands per year!** 🎉

---

**Quick Command Reference:**
```bash
# Start app
streamlit run app.py

# Test AI
python tools/ai_client.py test

# Stop app
Ctrl+C (or pkill streamlit)

# Restart app
pkill streamlit && streamlit run app.py
```
