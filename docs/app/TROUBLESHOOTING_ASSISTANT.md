# Troubleshooting - AI Assistant

## Common Issues & Fixes

### Issue: SyntaxError on startup
**Symptom:** Error mentions `doc_editor_assistant.py` with syntax error
**Cause:** Python is using old cached bytecode files (.pyc)

**Fix:**
```bash
cd /home/eanhd/projects/vehicles
rm -rf tools/__pycache__/*.pyc
rm -rf __pycache__/*.pyc
```
Then restart the app.

### Issue: Import errors
**Symptom:** "ModuleNotFoundError: No module named 'ai_client'"
**Cause:** Not running from correct directory or venv not activated

**Fix:**
```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
streamlit run app.py
```

### Issue: Wiring lookup fails
**Symptom:** Error message when asking for wiring diagrams
**Causes:**
- API keys not configured
- Internet connection
- Rate limits

**Fixes:**
1. Check `.env` file exists with:
   ```
   RESEARCH_AI_PROVIDER=perplexity
   PERPLEXITY_API_KEY=your_actual_key_here
   FORMATTER_AI_PROVIDER=openai
   OPENAI_API_KEY=your_actual_key_here
   ```

2. Test API key:
   ```bash
   source venv/bin/activate
   python3 -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Perplexity:', os.getenv('PERPLEXITY_API_KEY')[:10]+'...')"
   ```

3. Check internet: `ping -c 1 google.com`

### Issue: Cached diagrams don't show in sidebar
**Symptom:** Sidebar says "No wiring diagrams cached yet"
**Causes:**
- Directory doesn't exist
- No diagrams have been researched yet
- Files have wrong extension

**Fixes:**
1. Create directory: `mkdir -p wiring_diagrams`
2. Research a wiring diagram first
3. Check files exist: `ls -la wiring_diagrams/`
4. Refresh page (F5)

### Issue: Quick Actions don't work
**Symptom:** Buttons don't respond or give errors
**Cause:** No document loaded

**Fix:**
1. Select document from dropdown
2. Click "📂 Load Document"
3. Wait for confirmation
4. Then try Quick Actions

### Issue: Response is slow
**Symptom:** Takes 30+ seconds to respond
**Causes:**
- First-time wiring lookup (normal - it's researching!)
- API rate limits
- Network issues

**Expected Times:**
- First wiring lookup: 10-15 seconds ✅
- Cached wiring: <1 second ✅
- Document questions: 2-5 seconds ✅

**If slower than above:**
- Check internet speed
- Verify API key is valid
- Try again in a few minutes (rate limits)

### Issue: "No cached documents available"
**Symptom:** Can't load any documents in AI Assistant
**Cause:** No documents generated yet

**Fix:**
1. Go to "🔍 Generate Service Doc" tab
2. Generate a document OR
3. Go to "📚 Browse Cache" and use existing doc
4. Return to AI Assistant

### Issue: Wrong vehicle information in response
**Symptom:** AI responds about different vehicle
**Cause:** Document loaded is different than expected

**Fix:**
1. Check sidebar "🤖 Assistant Status"
2. Verify correct document is loaded
3. Load correct document if needed
4. Ask question again

## Quick Reset

If something is really broken:

```bash
cd /home/eanhd/projects/vehicles

# Clear all caches
rm -rf tools/__pycache__
rm -rf __pycache__
rm -rf .streamlit

# Restart venv
deactivate 2>/dev/null
source venv/bin/activate

# Restart app
streamlit run app.py
```

## Still Having Issues?

1. Check documentation:
   - README_AI_ASSISTANT.md - Quick overview
   - QUICK_START_AI_ASSISTANT.md - Usage guide
   - TEST_CHECKLIST.md - Testing guide

2. Verify files are correct:
   ```bash
   ls -la tools/doc_editor_assistant.py
   ls -la app.py
   ls -la wiring_diagrams/
   ```

3. Test basic import:
   ```bash
   cd /home/eanhd/projects/vehicles
   source venv/bin/activate
   python3 -c "import sys; sys.path.insert(0, 'tools'); from doc_editor_assistant import DocumentEditorAssistant; print('OK')"
   ```

4. Check Streamlit logs in terminal for specific errors

## Error Messages Explained

### "Please select a document first"
→ Load a document before using assistant

### "Could not understand the information to add"
→ Rephrase your edit request more clearly

### "Verification Uncertain" or "Verification Failed"
→ AI couldn't verify the information
→ Upload a source document for verification

### "No pending edits to confirm"
→ Nothing to confirm
→ Make an edit first, then confirm

### Rate limit errors
→ Too many API calls too quickly
→ Wait a few minutes and try again

## Performance Tips

1. **Use cached lookups**: Ask for same circuit twice to see instant response
2. **Be specific**: "upstream O2 sensor" not just "sensor"
3. **Check sidebar first**: See if wiring already cached
4. **Quick Actions**: Use buttons for common tasks
5. **Load right document**: Context matters for answers

## Success Indicators

✅ Sidebar shows loaded document
✅ Quick Actions visible above chat
✅ Wiring lookups return detailed info in 10-15s
✅ Cached lookups are instant
✅ Sidebar shows cached diagrams count
✅ Follow-up questions work

If all above work: **Everything is excellent!** 🎉
