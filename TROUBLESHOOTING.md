# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 1. App Won't Start - "Port 8501 is already in use"

**Problem**: Another Streamlit instance is already running on port 8501

**Solution**:
```bash
# Kill existing Streamlit processes
pkill -f streamlit

# Wait a moment
sleep 2

# Start the app again
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

---

### 2. "FileNotFoundError: vehicles.json"

**Problem**: Path issues when loading database files

**Status**: ✅ FIXED as of Jan 17, 2025

**What Was Done**:
- Updated all files to use absolute paths
- Files fixed: `tools/service_doc_generator.py`, `research_tools/service_doc_generator.py`
- Now works regardless of current working directory

**If Still Happening**:
```bash
# Verify files exist
ls -lh data/vehicles.json
ls -lh data/services.json

# Should show:
# data/vehicles.json  (1.9M)
# data/services.json  (92K)
```

---

### 3. "ModuleNotFoundError: No module named 'dotenv'"

**Problem**: Missing Python dependencies

**Solution**:
```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
pip install -r requirements.txt
```

---

### 4. API Key Errors

**Problem**: "Invalid API key" or "API key not found"

**Check Your .env File**:
```bash
cat .env

# Should contain (with your actual keys):
PERPLEXITY_API_KEY=pplx-xxxxx...
OPENAI_API_KEY=sk-xxxxx...
ANTHROPIC_API_KEY=sk-ant-xxxxx...
```

**If Keys Are Missing**:
1. Copy `.env.example` to `.env`
2. Add your actual API keys
3. Restart the app

```bash
cp .env.example .env
nano .env  # Edit and add your keys
```

---

### 5. App Loads But Dropdowns Are Empty

**Problem**: Database files not loading correctly

**Check Database Loading**:
```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
python3 -c "
from tools.service_doc_generator import ServiceDocGenerator
gen = ServiceDocGenerator()
print(f'Vehicles: {len(gen.vehicles)}')
print(f'Services: {len(gen.services)}')
"

# Should show:
# Vehicles: 2270
# Services: 153
```

---

### 6. Slow Document Generation

**Possible Causes**:
1. **First time generating** - Normal! AI needs to research (10-30 seconds)
2. **Slow internet** - Perplexity needs to search the web
3. **API rate limiting** - Wait a minute and try again

**Normal Speeds**:
- First generation: 10-30 seconds
- Cached documents: < 1 second
- Chat updates: 5-15 seconds

---

### 7. Can't Access From Other Devices

**Problem**: Can't reach http://172.31.17.60:8501 from phone/tablet

**Solutions**:

1. **Check Firewall**:
```bash
# Allow port 8501 through firewall
sudo ufw allow 8501/tcp
```

2. **Verify App Is Running**:
```bash
curl http://localhost:8501/_stcore/health
# Should return: ok
```

3. **Check If Listening on All Interfaces**:
```bash
netstat -tlnp | grep 8501
# Look for 0.0.0.0:8501 or :::8501
```

4. **Try Different IP**:
```bash
# Get all IPs
hostname -I

# Try each one in your browser:
# http://<ip>:8501
```

---

### 8. HTML Documents Look Broken

**Problem**: Generated HTML doesn't display correctly

**Possible Causes**:
1. Formatter AI had an error
2. Incomplete response from AI
3. HTML parsing issue

**Solution**:
```bash
# Regenerate the document (click "Generate" again)
# Or clear the cache and regenerate

cd /home/eanhd/projects/vehicles
rm -rf service_docs/cache_index.json
```

---

### 9. Virtual Environment Issues

**Problem**: Commands fail with "command not found" or module errors

**Solution**:
```bash
# Always activate virtual environment first
cd /home/eanhd/projects/vehicles
source venv/bin/activate

# Your prompt should show (venv) at the beginning
# If not, something is wrong with venv

# Recreate venv if needed
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 10. App Crashes or Freezes

**Problem**: Streamlit app stops responding

**Solution**:
```bash
# Stop the app
pkill -f streamlit

# Check for errors in terminal where app was running
# Look for Python tracebacks or error messages

# Restart with verbose logging
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py --logger.level=debug
```

---

## Verifying System Health

### Quick Health Check Script

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate

echo "=== SYSTEM HEALTH CHECK ==="
echo ""

echo "✓ Virtual Environment:"
which python
echo ""

echo "✓ Database Files:"
ls -lh data/*.json
echo ""

echo "✓ Python Dependencies:"
pip list | grep -E "streamlit|dotenv|requests"
echo ""

echo "✓ API Keys:"
grep -E "PERPLEXITY|OPENAI|ANTHROPIC" .env | sed 's/=.*/=***/' 
echo ""

echo "✓ App Status:"
curl -s http://localhost:8501/_stcore/health
echo ""

echo "✓ Generator Test:"
python3 -c "from tools.service_doc_generator import ServiceDocGenerator; g=ServiceDocGenerator(); print(f'{len(g.vehicles)} vehicles, {len(g.services)} services')"
echo ""

echo "=== END HEALTH CHECK ==="
```

---

## Getting Detailed Logs

### View Streamlit Logs
```bash
# Run app in foreground to see logs
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py

# Logs will appear in terminal
# Press Ctrl+C to stop
```

### Python Error Logs
```bash
# Test the generator directly
cd /home/eanhd/projects/vehicles
source venv/bin/activate

python3 -c "
from tools.service_doc_generator import ServiceDocGenerator
import traceback

try:
    gen = ServiceDocGenerator()
    print('✓ Generator initialized successfully')
    print(f'✓ Loaded {len(gen.vehicles)} vehicles')
    print(f'✓ Loaded {len(gen.services)} services')
except Exception as e:
    print('✗ Error initializing generator:')
    traceback.print_exc()
"
```

---

## System Requirements Check

### Verify Installation
```bash
# Python version (should be 3.8+)
python3 --version

# pip version
pip --version

# Check if venv is working
which python
# Should show: /home/eanhd/projects/vehicles/venv/bin/python
```

### Disk Space
```bash
# Check available disk space
df -h .

# Check service_docs cache size
du -sh service_docs/
```

---

## When All Else Fails

### Nuclear Option - Complete Reset

```bash
cd /home/eanhd/projects/vehicles

# 1. Stop everything
pkill -f streamlit

# 2. Backup your .env file
cp .env .env.backup

# 3. Remove virtual environment
rm -rf venv

# 4. Remove cache
rm -rf service_docs/

# 5. Recreate everything
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 6. Restore .env
cp .env.backup .env

# 7. Start fresh
streamlit run app.py
```

---

## Still Need Help?

### Check These Files
1. `README.md` - Full documentation
2. `QUICK_START.md` - Setup guide
3. `CURRENT_STATUS.md` - System overview
4. `ACCESS_INFO.md` - How to access the app

### Verify Your Setup
```bash
cd /home/eanhd/projects/vehicles

# Run comprehensive test
source venv/bin/activate
python3 << 'EOF'
print("=" * 70)
print("COMPREHENSIVE SYSTEM TEST")
print("=" * 70)

import sys
import os
from pathlib import Path

# Test 1: Check Python version
print(f"\n✓ Python version: {sys.version}")

# Test 2: Check working directory
print(f"✓ Working directory: {os.getcwd()}")

# Test 3: Check data files
print(f"✓ vehicles.json exists: {Path('data/vehicles.json').exists()}")
print(f"✓ services.json exists: {Path('data/services.json').exists()}")

# Test 4: Import modules
try:
    from tools.service_doc_generator import ServiceDocGenerator
    print("✓ Can import ServiceDocGenerator")
except Exception as e:
    print(f"✗ Import failed: {e}")

# Test 5: Initialize generator
try:
    gen = ServiceDocGenerator()
    print(f"✓ Generator initialized: {len(gen.vehicles)} vehicles, {len(gen.services)} services")
except Exception as e:
    print(f"✗ Initialization failed: {e}")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
EOF
```

---

## Emergency Contact Info

If you're completely stuck:

1. **Save your .env file** (has your API keys)
2. **Note what you were trying to do** when it broke
3. **Copy any error messages** from the terminal
4. **Check the files** listed in this troubleshooting guide

Remember: The database files in `data/` and your `.env` file are the most important. Everything else can be regenerated!
