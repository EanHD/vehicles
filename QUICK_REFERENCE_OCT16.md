# Quick Reference - Swoop Service Auto

## 🎯 What Was Fixed Today (Oct 16, 2024)

### UI Improvements
1. **Sidebar Metrics** - Now shows proper icons and formatting (🚗 Vehicles, 🔧 Services, 📄 Documents)
2. **Browse Cache Preview** - Fixed expansion to full width, increased height to 1000px
3. **Delete Confirmation** - Proper "Are you sure?" dialog when deleting cached documents

### HTML Styling Improvements
1. **Common Issues Section** - Fixed contrast issue (dark text on light background)
2. **Dark Mode Support** - All sections now have proper dark mode colors
3. **Diagram Paths** - Fixed relative paths so diagrams display correctly in browser

### Diagram Generation
1. **Working Perfectly** - Together AI integration generating high-quality diagrams
2. **Cost Effective** - ~$0.005 per diagram
3. **Smart Integration** - Only shows diagrams when actually generated (no placeholders)

## 🚀 How to Use the System

### Starting the App
```bash
cd /home/eanhd/projects/vehicles
./start_web_app.sh
```

App will be available via Tailscale on your configured URL.

### Generating Service Documentation

1. **Navigate to "Generate Service Doc"**
2. **Select Vehicle:**
   - Choose Make
   - Choose Model
   - Choose Year
   - View/select Engine and Transmission options

3. **Select Service:**
   - Pick from available services (Oil Change, Brake Pads, etc.)

4. **Click "Generate Documentation"**
   - System will research the procedure
   - Generate step-by-step instructions
   - Create technical diagrams (if enabled)
   - Save to cache for future use

### Browsing Cached Documents

1. **Navigate to "Browse Cache"**
2. **Filter by Make or Service** (optional)
3. **Select a document** from the dropdown
4. **Click "View Selected Document"** to see full preview
5. **Use "Delete Selected Document"** to remove (with confirmation)

### AI Assistant Feature

Ask questions about specific vehicles and services. The AI can:
- Provide detailed answers
- Reference your cached documentation
- Suggest related services
- Help troubleshoot issues

### Statistics Page

View analytics about your documentation library:
- Total vehicles in database
- Total services available
- Cached documents count
- Most common makes/services

## 📁 File Structure

```
/home/eanhd/projects/vehicles/
├── app.py                          # Main Streamlit application
├── data/
│   ├── vehicles.json              # Vehicle database
│   └── services.json              # Service definitions
├── service_docs/                  # Generated documentation
│   ├── diagrams/                  # AI-generated technical diagrams
│   ├── Toyota/Camry/              # Organized by Make/Model
│   │   └── 2015_Oil_Change.html
│   └── cache_index.json           # Cache metadata
├── tools/
│   ├── service_doc_generator.py   # Main doc generator
│   ├── ai_client.py               # AI API wrapper
│   └── diagram_generator.py       # Diagram generation
└── .env                           # API keys and configuration
```

## ⚙️ Configuration (.env)

### AI Providers
- **Research**: Perplexity Sonar Pro (web-enabled research)
- **Formatting**: OpenAI GPT-4O Mini (clean HTML output)
- **Diagrams**: Together AI FLUX.1-schnell (cost-effective, high quality)

### Switching Models
Edit `.env` file to change models:
```bash
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro

FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini

DIAGRAM_AI_PROVIDER=together
TOGETHER_IMAGE_MODEL=black-forest-labs/FLUX.1-schnell
```

### Disabling Diagrams
To save costs, disable diagram generation in the app settings or set:
```bash
DIAGRAM_AI_PROVIDER=
```

## 🎨 HTML Document Features

### Professional Styling
- Clean, mechanic-friendly design
- High contrast for readability
- Print-optimized layout
- Mobile-responsive

### Dark Mode Support
- Automatic detection of system preference
- Proper contrast in all sections
- Optimized for night work

### Content Sections
1. **Vehicle Specification** - Year, make, model, engine, transmission
2. **Service Overview** - Labor time, difficulty, cost estimate
3. **Safety Warnings** - Critical safety information
4. **Step-by-Step Procedure** - Detailed numbered steps with diagrams
5. **Torque Specifications** - All critical fastener specs
6. **Special Tools Required** - Tool list with part numbers
7. **Parts List** - OEM part numbers and descriptions
8. **Common Issues & Troubleshooting** - Known problems and solutions
9. **Pro Tips** - Professional insights and shortcuts

### Embedded Diagrams
- Technical illustrations for complex steps
- High-resolution (1024x1024)
- Professional automotive style
- Properly labeled components

## 💰 Cost Breakdown

### Per Document Generation
- Research (Perplexity): ~$0.02-0.05
- Formatting (GPT-4O Mini): ~$0.001-0.005
- Diagrams (2-5 per doc): ~$0.01-0.025
- **Total per document**: ~$0.03-0.08

### Monthly Estimate (Heavy Use)
- 100 documents/month: $3-8
- 500 documents/month: $15-40
- Very affordable compared to ALLDATA ($150+/month)

## 🐛 Troubleshooting

### App Won't Start
```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

### Missing Dependencies
```bash
cd /home/eanhd/projects/vehicles
pip install -r requirements.txt
```

### API Key Issues
Check `.env` file has valid keys:
```bash
cat .env | grep API_KEY
```

### Diagrams Not Generating
1. Check Together AI API key is valid
2. Verify `DIAGRAM_AI_PROVIDER=together` in .env
3. Check diagram cache directory exists: `service_docs/diagrams/`

### HTML Styling Issues
If you regenerated an old document and styling looks wrong:
- Use "Generate Documentation" with force_regenerate=True
- Or delete the cached document and regenerate

## 📊 Database Status

### Vehicles Database
- **Total vehicles**: Check in app sidebar (shows count)
- **Manufacturers**: Ford, Chevrolet, Toyota, BMW, Honda, etc.
- **Years covered**: 1940s to 2025+

### Services Database
- **Total services**: Check in app sidebar
- **Categories**: Engine, Transmission, Brakes, Suspension, Electrical, etc.
- **Common services**: Oil Change, Brake Pads, Alternator, Fuel Injectors, etc.

## 🔄 Updating the System

### Add New Vehicles
Edit `data/vehicles.json` following the existing format:
```json
{
  "make": "Toyota",
  "model": "Camry",
  "years": [2020, 2021, 2022],
  "engines": ["2.5L I4", "3.5L V6"],
  "transmissions": ["8-Speed Automatic"],
  "body_styles": ["Sedan"],
  "drivetrain": ["FWD"]
}
```

### Add New Services
Edit `data/services.json`:
```json
{
  "name": "Spark Plugs Replacement",
  "category": "Engine",
  "labor_time_hours": 1.5,
  "difficulty": "Medium"
}
```

### Reload App
After editing JSON files:
1. Save changes
2. Restart Streamlit app
3. Generator will automatically pick up new data

## 🎓 Best Practices

### For Best Results
1. **Be Specific** - Select exact year, engine, and transmission
2. **Review AI Output** - Always verify technical specs with manufacturer data
3. **Use Cache** - Documents are cached to save time and cost
4. **Export Important Docs** - Download HTML files for offline use
5. **Ask AI Assistant** - Use for clarifications and additional details

### Safety First
- Always verify torque specifications
- Follow manufacturer safety guidelines
- Use proper tools and equipment
- Consult professional when unsure

## 📞 Support

For issues or questions:
1. Check this Quick Reference
2. Review `IMPROVEMENTS_OCT16_2024.md` for recent changes
3. Check `README.md` for detailed documentation
4. Review error messages in the app

## ✅ System Status

Current status of your installation:
- ✅ App running (PID 21578)
- ✅ All API keys configured
- ✅ Diagram generation enabled
- ✅ 7 diagrams generated
- ✅ Multiple documents cached
- ✅ All improvements applied

**System is ready for production use!**
