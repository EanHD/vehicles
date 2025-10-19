# Quick Reference: Wiring Diagram Assistant

**🔌 Fast access to electrical circuit information**

---

## 💬 How to Request

Simply type in the AI Assistant chat:

```
"Find wiring diagram for [circuit/system]"
"Get [system] wiring schematic"
"Show me [component] wiring"
"I need electrical info for [circuit]"
```

---

## 🎯 Common Requests

### Starting & Charging
```
"starter circuit wiring"
"alternator wiring diagram"
"charging system schematic"
"battery disconnect circuit"
```

### Fuel System
```
"fuel pump wiring"
"fuel injector circuit"
"fuel pressure sensor wiring"
```

### HVAC
```
"AC compressor clutch wiring"
"blower motor circuit"
"HVAC controls wiring"
"cooling fan circuit"
```

### Lighting
```
"headlight wiring diagram"
"tail light circuit"
"brake light wiring"
"turn signal circuit"
```

### Body Electronics
```
"power window wiring"
"door lock circuit"
"BCM wiring diagram"
"radio harness pinout"
```

### Safety Systems
```
"ABS wiring diagram"
"airbag system circuit"
"SRS module wiring"
```

### Engine Management
```
"ECM/PCM wiring"
"ignition coil circuit"
"oxygen sensor wiring"
"MAF sensor circuit"
```

---

## 📋 What You Get

Every wiring diagram request provides:

✅ **Wire Colors & Gauges** - Exact wire specifications  
✅ **Connector Info** - Types, locations, part numbers  
✅ **Pin Assignments** - Complete pinout data  
✅ **Voltage Specs** - Expected voltage ranges  
✅ **Testing Points** - Where to measure  
✅ **Component Locations** - Where to find parts  
✅ **Common Issues** - Known failure modes  
✅ **TSB References** - Related technical bulletins  

---

## 💾 Automatic Caching

All wiring info is saved to:
```
wiring_diagrams/{Year}_{Make}_{Model}_{Circuit}_wiring.txt
```

**Example:**
```
wiring_diagrams/2020_Toyota_Camry_starter_wiring.txt
```

---

## 🚀 Workflow

1. **Load a service document** in AI Assistant
2. **Request wiring info** for specific circuit
3. **AI researches** and compiles information
4. **Review** technical details
5. **Info auto-saved** to cache
6. **Add to document** if needed

---

## 💡 Pro Tips

### Get Better Results
- Be specific about the circuit/system
- Include component name if possible
- Mention year/make/model for accuracy

### Good Requests
✅ "starter motor circuit wiring"  
✅ "alternator charging system diagram"  
✅ "AC compressor clutch relay circuit"  

### Vague Requests
❌ "wiring diagram"  
❌ "electrical stuff"  
❌ "show me wires"  

---

## 📎 Upload Sources

For best accuracy:
1. Request AI research first
2. Upload your actual diagram if available
3. AI will cross-reference and enhance info

**Supported uploads:**
- URL to OEM diagrams
- PDF service manual pages
- Text copied from FSM
- (Coming soon: Image/screenshot OCR)

---

## 🔍 Example Response

**Request:** "Find wiring diagram for starter circuit"

**AI Response:**
```
🔌 WIRING DIAGRAM INFORMATION

Vehicle: 2020 Toyota Camry
Circuit/System: Starter

WIRE COLORS & CONNECTIONS:
• Starter motor B+ terminal: Red 8GA from battery
• Starter solenoid S terminal: Yellow/Black 18GA from ignition
• Ground: Black 8GA to engine block
• Park/Neutral switch: Green/Yellow 20GA

CONNECTOR LOCATIONS:
• C101: Behind starter motor (3-pin)
• C201: Firewall junction box
• G101: Engine block ground point

PIN ASSIGNMENTS:
C101 Connector:
• Pin 1: B+ (Red, 8GA)
• Pin 2: S terminal (Yellow/Black, 18GA)
• Pin 3: Ground (Black, 8GA)

VOLTAGE SPECS:
• B+ terminal: 12V constant
• S terminal: 12V when cranking
• Ground: <0.1V resistance to battery negative

TESTING POINTS:
1. Check B+ voltage at starter (should be 12V+)
2. Check S terminal during crank (should be 12V)
3. Check ground resistance (<0.5 ohms)
4. Verify park/neutral switch continuity

COMMON ISSUES:
• Corroded B+ terminal connection
• Failed park/neutral switch
• Worn starter solenoid contacts
• High resistance ground connection

TSB REFERENCES:
• TSB-EL-001: Starter relay issues
• TSB-EL-015: Ground connection corrosion

✅ Saved to cache: 2020_Toyota_Camry_starter_wiring.txt
```

---

## 🎯 Quick Actions Button

Click **🔌 Get Wiring Diagram** in AI Assistant to:
- See this quick reference
- Get prompted for circuit type
- Access help and examples

---

## 📊 Cost

**Per wiring diagram request:** ~$0.0005-0.001  
**Cached results:** $0 (reuse saved info)  

Very affordable for shop use!

---

## ❓ Need Help?

**Assistant not understanding?**
- Be more specific about circuit
- Include system name (starter, alternator, etc.)

**Information seems wrong?**
- Upload a source document for verification
- Specify exact year/model/engine variant

**Can't find what you need?**
- Try different search terms
- Upload actual diagram for AI to analyze

---

**Updated:** October 18, 2024  
**Version:** 2.1.0
