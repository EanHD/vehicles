# 🚀 Quick Start - Swoop Service Auto Web App

**Get started in 60 seconds!**

---

## Step 1: Start the App (if not running)

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

Or use the convenience script:
```bash
./start_web_app.sh
```

---

## Step 2: Access the App

Open your browser to one of these URLs:

- **Local (same machine)**: http://localhost:8501
- **Network (same network)**: http://172.31.17.60:8501
- **External (via Tailscale)**: http://73.151.108.165:8501

---

## Step 3: Generate Your First Service Document

### Example: Oil Change for 2021 Ford F-150

1. **Select Vehicle**:
   - Make: `Ford`
   - Model: `F-150`
   - Year: `2021`

2. **Review Details**:
   - See available engines (e.g., "3.5L V6 EcoBoost")
   - See transmissions
   - Note complexity rating

3. **Select Service**:
   - Category: `Maintenance` (or select "All")
   - Service: `Engine Oil and Filter Change`

4. **Generate**:
   - Click **"⚡ Generate Service Documentation"**
   - Wait ~10-30 seconds
   - View professional HTML document

---

## What You'll Get

The AI will research and generate a comprehensive document including:

✅ **Vehicle-Specific Information**
- Exact oil type and capacity
- Filter part numbers
- Service intervals

✅ **Step-by-Step Procedure**
- Professional instructions
- Safety warnings
- Special tools needed

✅ **Technical Specifications**
- Torque specs for drain plug
- Oil filter specs
- Reset procedures

✅ **Additional Notes**
- Best practices
- Common issues
- Tips for mobile service

---

## Features

### 🔄 Caching
Documents are saved after generation. If you request the same vehicle/service again, it loads instantly from cache.

### 🔄 Force Regenerate
Check the "Force regenerate" box to create a new document even if one exists in cache.

### 🎨 AI Diagrams (NEW!)
Check the "🎨 Generate AI diagrams" box to add technical illustrations to your documentation.
- Cost: ~$0.005-$0.04 per diagram (depending on provider)
- Requires API key setup (see `QUICK_DIAGRAM_SETUP.md`)
- Adds visual aids for complex procedures
- Cached for reuse (free after first generation)

### 💬 Interactive Chat (Coming Soon)
Ask follow-up questions and enhance the documentation:
- "What if the drain plug is stripped?"
- "What's the torque spec for the oil filter?"
- "How do I reset the oil life monitor?"

---

## Pro Tips

### Best Vehicle/Service Combinations to Try

**Maintenance**:
- Oil change (most vehicles)
- Air filter replacement
- Tire rotation

**Brakes**:
- Brake pad replacement
- Brake rotor replacement
- Brake fluid flush

**Engine**:
- Spark plug replacement
- Serpentine belt replacement
- Coolant flush

**Suspension**:
- Shock absorber replacement
- Strut replacement

### Popular Vehicles in Database
- Ford F-150, Mustang, Explorer
- Chevrolet Silverado, Camaro, Equinox
- Toyota Camry, Corolla, RAV4, Tacoma
- Honda Civic, Accord, CR-V
- Ram 1500, 2500
- Jeep Wrangler, Cherokee, Grand Cherokee

---

## Troubleshooting

### App Won't Start
```bash
# Check if port is already in use
pkill -f streamlit

# Restart
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

### Generation Takes Too Long
- First-time generation requires AI research (15-45 seconds)
- Cached lookups are instant
- Complex vehicles/services take longer

### Document Quality Issues
- Ensure API keys are set in `.env`
- Check internet connection (research AI needs web access)
- Try regenerating with "Force regenerate"

### Can't Find Vehicle
- Check spelling (case-sensitive)
- Try different year (some models have limited years)
- Check `data/vehicles.json` to verify vehicle exists

---

## Cost Considerations

### Per Document Generation

**Research Phase** (Perplexity Sonar):
- ~$0.001 - $0.003 per document
- Uses web access for accurate info

**Formatting Phase** (OpenAI GPT-4):
- ~$0.005 - $0.015 per document

**Total**: ~$0.01 - $0.02 per NEW document  
**Cached**: $0.00 (instant retrieval)

### Daily Usage Estimates
- 50 new documents/day: ~$0.50-$1.00
- 200 cached lookups/day: $0.00
- Monthly (with 50% cache hits): ~$15-$30

---

## Next Steps

### Expand Your Knowledge
1. Try different vehicle/service combinations
2. Review generated HTML documents
3. Note which vehicles/services are most common in your area

### Contribute
1. Report vehicles missing from database
2. Suggest service additions
3. Improve documentation templates

### Deploy to Production
1. Set up on VPS/cloud server
2. Configure custom domain
3. Add user authentication
4. Set up backup system

---

## Key Files

- `app.py` - Main Streamlit interface
- `tools/service_doc_generator.py` - Document generator
- `tools/ai_client.py` - AI provider wrapper
- `data/vehicles.json` - Vehicle database (2,270 vehicles)
- `data/services.json` - Service catalog (153 services)
- `service_docs/` - Generated documents cache
- `.env` - API keys (keep private!)

---

## Support & Documentation

- **Main README**: `README.md`
- **App Status**: `APP_STATUS.md` (current state)
- **Implementation**: `IMPLEMENTATION_GUIDE.md`
- **Troubleshooting**: `TROUBLESHOOTING.md`
- **System Overview**: `SYSTEM_COMPLETE.md`

---

## 🎉 You're Ready!

The Swoop Service Auto system is:
- ✅ Fully operational
- ✅ 2,270+ vehicles ready
- ✅ 153 services defined
- ✅ AI-powered research
- ✅ Professional output

**Start generating documents and building your knowledge base!** 🚀

---

*Last updated: January 17, 2025*
