# 🚗 Swoop Service Auto - Quick Reference Card

**Last Updated**: January 17, 2025

---

## 🚀 Start the App (One Command)

```bash
cd /home/eanhd/projects/vehicles && source venv/bin/activate && streamlit run app.py
```

**Then open**: http://localhost:8501

---

## 📱 Access URLs

| Location | URL |
|----------|-----|
| **Local** | http://localhost:8501 |
| **Network** | http://172.31.17.60:8501 |
| **Tailscale** | http://73.151.108.165:8501 |

---

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| **Vehicles** | 2,270 |
| **Services** | 780 |
| **Manufacturers** | 48 |
| **Years** | 1949-2025 |
| **Cost/Doc** | ~$0.01 |
| **Cached Docs** | 7 |

---

## 🔧 Common Commands

### Start App
```bash
streamlit run app.py
```

### Stop App
```bash
pkill -f streamlit
```

### Regenerate All Docs
```bash
python3 regenerate_docs.py
```

### Check Status
```bash
cat service_docs/cache_index.json | python3 -m json.tool
```

---

## 📖 Documentation Quick Links

| Document | Purpose |
|----------|---------|
| **START_HERE_JAN17.md** | Quick start guide |
| **QUICK_USE_GUIDE.md** | Daily usage reference |
| **README.md** | Complete documentation |
| **FINAL_STATUS_REPORT.md** | Current system status |
| **TROUBLESHOOTING.md** | Fix common issues |

---

## ⚙️ Configuration (.env)

```bash
# Required
PERPLEXITY_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Optional
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro
FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
```

---

## 🎯 Try These First

1. **2020 Toyota Camry - Oil Change**
2. **2019 Honda Accord - Oil Change**
3. **2021 Ford F-150 - Oil Change**

Each generates in ~15 seconds!

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| **App won't start** | `pkill -f streamlit && streamlit run app.py` |
| **Missing API keys** | Edit `.env` file |
| **Cache not updating** | Restart app |
| **Generation fails** | Check internet connection |

---

## 💡 Pro Tips

- ✅ Check cache before generating (instant results)
- ✅ Generate common services for your fleet
- ✅ Use Tailscale for field access
- ✅ Delete unwanted docs to save space
- ✅ Run regenerate script after updates

---

## 📞 Need Help?

**Quick Help**: START_HERE_JAN17.md  
**Daily Use**: QUICK_USE_GUIDE.md  
**Full Docs**: README.md  
**Troubleshooting**: TROUBLESHOOTING.md  

---

## ✅ System Status

✅ **Database**: Complete  
✅ **Web App**: Working  
✅ **AI Integration**: Configured  
✅ **Cache**: Functional  
✅ **Documents**: Professional  

**Status**: READY TO USE 🚀

---

**Built with ❤️ for Swoop Service Auto**
