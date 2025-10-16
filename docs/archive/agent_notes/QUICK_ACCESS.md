# 🚗 Quick Access Card - Swoop Service Auto

## 🌐 WEB APP ACCESS
```
Local:    http://localhost:8501
Network:  http://172.31.17.60:8501
Status:   🟢 RUNNING
```

## 📊 SYSTEM STATS
```
Vehicles:  2,270 models
Services:  153 types
Years:     1902-2025
Makes:     49 brands
```

## 🚀 START/STOP COMMANDS

**Start App:**
```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

**Stop App:**
```bash
pkill -f streamlit
```

**Check Status:**
```bash
ps aux | grep streamlit
curl http://localhost:8501/_stcore/health
```

## 📖 KEY DOCUMENTATION

| File | Purpose |
|------|---------|
| `START_HERE.md` | System overview |
| `ACCESS_INFO.md` | Usage instructions |
| `TROUBLESHOOTING.md` | Fix common issues |
| `CURRENT_STATUS.md` | Full system status |
| `README.md` | Complete documentation |

## 🔧 COMMON TASKS

**Generate Service Doc:**
1. Open http://172.31.17.60:8501
2. Select vehicle details
3. Choose service type
4. Click "Generate"
5. View HTML guide

**View Cached Docs:**
```bash
ls -lh service_docs/
```

**Check Database:**
```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
python3 -c "from tools.service_doc_generator import ServiceDocGenerator; g=ServiceDocGenerator(); print(f'{len(g.vehicles)} vehicles, {len(g.services)} services')"
```

## 💰 COST ESTIMATE
```
Per Document:  ~$0.05-0.08 (first time)
Cached:        FREE (instant)
vs ALLDATA:    ~$150/month
```

## 🆘 QUICK TROUBLESHOOTING

**Port in use:**
```bash
pkill -f streamlit && sleep 2 && streamlit run app.py
```

**Module not found:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Database not loading:**
```bash
ls -lh data/*.json  # Should show 1.9M and 92K
```

**API key issues:**
```bash
cat .env  # Verify keys are present
```

## 📱 MOBILE ACCESS

1. Ensure phone is on same network (or Tailscale)
2. Open browser: http://172.31.17.60:8501
3. Mobile-responsive interface works automatically

## 🎯 EXAMPLE WORKFLOW

**Generate oil change for 2020 Toyota Camry:**
```
Year:         2020
Make:         Toyota
Model:        Camry
Engine:       2.5L 4-Cylinder
Transmission: Automatic
Body:         Sedan
Service:      Oil Change & Filter Replacement
```
→ Click "Generate" → Wait 10-30 sec → View professional guide

## 🔑 API KEYS LOCATION
```
File: /home/eanhd/projects/vehicles/.env

PERPLEXITY_API_KEY=pplx-...  # Research AI
OPENAI_API_KEY=sk-...        # Formatter AI
ANTHROPIC_API_KEY=sk-ant-... # Alternative
```

⚠️ **NEVER commit .env to Git!**

## 📂 IMPORTANT DIRECTORIES
```
data/          - Database files (vehicles.json, services.json)
service_docs/  - Generated HTML documentation cache
tools/         - Core generator scripts
venv/          - Python virtual environment
```

## ✅ SYSTEM STATUS
```
Database:   ✅ 2,270 vehicles loaded
Services:   ✅ 153 services available
Web App:    ✅ Running on port 8501
AI:         ✅ Research + Formatter ready
Cache:      ✅ Operational
```

---

**Last Updated:** January 17, 2025  
**Status:** 🟢 **FULLY OPERATIONAL**  
**Ready for production use!**
