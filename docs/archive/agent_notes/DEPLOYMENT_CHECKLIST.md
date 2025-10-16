# ✅ Swoop Service Auto - Deployment Checklist

**Use this checklist to deploy and verify your system is production-ready.**

---

## 🔧 Pre-Deployment Setup

### Environment Setup

- [ ] **Python 3.8+ installed**
  ```bash
  python3 --version  # Should be 3.8 or higher
  ```

- [ ] **Virtual environment created**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- [ ] **Dependencies installed**
  ```bash
  pip install -r requirements.txt
  ```

- [ ] **Verify installations**
  ```bash
  pip list | grep -E "streamlit|requests|flask|pandas"
  ```

### API Keys Configuration

- [ ] **Copy .env.example to .env**
  ```bash
  cp .env.example .env
  ```

- [ ] **Perplexity API key added**
  - Sign up: https://www.perplexity.ai
  - Get key: https://www.perplexity.ai/settings/api
  - Add to .env: `PERPLEXITY_API_KEY=pplx-...`

- [ ] **OpenAI API key added**
  - Sign up: https://platform.openai.com
  - Get key: https://platform.openai.com/api-keys
  - Add to .env: `OPENAI_API_KEY=sk-proj-...`

- [ ] **Verify .env file is in .gitignore**
  ```bash
  grep ".env" .gitignore
  ```

### Test Connections

- [ ] **Test AI connections**
  ```bash
  python tools/ai_client.py test
  ```
  Should show: ✅ All AI connections successful!

- [ ] **Generate test document**
  ```bash
  python tools/service_doc_generator.py \
    --year 2020 --make Toyota --model Camry \
    --service "Oil Change"
  ```
  Should create: `service_docs/Toyota/Camry/2020_Oil_Change.html`

- [ ] **Verify document quality**
  - Open HTML file in browser
  - Check: professional appearance, torque specs, procedure steps
  - Verify: Swoop Service Auto branding present

---

## 🌐 Web App Deployment

### Local Testing

- [ ] **Start web app**
  ```bash
  ./start_web_app.sh
  ```

- [ ] **Access locally**
  - Open: http://localhost:8501
  - Should load without errors

- [ ] **Test core features**
  - [ ] Vehicle selection works (Make → Model → Year)
  - [ ] Service selection works (Category → Service)
  - [ ] Document generation works (first time: 30-60s)
  - [ ] Cache retrieval works (second time: <1s)
  - [ ] Preview in-app works
  - [ ] Download button works

- [ ] **Test Browse Cache page**
  - [ ] Shows generated documents
  - [ ] Filter by make works
  - [ ] Filter by service works
  - [ ] View document works

- [ ] **Test AI Assistant page**
  - [ ] Can ask questions
  - [ ] Gets responses
  - [ ] Chat history persists

- [ ] **Test Statistics page**
  - [ ] Shows correct vehicle count
  - [ ] Shows correct service count
  - [ ] Shows cached document count
  - [ ] Charts display correctly

- [ ] **Test Settings page**
  - [ ] AI configuration displayed
  - [ ] Database paths shown
  - [ ] Cache size calculated

### Mobile Access (Tailscale)

- [ ] **Get Tailscale IP**
  ```bash
  tailscale ip -4
  ```

- [ ] **Access from mobile device**
  - Open browser on phone/tablet
  - Go to: `http://[your-tailscale-ip]:8501`
  - Should load web app

- [ ] **Test mobile functionality**
  - [ ] Touch targets are large enough
  - [ ] Text is readable
  - [ ] All features work on mobile
  - [ ] No horizontal scrolling issues

- [ ] **Bookmark on mobile device**
  - Add to home screen for quick access

---

## 📊 Performance Testing

### Cache Performance

- [ ] **Generate a document twice**
  1. First time: Record time (should be 30-60s)
  2. Second time: Record time (should be <1s)
  
- [ ] **Verify cache hit rate**
  - Generate 5 different documents
  - Retrieve each one 3 times
  - Calculate: (cached requests / total requests) * 100
  - Target: Should approach 80%+ over time

### System Performance

- [ ] **Web app response time**
  - Page loads: < 2 seconds
  - Form interactions: < 500ms
  - Document preview: < 1 second

- [ ] **Database query speed**
  - Vehicle search: < 50ms
  - Service listing: < 50ms

- [ ] **Memory usage acceptable**
  ```bash
  # While web app running
  ps aux | grep streamlit
  # Should be < 500MB RAM
  ```

---

## 💰 Cost Verification

### Initial Cost Test

- [ ] **Generate 5 test documents**
  - Note: First generation is paid ($0.01-0.06 each)
  - Expected cost: $0.05-0.30 total

- [ ] **Verify caching saves money**
  - Retrieve those 5 documents again
  - Should be instant and FREE

- [ ] **Check API usage on provider dashboards**
  - Perplexity: https://www.perplexity.ai/settings/api
  - OpenAI: https://platform.openai.com/usage
  - Verify charges match expectations

### Cost Monitoring

- [ ] **Set up usage alerts** (on provider dashboards)
  - Perplexity: Alert at $10
  - OpenAI: Alert at $5
  
- [ ] **Track cache stats weekly**
  ```bash
  cat service_docs/cache_index.json | jq 'length'
  ```

---

## 🔐 Security Verification

### Access Control

- [ ] **.env is gitignored**
  ```bash
  git status  # Should not show .env
  ```

- [ ] **No API keys in code**
  ```bash
  grep -r "pplx-" . --exclude-dir=venv --exclude-dir=.git
  grep -r "sk-proj-" . --exclude-dir=venv --exclude-dir=.git
  # Should return no results
  ```

- [ ] **Tailscale is running**
  ```bash
  tailscale status
  ```

### Data Privacy

- [ ] **Verify data stays local**
  - Check: service_docs/ directory is on your machine
  - Check: vehicles.json is on your machine
  - Only AI queries go to cloud

- [ ] **No sensitive data in logs**
  - Review web app terminal output
  - Should show no API keys or sensitive info

---

## 📚 Documentation Verification

### Essential Docs Present

- [ ] **README.md** - Complete and updated
- [ ] **QUICK_START.md** - Easy to follow
- [ ] **docs/WEB_APP_GUIDE.md** - Comprehensive
- [ ] **docs/ARCHITECTURE.md** - System design explained
- [ ] **.env.example** - Template with all variables

### Documentation Accuracy

- [ ] **Test quick start guide**
  - Follow steps exactly as written
  - Should work without issues

- [ ] **Verify all links work**
  - Click through documentation links
  - No broken references

---

## 🚀 Production Readiness

### Functionality Checklist

- [ ] **Core features working**
  - ✅ Vehicle search
  - ✅ Service selection
  - ✅ Document generation
  - ✅ Caching
  - ✅ Mobile access
  - ✅ AI assistant

- [ ] **Error handling tested**
  - Try invalid vehicle (should show error)
  - Try with no internet (should show error)
  - Try with wrong API key (should show error)

- [ ] **Edge cases handled**
  - Very old vehicle (1920s) - should work
  - Very new vehicle (2025) - should work
  - Special characters in model name - should work

### User Experience

- [ ] **Professional appearance**
  - Documents look good
  - Web app is clean and intuitive
  - No broken styling

- [ ] **Mobile usability**
  - Works well on phone
  - Easy to use with one hand
  - Text is readable outdoors

- [ ] **Speed is acceptable**
  - First generation: 30-60s (acceptable, AI research)
  - Cached retrieval: <1s (excellent)
  - Web app navigation: instant

### Business Readiness

- [ ] **Can show to customers**
  - Documents are professional
  - Branding is appropriate
  - Information is accurate

- [ ] **Cost is sustainable**
  - Monthly cost < $50 for typical usage
  - Much cheaper than ALLDATA ($135-300/month)
  - ROI is clear

- [ ] **Reliable enough for daily use**
  - Works consistently
  - No frequent crashes
  - Cache persists between restarts

---

## 📋 Pre-Launch Checklist

### Technical

- [x] System architecture complete
- [x] AI client working (hybrid approach)
- [x] Caching system functional
- [x] Web app deployed
- [x] Mobile access working
- [x] REST API available
- [x] Command line tools ready

### Data

- [x] 2,270+ vehicles in database
- [x] 48 manufacturers covered
- [x] 100+ services defined
- [x] Wikipedia citations included
- [x] Backup system in place

### Documentation

- [x] Quick start guide
- [x] Web app guide
- [x] Architecture documentation
- [x] API documentation
- [x] Troubleshooting guide

### Testing

- [ ] **Completed all checklists above**
- [ ] **Generated 10+ test documents**
- [ ] **Verified cache works**
- [ ] **Tested mobile access**
- [ ] **Shown to at least one other person**

---

## 🎯 Launch Day Tasks

### Morning of Launch

1. **Final system check**
   ```bash
   python tools/ai_client.py test
   ./start_web_app.sh
   ```

2. **Pre-generate common vehicles**
   ```bash
   python tools/batch_generate.py --max 50
   ```
   Cost: ~$1-3, but then FREE forever

3. **Verify mobile access**
   - Test from phone
   - Bookmark URL
   - Download a test document

### During First Week

- [ ] **Generate 20-30 documents** for your common vehicles
- [ ] **Monitor costs** on API dashboards
- [ ] **Track cache hit rate** (should improve daily)
- [ ] **Note any issues** for future improvements
- [ ] **Train team members** if applicable

### First Month

- [ ] **Build substantial cache** (50-100 documents)
- [ ] **Calculate actual costs** vs projections
- [ ] **Measure time savings** vs alternative methods
- [ ] **Get feedback** from users
- [ ] **Plan improvements** based on usage

---

## ✅ Sign-Off

### System Owner Approval

I have verified that:

- [ ] All technical requirements are met
- [ ] All tests pass successfully
- [ ] Documentation is complete and accurate
- [ ] Security measures are in place
- [ ] Cost monitoring is set up
- [ ] Mobile access works
- [ ] System is ready for production use

**Signed:** _____________________ **Date:** _____________

---

## 🆘 Emergency Contacts

### If Things Go Wrong

**Web app won't start:**
```bash
source venv/bin/activate
pip install -r requirements.txt
./start_web_app.sh
```

**AI connection fails:**
```bash
python tools/ai_client.py test
# Check .env file
nano .env
```

**Cache corrupted:**
```bash
rm service_docs/cache_index.json
# Restart web app, will rebuild
```

**Need to restore database:**
```bash
ls backups/  # Find latest backup
cp backups/vehicles_YYYYMMDD_HHMMSS.json data/vehicles.json
```

---

## 📞 Support Resources

- **Quick Start:** [QUICK_START.md](QUICK_START.md)
- **Web App Guide:** [docs/WEB_APP_GUIDE.md](docs/WEB_APP_GUIDE.md)
- **Architecture:** [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- **Troubleshooting:** See Web App Guide

---

**Deployment Status: Ready for verification**

Use this checklist to ensure a smooth deployment and successful launch!

**Last Updated: January 17, 2025**
