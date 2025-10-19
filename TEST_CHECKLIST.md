# AI Assistant - Test Checklist

## Quick Test (5 minutes) ⚡

### Setup
- [ ] Open terminal
- [ ] `cd /home/eanhd/projects/vehicles`
- [ ] `source venv/bin/activate`
- [ ] `streamlit run app.py`
- [ ] App opens in browser

### Basic Test
- [ ] Go to "💬 AI Assistant" tab
- [ ] See Quick Action buttons (🔌 Get Wiring, 📋 List Sections, etc.)
- [ ] Select document from dropdown
- [ ] Click "📂 Load Document"
- [ ] See "✅ Editing: [document name]" in sidebar

### Wiring Diagram Test
- [ ] Type: "I need wiring for the upstream O2 sensor to the ECM"
- [ ] See "🤔 Analyzing and verifying..." spinner
- [ ] Wait 10-15 seconds
- [ ] See detailed wiring information with:
  - [ ] Wire colors (BLACK, GRAY, etc.)
  - [ ] ECM connector and pin numbers
  - [ ] Voltage specifications
  - [ ] Component locations
  - [ ] Testing procedures
- [ ] See "✅ Saved to cache: [filename]" at bottom
- [ ] Check sidebar shows "1 diagram(s) cached"

### Cached Lookup Test
- [ ] Ask same question again: "Show me the upstream O2 sensor wiring"
- [ ] Response is INSTANT (<1 second)
- [ ] Response shows "(From Cache)"
- [ ] Same detailed information displayed

### Quick Actions Test
- [ ] Click [🔧 Torque Specs] button
- [ ] See list of torque specifications from document
- [ ] Click [📋 List All Sections] button
- [ ] See list of document sections

### Sidebar Test
- [ ] Check "🔌 Cached Wiring Diagrams" section in sidebar
- [ ] Click "View Cached Diagrams" expander
- [ ] See your cached diagram listed
- [ ] Click on cached diagram
- [ ] See full wiring information displayed

## ✅ Success Criteria

All items above should work. If they do:
🎉 **AI Assistant is now excellent!**

## ❌ If Something Doesn't Work

### "No cached documents available"
→ Go to "🔍 Generate Service Doc" tab first
→ Generate or browse for a document
→ Then come back to AI Assistant

### Wiring lookup fails
→ Check your .env file has API keys:
   - RESEARCH_AI_PROVIDER=perplexity
   - PERPLEXITY_API_KEY=your_key
→ Check internet connection
→ Try a different circuit name

### Sidebar doesn't show cached diagrams
→ Check `/home/eanhd/projects/vehicles/wiring_diagrams/` exists
→ Check files end with `.txt`
→ Refresh page (F5)

### Response is slow
→ First lookup takes 10-15 seconds (normal - it's researching!)
→ Cached lookups should be instant
→ Check API key is valid

## 💡 Next Steps After Testing

Once basic test works:
1. Try different wiring requests:
   - "Show me fuel pump circuit wiring"
   - "I need starter motor wiring"
   - "What's the cooling fan circuit?"

2. Test follow-up questions:
   - "What wire color is pin 3?"
   - "Where is this connector located?"
   - "What voltage should I see?"

3. Test document questions:
   - "What are the safety precautions?"
   - "What tools are needed?"
   - "Show me the procedure steps"

4. Browse cached diagrams:
   - Accumulate 3-5 cached diagrams
   - Use sidebar to quickly access them
   - Note how instant cached lookups are

## 📊 What You Should Notice

### Speed
- First wiring lookup: 10-15 seconds ⏱️
- Cached wiring lookup: <1 second ⚡
- Document questions: 2-5 seconds 🔄

### Quality
- Detailed technical information ✅
- Wire colors, connector pins, voltages ✅
- Testing procedures and locations ✅
- Context-aware answers ✅

### Cost
- First lookup: ~$0.015 💰
- Cached lookup: $0.00 🆓
- Very affordable! 💚

### Usability
- Quick Action buttons are intuitive ✅
- Natural language works well ✅
- Sidebar shows cached diagrams ✅
- Clear status and feedback ✅

## 🎯 The Big Win

**Before:** "The document doesn't include that..." ❌
**After:** [Comprehensive wiring information] ✅

The assistant now ACTUALLY HELPS! 🎉
