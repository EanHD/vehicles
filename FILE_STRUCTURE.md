# File Structure - Swoop Service Auto

## 📁 Complete Directory Layout

```
vehicles/
│
├── 🚀 **QUICK START**
│   ├── start_app.sh                    # Quick start script - Run this!
│   ├── QUICK_START_GUIDE.md           # Daily use guide
│   └── COMPLETION_REPORT.md            # Session completion summary
│
├── 📚 **DOCUMENTATION**
│   ├── README.md                       # Main overview
│   ├── QUICK_START_GUIDE.md           # Quick reference
│   ├── FIXES_AND_IMPROVEMENTS.md      # Technical details
│   ├── SYSTEM_STATUS.md               # Current status
│   ├── COMPLETION_REPORT.md           # This session's work
│   ├── FILE_STRUCTURE.md              # This file
│   └── IMPLEMENTATION_GUIDE.md        # Setup instructions
│
├── 🎛️ **CONFIGURATION**
│   ├── .env                           # API keys (DO NOT SHARE)
│   ├── .env.example                   # Configuration template
│   └── requirements.txt               # Python dependencies
│
├── 💻 **APPLICATION**
│   ├── app.py                         # Streamlit web interface
│   └── venv/                          # Python virtual environment
│
├── 🔧 **TOOLS** (Python modules)
│   ├── ai_client.py                   # Unified AI interface
│   ├── service_doc_generator.py       # Documentation generator
│   └── __pycache__/                   # Python cache
│
├── 📊 **DATA**
│   ├── vehicles.json                  # 2,270 vehicles database
│   └── services.json                  # 780 services database
│
├── 📄 **GENERATED DOCUMENTS**
│   └── service_docs/
│       ├── cache_index.json           # Cache lookup index
│       └── [Make]/[Model]/            # Organized by vehicle
│           └── [Year]_[Service].html  # Generated documents
│
└── 🗑️ **OTHER**
    ├── wip/                           # Work in progress files
    ├── backups/                       # Backup files
    ├── docs/                          # Additional documentation
    ├── reports/                       # Status reports
    └── .git/                          # Git repository
```

---

## 🎯 Key Files Explained

### 🚀 Quick Start
| File | Purpose | When to Use |
|------|---------|-------------|
| `start_app.sh` | Launch the web app | Every time you want to use the system |
| `QUICK_START_GUIDE.md` | Simple usage guide | Learning how to use daily |
| `COMPLETION_REPORT.md` | What was fixed this session | Understanding what changed |

### 📚 Documentation
| File | Purpose | When to Use |
|------|---------|-------------|
| `README.md` | System overview | First time setup, general info |
| `FIXES_AND_IMPROVEMENTS.md` | Technical details | Understanding architecture |
| `SYSTEM_STATUS.md` | Current system state | Checking system health |
| `IMPLEMENTATION_GUIDE.md` | Setup instructions | Initial setup |

### 🎛️ Configuration
| File | Purpose | When to Use |
|------|---------|-------------|
| `.env` | API keys & settings | **NEVER SHARE** - Contains secrets |
| `.env.example` | Template | Setting up on new machine |
| `requirements.txt` | Python packages | Installing dependencies |

### 💻 Application
| File | Purpose | When to Use |
|------|---------|-------------|
| `app.py` | Web interface | Modified by developers only |
| `venv/` | Python environment | Auto-managed by Python |

### 🔧 Tools
| File | Purpose | When to Use |
|------|---------|-------------|
| `ai_client.py` | AI communication | Testing AI connections |
| `service_doc_generator.py` | Doc generation | Core document engine |

### 📊 Data
| File | Purpose | Size | Records |
|------|---------|------|---------|
| `vehicles.json` | Vehicle database | 1.9 MB | 2,270 vehicles |
| `services.json` | Service procedures | 2.1 MB | 780 services |

### 📄 Generated Documents
| Location | Purpose | Format |
|----------|---------|--------|
| `service_docs/` | Cached HTML docs | HTML5 |
| `cache_index.json` | Quick lookup | JSON |
| Organized by: | Make → Model → Year_Service.html | Hierarchical |

---

## 📖 Reading Order for New Users

### First Time Setup
1. Read: `README.md` - Get overview
2. Read: `QUICK_START_GUIDE.md` - Learn basics
3. Run: `start_app.sh` - Launch app
4. Try: Generate first document
5. Reference: `COMPLETION_REPORT.md` - See what's fixed

### Daily Use
1. Run: `start_app.sh`
2. Use: Web interface at http://localhost:8501
3. Reference: `QUICK_START_GUIDE.md` for help

### Troubleshooting
1. Check: `SYSTEM_STATUS.md` - System health
2. Review: `FIXES_AND_IMPROVEMENTS.md` - Technical details
3. Test: `python tools/ai_client.py test`

---

## 🔐 Important Files (DO NOT DELETE)

### Critical Files
- ✅ `.env` - Contains API keys
- ✅ `data/vehicles.json` - Vehicle database
- ✅ `data/services.json` - Service database
- ✅ `tools/ai_client.py` - AI interface
- ✅ `tools/service_doc_generator.py` - Core engine
- ✅ `app.py` - Web interface
- ✅ `requirements.txt` - Dependencies

### Safe to Delete
- ❌ `wip/` - Temporary work files
- ❌ `backups/` - Old backups
- ❌ `__pycache__/` - Python cache (regenerates)
- ❌ `service_docs/` - Cached docs (regenerates)

---

## 📏 File Sizes

### Large Files
- `data/services.json` - 2.1 MB (780 services)
- `data/vehicles.json` - 1.9 MB (2,270 vehicles)
- `venv/` - ~200 MB (Python packages)

### Documentation
- All .md files combined - ~50 KB
- Very lightweight documentation

### Generated Documents
- Each HTML doc - ~10-50 KB
- 1,000 docs ≈ 10-50 MB
- Grows with usage

---

## 🗺️ Navigation Guide

### Want to start using the system?
→ Run `start_app.sh`

### Want to learn how to use it?
→ Read `QUICK_START_GUIDE.md`

### Want technical details?
→ Read `FIXES_AND_IMPROVEMENTS.md`

### Want to check system health?
→ Read `SYSTEM_STATUS.md`

### Want to see what was fixed?
→ Read `COMPLETION_REPORT.md`

### Want to customize settings?
→ Edit `.env`

### Want to add new vehicles/services?
→ Edit `data/vehicles.json` or `data/services.json`

---

## 🔄 File Updates

### Updated This Session
1. `app.py` - Fixed service name field + styling
2. `tools/service_doc_generator.py` - Fixed service lookup
3. `.env` - Added AI configuration
4. `README.md` - Updated statistics

### Created This Session
1. `FIXES_AND_IMPROVEMENTS.md` - Technical documentation
2. `QUICK_START_GUIDE.md` - User guide
3. `SYSTEM_STATUS.md` - Status report
4. `COMPLETION_REPORT.md` - Session summary
5. `FILE_STRUCTURE.md` - This file
6. `start_app.sh` - Quick start script

---

## 💾 Backup Strategy

### What to Backup
1. **Critical:**
   - `.env` (API keys)
   - `data/vehicles.json`
   - `data/services.json`

2. **Important:**
   - `app.py`
   - `tools/*.py`
   - Documentation files

3. **Optional:**
   - `service_docs/` (can regenerate)
   - `venv/` (can reinstall)

### Backup Command
```bash
# Quick backup of critical files
tar -czf backup_$(date +%Y%m%d).tar.gz \
  .env \
  data/ \
  tools/ \
  app.py \
  *.md \
  requirements.txt
```

---

## 📱 Access Points

### Local Access
- URL: `http://localhost:8501`
- Command: `./start_app.sh`

### Network Access
- URL: `http://[YOUR_IP]:8501`
- Find IP: `hostname -I`

### Remote Access (Tailscale)
- URL: `http://[TAILSCALE_IP]:8501`
- Secure, encrypted access

---

## 🎯 Quick Reference

| Task | Command | Location |
|------|---------|----------|
| Start app | `./start_app.sh` | Root directory |
| Test AI | `python tools/ai_client.py test` | tools/ |
| Check data | `ls -lh data/` | data/ |
| View docs | Open http://localhost:8501 | Browser |
| Read guide | `cat QUICK_START_GUIDE.md` | Root directory |

---

**Status:** ✅ All files organized and documented  
**Last Updated:** January 17, 2025  
**Total Files:** 2,000+ (including cached documents)  
**Documentation:** Complete

