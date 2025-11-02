# AI Assistant UI Guide

## Page Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│  💬 AI Service Assistant                                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [Info Box]                                                         │
│  💬 AI Service Assistant                                            │
│  Your intelligent assistant for automotive service docs             │
│                                                                      │
│  What I can do:                                                     │
│  • 🔍 Answer questions about loaded documents                       │
│  • 🔌 Find wiring diagrams (automatically cached)                   │
│  • 📝 Edit documents with verified information                      │
│  • ⚡ Research repair procedures                                     │
│                                                                      │
├─────────────────────────────────────────────────────────────────────┤
│  📄 Select Document to Edit                                         │
│                                                                      │
│  [Dropdown: 2011 Chevrolet Aveo - O2 Sensor...] [📂 Load Document] │
│                                                                      │
│  ▼ Current Document Sections                                        │
│    • Safety                                                         │
│    • Steps                                                          │
│    • Torque Specifications                                          │
│    • Troubleshooting                                                │
│                                                                      │
├─────────────────────────────────────────────────────────────────────┤
│  💬 Chat with Assistant                                             │
│                                                                      │
│  Quick Actions:                                                     │
│  [🔌 Get Wiring] [📋 List Sections] [⚠️ Safety] [🔧 Torque]       │
│                                                                      │
│  Tips:                                                              │
│  💡 Ask: 'What are safety steps?'                                  │
│  🔌 Wiring: 'Show me O2 sensor wiring'                             │
│  📝 Edit: 'Add torque spec: 25 ft-lbs'                            │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 👤 You                                                        │  │
│  │ I need a wiring diagram showing the upstream O2 sensor       │  │
│  │ to the ECM                                                    │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 🤖 Assistant                                                  │  │
│  │ 🔌 Wiring Diagram Information Retrieved                       │  │
│  │                                                                │  │
│  │ Vehicle: 2011 Chevrolet Aveo                                  │  │
│  │ Circuit: Upstream Oxygen Sensor                               │  │
│  │                                                                │  │
│  │ **Component Identification:**                                 │  │
│  │ - Upstream O2 Sensor (Bank 1, Sensor 1)                      │  │
│  │ - Engine Control Module (ECM)                                 │  │
│  │ - Connector C1 at ECM                                         │  │
│  │                                                                │  │
│  │ **Wire Information:**                                         │  │
│  │ - Signal Wire: BLACK (BLK), 18 AWG                           │  │
│  │ - Heater Wire: GRAY (GRY), 16 AWG                            │  │
│  │ - Ground: BLACK/WHITE (BLK/WHT), 18 AWG                      │  │
│  │                                                                │  │
│  │ **Connector Details:**                                        │  │
│  │ - ECM Connector C1, Pin 24 (Signal)                          │  │
│  │ - ECM Connector C1, Pin 25 (Ground)                          │  │
│  │ - ECM Connector C2, Pin 12 (Heater)                          │  │
│  │                                                                │  │
│  │ **Electrical Specifications:**                                │  │
│  │ - Signal Voltage: 0.1-0.9V (fluctuating)                     │  │
│  │ - Heater Voltage: 12V battery                                │  │
│  │ - Signal Resistance: 3-20 ohms                               │  │
│  │ - Heater Resistance: 4-7 ohms                                │  │
│  │                                                                │  │
│  │ ✅ Saved to cache: 2011_Chevrolet_Aveo_upstream_...          │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  [Type your message: wiring, specs, troubleshooting...           ] │
│                                                                      │
├─────────────────────────────────────────────────────────────────────┤
│  📎 Upload Source for Verification (Optional)                       │
│  [Collapsed by default]                                             │
└─────────────────────────────────────────────────────────────────────┘
```

## Sidebar Layout

```
┌──────────────────────────┐
│ 🤖 Assistant Status      │
├──────────────────────────┤
│ ✅ Editing:              │
│ 2011 Chevrolet Aveo...   │
│                          │
├──────────────────────────┤
│ 🔌 Cached Wiring Diagrams│
├──────────────────────────┤
│ 📊 3 diagram(s) cached   │
│                          │
│ ▼ View Cached Diagrams   │
│                          │
│ [📄 2011 Chevrolet...]   │
│ [📄 2022 Honda Accord]   │
│ [📄 2015 Ford F150...]   │
│                          │
├──────────────────────────┤
│ [🔄 Clear Conversation]  │
└──────────────────────────┘
```

## Quick Action Buttons

Visual representation:

```
┌──────────────────────────────────────────────────────────────┐
│  Quick Actions:                                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌────────┐│
│  │🔌 Get       │ │📋 List All  │ │⚠️ Safety    │ │🔧 Torque││
│  │  Wiring Info│ │  Sections   │ │  Info       │ │  Specs  ││
│  └─────────────┘ └─────────────┘ └─────────────┘ └────────┘│
└──────────────────────────────────────────────────────────────┘
```

**What Happens When Clicked:**
- 🔌 **Get Wiring Info** → Triggers: "I need wiring diagram information for this vehicle"
- 📋 **List All Sections** → Triggers: "What sections are in this document?"
- ⚠️ **Safety Info** → Triggers: "What are the safety precautions?"
- 🔧 **Torque Specs** → Triggers: "Show me all torque specifications"

## Chat Input States

### No Document Loaded
```
┌────────────────────────────────────────────────────────────────┐
│ [Load a document first, then ask me anything!               ] │
└────────────────────────────────────────────────────────────────┘
```

### Document Loaded
```
┌────────────────────────────────────────────────────────────────┐
│ [Ask me anything: wiring diagrams, repair steps, specs...   ] │
└────────────────────────────────────────────────────────────────┘
```

## Response Types

### 1. Wiring Diagram Response (New Research)
```
┌──────────────────────────────────────────────────────────────┐
│ 🔌 Wiring Diagram Information Retrieved                      │
│                                                               │
│ Vehicle: [Vehicle Info]                                       │
│ Circuit/System: [Circuit Name]                                │
│                                                               │
│ [Detailed technical information...]                           │
│                                                               │
│ ---                                                           │
│ ✅ Saved to cache: filename.txt                              │
│                                                               │
│ What you can do next:                                         │
│ - Ask follow-up questions                                     │
│ - Say "Add this to troubleshooting"                          │
│ - Request another circuit                                     │
└──────────────────────────────────────────────────────────────┘
```

### 2. Wiring Diagram Response (From Cache)
```
┌──────────────────────────────────────────────────────────────┐
│ 🔌 Wiring Diagram Information (From Cache)                   │
│                                                               │
│ Vehicle: [Vehicle Info]                                       │
│ Circuit/System: [Circuit Name]                                │
│                                                               │
│ [Detailed technical information...]                           │
│                                                               │
│ ---                                                           │
│ ✅ Previously cached: filename.txt                           │
│                                                               │
│ What you can do:                                              │
│ - Ask specific questions                                      │
│ - Request to add to service document                          │
└──────────────────────────────────────────────────────────────┘
```

### 3. Question Answer
```
┌──────────────────────────────────────────────────────────────┐
│ [Direct answer to user's question]                            │
│                                                               │
│ Based on the [Section Name] section:                          │
│ [Specific answer with details]                                │
└──────────────────────────────────────────────────────────────┘
```

### 4. Edit Verification
```
┌──────────────────────────────────────────────────────────────┐
│ ✅ Verification Passed (confidence: 95%)                      │
│                                                               │
│ Information to add:                                           │
│ [What will be added]                                          │
│                                                               │
│ Target section: [Section Name]                                │
│                                                               │
│ Verification summary:                                         │
│ [Why this is accurate]                                        │
│                                                               │
│ Sources: [List of sources]                                    │
│                                                               │
│ Reply with:                                                   │
│ - "add it" or "yes" to confirm                               │
│ - "no" or "cancel" to cancel                                 │
└──────────────────────────────────────────────────────────────┘
```

## Color Scheme

### Status Indicators
- ✅ Green: Success, loaded, verified
- ⚠️ Yellow: Warning, pending, uncertain
- ❌ Red: Error, failed, blocked
- 🔌 Blue: Wiring/electrical
- 💡 Blue: Tips and info
- 📋 Gray: Neutral information

### Button States
- **Primary Action**: Blue background
- **Secondary Action**: Gray background
- **Quick Actions**: White background, colored icon

## User Flow Examples

### Flow 1: First-Time Wiring Lookup

```
1. User loads document
   ↓
2. Sees Quick Actions buttons
   ↓
3. Clicks [🔌 Get Wiring Info] OR types question
   ↓
4. Spinner appears: "🤔 Analyzing and verifying..."
   ↓
5. Response appears with detailed wiring info
   ↓
6. File saved notification
   ↓
7. Sidebar shows "1 diagram(s) cached"
   ↓
8. User can ask follow-up questions
```

### Flow 2: Cached Wiring Lookup

```
1. User asks about previously researched circuit
   ↓
2. Brief spinner: <1 second
   ↓
3. Response appears instantly
   ↓
4. Note: "(From Cache)"
   ↓
5. No API cost, instant results
```

### Flow 3: Document Question

```
1. User types or clicks quick action
   ↓
2. Brief spinner: 2-5 seconds
   ↓
3. Response with document content
   ↓
4. Cites specific sections
   ↓
5. User can ask follow-ups
```

## Mobile Responsiveness

### On Small Screens
- Quick Action buttons stack vertically
- Tips collapse to single column
- Chat messages full width
- Sidebar becomes collapsible menu

### On Touch Devices
- Larger tap targets for buttons
- Swipe gestures for sidebar
- Touch-friendly scrolling

## Accessibility Features

### Screen Readers
- Proper ARIA labels on all buttons
- Alt text for icons
- Semantic HTML structure

### Keyboard Navigation
- Tab through interactive elements
- Enter to activate buttons
- Escape to close modals

### Visual
- High contrast text
- Clear focus indicators
- Readable font sizes

## Pro Tips for UI

### Tip 1: Use Quick Actions First
New users should start with Quick Action buttons to see what's possible

### Tip 2: Check Sidebar for Cache
Before asking for wiring, check sidebar to see if it's already cached

### Tip 3: Clear, Specific Questions
Better results with: "What's the oil drain plug torque?" vs "torque?"

### Tip 4: Follow-up Questions
After getting info, ask specific follow-ups for details

### Tip 5: Use Document Context
Load the right document first for best answers

## Common UI States

### Loading State
```
🤔 Analyzing and verifying...
```

### Success State
```
✅ [Success message]
```

### Error State
```
❌ [Error message with suggestions]
```

### Info State
```
💡 [Helpful information]
```

### Warning State
```
⚠️ [Warning or caution]
```

## Summary

The UI is designed to be:
- **Intuitive**: Quick actions for common tasks
- **Informative**: Clear status and feedback
- **Efficient**: Fast access to cached information
- **Helpful**: Tips and examples throughout
- **Accessible**: Works for all users

Key UI innovations:
1. Quick Action buttons (new!)
2. Wiring diagram sidebar browser (new!)
3. Context-aware prompts (improved!)
4. Clear status indicators (improved!)
5. Better response formatting (improved!)
