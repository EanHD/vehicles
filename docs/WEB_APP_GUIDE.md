# 🌐 Swoop Service Auto - Web App Guide

## Overview

The Swoop Service Auto web application provides an intuitive, professional interface for generating and managing automotive service documentation. Built with Streamlit, it offers a mobile-friendly, production-ready experience for mechanics in the field.

---

## 🚀 Quick Start

### Launch the Web App

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

### Access via Tailscale

Once running, you can access the app from any device on your Tailscale network:

1. Get your machine's Tailscale IP: `tailscale ip -4`
2. Access from phone/tablet: `http://[tailscale-ip]:8501`
3. Bookmark it for quick access in the field!

---

## 📱 Features

### 1. 🔍 Generate Service Documentation

**Interactive vehicle selection:**
- Choose Make → Model → Year in sequence
- View real-time vehicle details (engines, transmissions, body styles)
- See complexity ratings (difficulty modifiers)
- Filter services by category

**Smart generation:**
- Checks cache first (instant, free)
- Uses Perplexity AI for research (web-connected, accurate)
- Uses GPT-4o-mini for HTML formatting (clean, professional)
- Saves to cache automatically (no repeat costs!)

**Document actions:**
- Preview in-app
- Download HTML file
- Open in browser
- Share via email/messaging

### 2. 📚 Browse Cache

**Search and filter:**
- View all cached documents in a table
- Filter by make and service
- See generation dates and complexity ratings

**Quick access:**
- Click any cached document to view instantly
- No API calls = no costs for cached docs

### 3. 💬 AI Assistant

**Interactive help:**
- Ask questions about specific vehicles and services
- Get expert answers from Perplexity AI
- Context-aware (knows about your last generated doc)

**Example questions:**
- "What's the correct oil for a 2020 Ford F-150 with the 3.5L EcoBoost?"
- "How do I bleed brakes on a 2019 Toyota Camry?"
- "What are common issues with Honda Civic brake systems?"

### 4. 📊 Statistics

**System overview:**
- Total vehicles in database (2,270+)
- Available services (100+)
- Cached documents count
- Manufacturers covered (48)

**Visual analytics:**
- Top 10 manufacturers by vehicle count
- Services by category breakdown
- Most cached makes and services

### 5. ⚙️ Settings

**AI configuration:**
- View current Research AI settings (Perplexity)
- View current Formatter AI settings (OpenAI)
- See temperature and token limits

**Cache management:**
- View cache size (MB)
- Refresh cache index
- See database paths

**System information:**
- Python version
- Streamlit version
- Working directory

---

## 💡 Usage Tips

### For Mobile Mechanics

1. **Pre-generate common docs before going offline:**
   - Use the Browse Cache page to see what's cached
   - Generate docs for common vehicles you service
   - Cached docs work without internet!

2. **Quick document access:**
   - Bookmark your Tailscale URL
   - Add to phone home screen
   - Access from any device on your network

3. **Download for offline use:**
   - Download HTML files to phone/tablet
   - Open in any browser (no internet needed)
   - Professional enough to show customers

### Cost Optimization

**Free operations:**
- ✅ Viewing cached documents (instant)
- ✅ Browsing cache index
- ✅ Statistics page
- ✅ Settings page

**Paid operations:**
- 💰 Generating NEW documents (~$0.05-0.20 per doc)
- 💰 AI Assistant questions (~$0.01-0.05 per question)

**Cost reduction strategies:**
1. Generate once, use many times (cache FTW!)
2. Pre-generate for common vehicles
3. Use AI Assistant sparingly (or use cached context)

---

## 🎨 UI Features

### Professional Design

- **Clean, modern interface** inspired by ALLDATA/ProDemand
- **Mobile-responsive** layout (works on phones/tablets)
- **Color-coded information:**
  - Blue = Primary actions/headers
  - Green = Success/tips
  - Yellow = Warnings/common issues
  - Red = Safety warnings
- **Swoop Service Auto branding** on all generated docs

### Accessibility

- Large touch targets for mobile use
- High contrast text for outdoor visibility
- Print-friendly document layout
- Fast load times (even on mobile data)

---

## 🔧 Configuration

### Environment Variables

Edit `.env` file to customize AI providers:

```bash
# Research AI (for finding information)
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro
RESEARCH_TEMPERATURE=0.2
RESEARCH_MAX_TOKENS=4000

# Formatter AI (for generating HTML)
FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
FORMATTER_TEMPERATURE=0.3
FORMATTER_MAX_TOKENS=8000
```

### Recommended Configurations

**Best Quality (Production):**
```bash
RESEARCH_AI_PROVIDER=perplexity  # Web-connected, accurate
FORMATTER_AI_PROVIDER=openai     # Clean formatting
```
Cost: ~$0.05-0.20 per document

**Budget Option (Testing):**
```bash
RESEARCH_AI_PROVIDER=openai      # GPT-4 Turbo via OpenRouter
FORMATTER_AI_PROVIDER=openai     # GPT-4o-mini
```
Cost: ~$0.02-0.10 per document

---

## 📡 Deployment Options

### Option 1: Local Access (Tailscale)

**Best for:** Single mechanic or small shop

```bash
# Start the app
streamlit run app.py

# Access from any device on your Tailscale network
http://[your-tailscale-ip]:8501
```

**Pros:**
- Simple setup
- Secure (Tailscale encrypted)
- No public hosting costs
- Works from anywhere (Tailscale is always on)

**Cons:**
- Requires Tailscale on all devices
- Main machine must be running

### Option 2: Cloud Deployment (Streamlit Cloud)

**Best for:** Multiple mechanics or business use

1. Push code to GitHub repo
2. Connect to Streamlit Cloud (free tier available)
3. Set environment secrets
4. Get public URL: `https://yourapp.streamlit.app`

**Pros:**
- Always available
- No local machine needed
- Automatic HTTPS
- Easy sharing

**Cons:**
- Requires GitHub account
- Limited free tier
- API keys stored in cloud

### Option 3: Self-Hosted (Docker)

**Best for:** Shop with dedicated server

```bash
# Build Docker image
docker build -t swoop-service-auto .

# Run container
docker run -p 8501:8501 \
  --env-file .env \
  -v $(pwd)/service_docs:/app/service_docs \
  swoop-service-auto
```

**Pros:**
- Full control
- Can run on shop server
- Persistent cache storage

**Cons:**
- Requires Docker knowledge
- More maintenance

---

## 🔐 Security Considerations

### API Keys

- **Never commit .env file to git**
- Use Streamlit secrets for cloud deployment
- Rotate keys periodically

### Access Control

- Use Tailscale for private access
- Add Streamlit authentication for cloud deployment
- Consider IP whitelisting for business use

### Data Privacy

- Generated docs stored locally (not sent to cloud)
- Only research queries go to AI providers
- Cache is stored on your machine

---

## 🐛 Troubleshooting

### App Won't Start

```bash
# Check Python version (needs 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt

# Check for port conflicts
lsof -i :8501
```

### AI Connection Errors

```bash
# Test AI connections
cd tools
python ai_client.py test

# Check .env file exists and has keys
cat .env | grep API_KEY
```

### Slow Generation

- **First generation:** Slow (AI research takes 30-60 seconds)
- **Subsequent:** Fast (uses cache)
- **Tip:** Pre-generate common vehicles

### Cache Issues

```bash
# View cache location
ls -lh service_docs/

# Check cache index
cat service_docs/cache_index.json | jq 'length'

# Clear cache (if needed)
rm -rf service_docs/*
```

---

## 📈 Future Enhancements

### Planned Features

- [ ] **Offline mode** - Pre-download all data for offline use
- [ ] **PDF export** - Generate PDF versions of documents
- [ ] **Wiring diagrams** - AI-generated/sourced wiring diagrams
- [ ] **Multi-language** - Spanish, French translations
- [ ] **Voice input** - Hands-free queries in the field
- [ ] **Parts ordering** - Direct integration with parts suppliers
- [ ] **Labor time adjustment** - Learn from your actual times
- [ ] **Customer quotes** - Generate customer-facing quotes
- [ ] **Photo upload** - Add vehicle photos to documentation
- [ ] **Video links** - Link to relevant YouTube tutorials

### Community Requests

Submit feature requests via GitHub Issues!

---

## 📞 Support

### Documentation

- **This guide:** `/docs/WEB_APP_GUIDE.md`
- **Main README:** `/README.md`
- **Service system:** `/docs/service_system/`
- **Agent instructions:** `/docs/agents/CLAUDE.md`

### Getting Help

1. Check troubleshooting section above
2. Review AI configuration in Settings page
3. Test AI connections: `python tools/ai_client.py test`
4. Check GitHub Issues for similar problems

---

## 🎯 Best Practices

### For Shop Owners

1. **Pre-generate during downtime**
   - Run batch generator overnight
   - Cache common vehicles for your area
   - Reduces wait time for customers

2. **Train technicians**
   - Show how to search cache first
   - Teach cost-saving habits
   - Emphasize downloading for offline use

3. **Monitor costs**
   - Check cache statistics regularly
   - Track new documents generated
   - Adjust AI models based on budget

### For Mobile Mechanics

1. **Before leaving shop:**
   - Generate docs for day's appointments
   - Download to phone/tablet
   - Test Tailscale connection

2. **In the field:**
   - Use cached docs when possible
   - Download docs for offline viewing
   - Take notes in AI Assistant for later

3. **After service:**
   - Review any issues encountered
   - Update documentation if needed
   - Share useful docs with team

---

## 🏁 Getting Started Checklist

- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Configure API keys in `.env`
- [ ] Test AI connections: `python tools/ai_client.py test`
- [ ] Start web app: `streamlit run app.py`
- [ ] Generate first document (pick a common vehicle)
- [ ] Bookmark Tailscale URL on phone
- [ ] Pre-generate top 10 most common vehicles
- [ ] Train team on app usage
- [ ] Set up monitoring/backups

---

**Built with ❤️ for mechanics who need reliable information in the field.**

*Last Updated: January 17, 2025*
