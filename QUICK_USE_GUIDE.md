# 🚀 Quick Use Guide - Swoop Service Auto

**Updated**: January 17, 2025  
**All Features Working**: ✅

---

## Starting the App

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

**Access URLs**:
- Local: http://localhost:8501
- Network: http://172.31.17.60:8501
- Tailscale: http://73.151.108.165:8501

---

## Generating Your First Service Document

### Step 1: Select Vehicle

1. Click **"🔍 Generate Service Doc"** in sidebar
2. Choose **Make** (e.g., Toyota)
3. Choose **Model** (e.g., Camry)
4. Choose **Year** (e.g., 2015)

### Step 2: Choose Service

1. Filter by **Category** (optional)
2. Select **Service** (e.g., "Oil Change")

### Step 3: Generate

1. ☑️ Check **"🎨 Generate AI diagrams"** if you want technical illustrations
2. ☐ Leave unchecked to save costs (default)
3. Click **"⚡ Generate Service Documentation"**
4. Wait 10-30 seconds

### Step 4: View & Use

- **View** the document inline in Streamlit
- **Download** as HTML file
- **Share** via email or Tailscale

---

## When to Use Diagrams

### ✅ Enable Diagrams For:

- Complex procedures (timing belt, transmission)
- First-time repairs you're unfamiliar with
- Training new technicians
- Customer education

### ☐ Skip Diagrams For:

- Simple routine maintenance (oil changes, filters)
- Services you've done many times
- Cost-sensitive situations
- Quick reference lookups

**Cost**: ~$0.01-0.015 per diagram (Together AI)

---

## Understanding the Document

### Document Sections

1. **Vehicle Specification** - Year, make, model, engine, transmission
2. **Service Overview** - Labor time, category, skill level
3. **⚠️ Safety Warnings** - Critical safety information
4. **📋 Step-by-Step Procedure** - Detailed numbered steps
   - Time estimates per step
   - Torque specs in-line
   - Embedded diagrams (if generated)
5. **🔧 Torque Specifications** - All critical torque values
6. **📐 Reference Diagrams** - Full-size diagram gallery
7. **🛠️ Required Parts** - Parts list with OEM numbers
8. **🔨 Special Tools** - Tools needed
9. **🔍 Common Issues** - Troubleshooting guide
10. **💡 Pro Tips** - Professional insights
11. **Citations** - Research sources for verification

### Reading Torque Specs

```
Component: Oil drain plug
Value: 27 ft-lbs
Pattern: Straight (not star pattern)
⚠️ Note: Verify torque - critical specification
```

**Always verify critical specs** - The AI finds accurate values, but double-check in factory manual for liability.

---

## Using the Browse Cache Feature

1. Click **"📚 Browse Cache"** in sidebar
2. See all previously generated documents
3. **Filter** by make/model/service
4. **Select** a document to preview
5. **Download** or **Re-generate** if needed

**Benefits**:
- Instant access (no API cost)
- Faster than regenerating
- Consistent documentation

---

## Using the AI Assistant

1. Click **"💬 AI Assistant"** in sidebar
2. Ask questions about:
   - Service procedures
   - Troubleshooting issues
   - Part identification
   - Tool requirements
3. Get detailed, vehicle-specific answers

**Example Questions**:
- "How do I reset the oil life monitor on a 2015 Toyota Camry?"
- "What size socket do I need for Honda lug nuts?"
- "Why is my oil drain plug leaking after service?"

---

## Cost Management

### Per Document Costs

| Scenario | Cost | Time |
|----------|------|------|
| Cached doc (no regeneration) | $0.00 | <1 sec |
| New doc without diagrams | $0.01-0.02 | 10-15 sec |
| New doc with 2-3 diagrams | $0.02-0.03 | 20-30 sec |

### Money-Saving Tips

1. **Cache everything** - First generation costs, rest are free
2. **Skip diagrams** for routine services
3. **Generate common services** for your fleet ahead of time
4. **Use cached docs** instead of regenerating

### Monthly Budget Estimate

**Light use** (5-10 new docs/week): ~$5-10/month  
**Moderate use** (20-30 new docs/week): ~$20-30/month  
**Heavy use** (50+ new docs/week): ~$50-80/month  

**Compare to ALLDATA**: $3,000-5,000/year subscription

---

## Tips for Best Results

### 1. Vehicle Selection

- Be specific with model (e.g., "Camry XV50" vs just "Camry")
- Select correct year (specs change between years)
- Verify engine size matches your vehicle

### 2. Service Selection

- Choose the most specific service available
- Category filter helps narrow choices
- Review labor time estimate for accuracy

### 3. Using Generated Docs

- **Verify torque specs** against factory manual (AI is accurate but safety first)
- **Check diagram accuracy** - AI diagrams are illustrations, not photos
- **Use common issues section** for troubleshooting
- **Follow safety warnings** carefully

### 4. Quality Control

- Cross-reference critical specs with service manual
- Use multiple documents if procedure is complex
- Ask AI Assistant if anything is unclear
- Report any errors or issues

---

## Common Workflows

### Daily Oil Change Workflow

1. Customer arrives
2. Open Browse Cache
3. Find vehicle's oil change doc (cached from first time)
4. View on tablet/phone at bay
5. Follow procedure
6. Use torque specs
7. Reference common issues if problems

**Time saved**: No manual lookup needed!

### Complex Repair Workflow

1. Generate doc WITH diagrams
2. Review procedure and time estimate
3. Order parts from parts list
4. Gather special tools
5. Follow step-by-step with diagrams
6. Use troubleshooting guide if issues
7. Save doc for future reference

**Confidence level**: High - detailed guidance

### Training New Technician

1. Generate docs for common services (with diagrams)
2. Have technician review before service
3. Use docs as training materials
4. Reference during supervised work
5. Build confidence with visual aids

**Learning accelerated**: Clear visual guidance

---

## Troubleshooting

### "Diagram could not be loaded"

**Fixed!** ✅ Update applied October 16, 2024  
- Diagrams now embed as base64
- No more loading issues
- Works in Streamlit iframe

### "Vehicle not found"

- Check spelling of make/model
- Try different year
- Model may not be in database
- Contact support to add vehicle

### "Service not found"

- Try searching without filters
- Service might be named differently
- Check category selection
- Available services: 153 total

### Generation is slow

- Normal: 10-30 seconds
- With diagrams: Add 10-20 seconds
- AI research takes time
- Be patient for quality

### AI gives generic info

- Try regenerating (AI is non-deterministic)
- Use more specific vehicle selection
- Check citations for source quality
- Report if consistently poor

---

## Pro Tips from Mechanics

### Workshop Integration

1. **Tablet mount** at each bay with Tailscale access
2. **Pre-generate common services** for your fleet
3. **Print critical procedures** for offline backup
4. **Use QR codes** to link to cached docs

### Customer Relations

1. **Show diagrams** to explain repairs
2. **Print procedure** for transparency
3. **Share parts list** for customer approval
4. **Build trust** with documented process

### Business Benefits

1. **Faster service** - No manual searching
2. **Consistent quality** - Same procedure every time
3. **Training tool** - Onboard techs faster
4. **Documentation** - Prove work was done correctly
5. **Cost savings** - vs. expensive subscriptions

---

## System Maintenance

### Weekly

- Review cache size (delete old docs if needed)
- Check API usage/costs
- Verify key services are cached

### Monthly

- Review quality of generated docs
- Update frequently-used vehicles
- Clean up temporary files

### As Needed

- Update service catalog
- Add new vehicles to database
- Regenerate docs with updated info

---

## Getting Help

### In-App

- Use **AI Assistant** for questions
- Check **Statistics** for system health
- Review **Settings** for configuration

### Documentation

- **README.md** - System overview
- **IMPLEMENTATION_GUIDE.md** - Technical details
- **TROUBLESHOOTING.md** - Common issues
- **IMPROVEMENTS_COMPLETE_OCT16.md** - Latest updates

### Support

- Check GitHub issues/discussions
- Review documentation files
- Contact system maintainer

---

## Quick Reference: Keyboard Shortcuts

(Streamlit default shortcuts)

- **Ctrl+S** - Rerun app
- **Ctrl+R** - Refresh page
- **Ctrl+F** - Search page
- **Ctrl+P** - Print document

---

## Remember

✅ **First document costs** - subsequent retrievals are free  
✅ **Diagrams are optional** - use when needed  
✅ **Verify critical specs** - safety first  
✅ **Cache is your friend** - pre-generate common services  
✅ **AI Assistant helps** - don't hesitate to ask questions  

---

**You're Ready to Go!** 🔧

Start with simple services to get familiar, then tackle more complex repairs with confidence. The system improves with use as more documents get cached.

**Happy Wrenching!** 🚗💨
