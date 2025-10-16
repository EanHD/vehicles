# 🚀 Swoop Service Auto - Quick Start Guide

**Get professional automotive service documentation in 5 minutes!**

---

## ⚡ Super Quick Start (Web App)

```bash
# 1. Navigate to project
cd /home/eanhd/projects/vehicles

# 2. Run startup script
./start_web_app.sh
```

That's it! The script handles everything:
- ✅ Creates virtual environment
- ✅ Installs dependencies
- ✅ Tests AI connections
- ✅ Launches web app
- ✅ Shows you your Tailscale URL

**Access the app:**
- Local: http://localhost:8501
- Mobile (via Tailscale): http://[your-ip]:8501

---

## 📖 First-Time Setup (5 Steps)

### Step 1: Check Prerequisites

```bash
# Verify Python 3.8+ installed
python3 --version

# Verify git (should be in project already)
pwd  # Should show: /home/eanhd/projects/vehicles
```

### Step 2: Set Up API Keys

```bash
# Copy example environment file
cp .env.example .env

# Edit with your favorite editor
nano .env
# OR
vim .env
```

**Required API Keys:**

1. **Perplexity API** (Research - RECOMMENDED)
   - Sign up: https://www.perplexity.ai
   - Get API key: https://www.perplexity.ai/settings/api
   - Free tier: $5 credit (enough for 100-500 documents)
   - Paste key in .env: `PERPLEXITY_API_KEY=pplx-...`

2. **OpenAI API** (Formatting)
   - Sign up: https://platform.openai.com
   - Get API key: https://platform.openai.com/api-keys
   - Pay as you go: ~$0.001-0.01 per document
   - Paste key in .env: `OPENAI_API_KEY=sk-proj-...`

**Your .env should look like:**
```bash
PERPLEXITY_API_KEY=pplx-5iNNMDS3HgW5n399...
OPENAI_API_KEY=sk-proj-Q_hsyeGcPpvqiv...
```

### Step 3: Install Dependencies

```bash
# Activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 4: Test Configuration

```bash
# Verify AI connections work
python tools/ai_client.py test
```

**Expected output:**
```
Testing research AI connection...
  Provider: perplexity
  Model: sonar-pro
  ✅ Connection successful!

Testing formatter AI connection...
  Provider: openai
  Model: gpt-4o-mini
  ✅ Connection successful!
```

### Step 5: Launch Web App

```bash
# Option A: Use startup script (recommended)
./start_web_app.sh

# Option B: Direct launch
streamlit run app.py
```

🎉 **Done!** The web app will open in your browser automatically.

---

## 🔍 Your First Service Document

### Using Web App (Recommended)

1. **Select Vehicle:**
   - Make: Ford
   - Model: F-150
   - Year: 2020

2. **Select Service:**
   - Category: Brakes
   - Service: Brake Pads Replacement (Front)

3. **Click "Generate Service Documentation"**

4. **Wait 30-60 seconds** (first generation is slow, caching for future use)

5. **View/Download** your professional service guide!

### Using Command Line

```bash
python tools/service_doc_generator.py \
  --year 2020 \
  --make Ford \
  --model "F-150" \
  --service "Brake Pads Replacement (Front)"
```

**Output location:**
```
service_docs/Ford/F-150/2020_Brake_Pads_Replacement_Front.html
```

Open in browser to view!

---

## 💡 Pro Tips

### Cost Saving

**Cache is King!** The system automatically caches documents:
- ✅ First generation: $0.01-0.06 (30-60 seconds)
- ✅ Subsequent retrievals: **FREE** (<1 second)

**Pre-generate common vehicles:**
```bash
# Use batch generator
python tools/batch_generate.py --max 50

# This generates top 50 most common vehicle/service combos
# Cost: ~$1-3, but then FREE forever!
```

### Mobile Access

1. **Get your Tailscale IP:**
   ```bash
   tailscale ip -4
   ```

2. **Access from phone/tablet:**
   - Open browser
   - Go to: `http://[your-tailscale-ip]:8501`
   - Bookmark it!

3. **Works anywhere** with Tailscale running

### Offline Use

1. **Download documents** from web app
2. **HTML files work offline** - no internet needed
3. **Share via email** or messaging with customers

---

## 🎯 Common Use Cases

### Use Case 1: Mobile Mechanic

**Scenario:** Appointment at customer's house

**Before leaving shop:**
```bash
# Generate doc for appointment
python tools/service_doc_generator.py \
  --year 2019 \
  --make Toyota \
  --model Camry \
  --service "Oil Change"
```

**In the field:**
- Open HTML on phone
- Follow professional procedures
- Show customer the documented process

### Use Case 2: Shop Owner

**Scenario:** Train new technician

**Pre-generate shop's common services:**
```bash
# Generate batch of most common vehicles
python tools/batch_generate.py --max 100

# Cost: ~$5
# Result: 100 cached docs for instant access
```

**Use:**
- Technician selects vehicle in web app
- Gets instant, professional documentation
- No waiting, no repeated costs

### Use Case 3: Complex Repair

**Scenario:** Unfamiliar with vehicle specifics

**In web app:**
1. Generate service documentation
2. Ask AI Assistant: "What are common issues with 2020 Honda Civic brake calipers?"
3. Get expert answers with citations
4. Proceed with confidence

---

## 🔧 Troubleshooting

### Web App Won't Start

**Issue:** `streamlit: command not found`

**Fix:**
```bash
# Activate virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install streamlit
```

### API Connection Failed

**Issue:** `❌ Connection failed: 401 Unauthorized`

**Fix:**
1. Check `.env` file exists
2. Verify API keys are correct (no spaces, full key)
3. Test again: `python tools/ai_client.py test`

### Slow Generation

**Issue:** Taking longer than 60 seconds

**Causes:**
- Slow internet connection
- AI provider rate limits
- Complex service requiring more research

**Fix:**
- Wait patiently (first time only!)
- Check internet connection
- Document will cache for instant future access

### Cache Not Working

**Issue:** Every request takes 30-60 seconds

**Check:**
```bash
# Verify cache exists
ls -lh service_docs/

# Check cache index
cat service_docs/cache_index.json | jq 'length'
```

**Fix:**
```bash
# Rebuild cache (if corrupted)
rm service_docs/cache_index.json
# App will rebuild on next generation
```

---

## 📚 Next Steps

### Learn More

- **[Web App Guide](docs/WEB_APP_GUIDE.md)** - Complete web interface documentation
- **[Architecture](docs/ARCHITECTURE.md)** - System design and data flow
- **[README](README.md)** - Full project overview

### Customize

- **Change AI models** - Edit `.env` to use different providers
- **Add services** - Edit `data/services.json`
- **Add vehicles** - Follow workflow in `docs/workflow/WORKFLOW.md`

### Deploy

- **Tailscale** - Already works! Just share your IP
- **Cloud hosting** - Follow guides for Streamlit Cloud, Heroku, AWS
- **Docker** - Build container for shop server deployment

---

## 🆘 Need Help?

### Quick Checks

1. ✅ In correct directory? `pwd` should show `/home/eanhd/projects/vehicles`
2. ✅ Virtual environment activated? Prompt should show `(venv)`
3. ✅ API keys set? `cat .env | grep API_KEY` should show your keys
4. ✅ Dependencies installed? `pip list | grep streamlit`

### Get Support

- Check [Web App Guide](docs/WEB_APP_GUIDE.md) for detailed help
- Review error messages carefully
- Test AI connections: `python tools/ai_client.py test`

### Common Solutions

**"Module not found"** → `pip install -r requirements.txt`

**"API key invalid"** → Check `.env` file, verify keys on provider website

**"Document not found"** → Check `data/vehicles.json` has the vehicle (use jq to search)

**"Port already in use"** → Kill existing process or use different port: `streamlit run app.py --server.port 8502`

---

## ✅ Success Checklist

After completing this guide, you should have:

- [x] Virtual environment set up
- [x] API keys configured in `.env`
- [x] Dependencies installed
- [x] AI connections tested successfully
- [x] Web app running
- [x] Generated your first service document
- [x] Accessed app from mobile device (via Tailscale)
- [x] Understood caching (first generation = slow, subsequent = instant)
- [x] Bookmarked Tailscale URL on phone

**🎉 Congratulations! You're ready to use Swoop Service Auto in production!**

---

## 💰 Cost Expectations

### Typical Usage

**Small shop (10-20 vehicles/week):**
- First generation: ~$5/month
- Subsequent (cached): FREE
- **Total: $5/month**

**Medium shop (50-100 vehicles/week):**
- First generation: ~$10-20/month
- Heavy cache usage
- **Total: $10-20/month**

**Large shop (200+ vehicles/week):**
- First generation: ~$30-50/month
- Massive cache savings
- **Total: $30-50/month**

**Remember:** Every document is cached forever. The more you use it, the more you save!

---

**Last Updated: January 17, 2025**

*Built for mechanics who need professional documentation without breaking the bank.* 🔧
