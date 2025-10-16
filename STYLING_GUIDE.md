# Swoop Service Auto - Professional Styling Guide
**Version**: 3.0 - ALLDATA-Inspired Professional Design  
**Last Updated**: October 15, 2025

## 🎨 Design Philosophy

### Core Principles
1. **Professional Industrial Aesthetic**: Inspired by ALLDATA and professional automotive service manuals
2. **High Contrast Black & White**: Sharp, clean, easy to read in any environment
3. **Minimal Color**: Only red for critical accents (warnings, brand)
4. **Information Dense**: Maximum info with clean hierarchy
5. **Print-Ready**: Clean black & white for professional printing
6. **Mechanical Focus**: Designed for mechanics, not consumers

---

## 🎯 Color Palette

### Primary Colors (Monochrome Professional)
```css
Black (Headers/Accents):          #000000
Dark Gray (Borders):              #333333
Medium Gray (Text):               #666666
Light Gray (Backgrounds):         #f0f0f0, #f8f8f8
White (Content):                  #ffffff
Page Background:                  #d0d0d0
```

### Accent Colors (Minimal Use Only)
```css
/* Critical/Brand */
Red (Warnings/Brand):             #cc0000

/* Highlights (Sparingly) */
Warning Background:               #ffcccc
Info/Caution Background:          #ffffcc
Success Background:               #e6f7e6
```

### Text Colors
```css
Primary Text:                     #000000
Secondary Text:                   #333333
Tertiary/Meta Text:               #666666
Light Text (on dark):             #cccccc
```

---

## 📐 Typography

### Font Stack
```css
font-family: 'Arial', 'Helvetica', sans-serif;
/* Simple, clean, professional - no fancy fonts */
```

### Hierarchy
```css
Page Title (h1):                 22px, 700 weight, 0.5px spacing, UPPERCASE
Section Headers (h2):            14px, 700 weight, UPPERCASE, 0.5px spacing
Subsection Headers (h3):         13px, 700 weight, UPPERCASE, 0.5px spacing
Body Text:                       13px, 400 weight, 1.5 line-height
Labels:                          10px, 700 weight, UPPERCASE, 0.5px spacing
Meta Info:                       11px, 600 weight, UPPERCASE
```

---

## 🏗️ Component Styles

### Header
```css
Background: #000000 (solid black)
Border: 3px solid #cc0000 (bottom, red accent)
Padding: 20px 25px
Text: White, bold, uppercase
```

### Vehicle Info Box
```css
Background: #f8f8f8 (light gray)
Border: 2px solid #333333
Header: #333333 background bar with white text
Labels: Black, uppercase, 10px
Values: #333333, underlined
```

### Service Overview
```css
Background: #ffffcc (pale yellow - caution color)
Border: 2px solid #000000
Border-Left: 5px solid #cc0000 (red accent)
Header: Black, uppercase, 14px
```

### Procedure Steps
```css
Background: #ffffff (white)
Border: 1px solid #666666
Border-Left: 4px solid #000000 (emphasis)
Number Badge: #000000 background, 28x28px, white text
Text: 13px, black
Meta: 11px, #666666, uppercase
```

### Torque Specs
```css
Background: #f0f0f0
Border: 1px solid #666666
Component: #000000, 12px, bold
Value: #cc0000 (red), 13px, bold, Courier New (monospace)
```

### Warnings
```css
Background: #ffcccc (light red)
Border: 2px solid #cc0000
Border-Left: 5px solid #cc0000
Icon: #cc0000 background badge
```

### Tips
```css
Background: #e6f7e6 (light green)
Border: 1px solid #00aa00
Border-Left: 4px solid #00aa00
Icon: #00aa00 background badge
```

### Parts List
```css
Background: Alternating #f9f9f9 and #ffffff
Border: 1px solid #666666
Checkbox: 16x16px
Name: #000000, 12px, bold
Part Number: #666666, 11px, Courier New (monospace)
```

### Footer
```css
Background: #000000 (black)
Color: #cccccc (light gray)
Border: 3px solid #cc0000 (top)
Watermark: #999999, uppercase, 10px
Citations: #909090, 10px
Links: #ff6666 (red tint)
```

---

## 📋 Layout Structure

### Container
```css
Max-width: 950px
Background: White
Border: 1px solid #000000
Box-shadow: 0 2px 8px rgba(0,0,0,0.3)
No border-radius (sharp corners)
```

### Content Area
```css
Padding: 25px
Background: #ffffff
```

### Sections
```css
Background: White
Border: 1px solid #999999
Padding: 15px
Margin-bottom: 20px
No border-radius (sharp professional edges)
```

---

## 🖼️ Diagram Placeholders

### Style
```css
Background: #f0f0f0
Border: 2px dashed #666666
Padding: 30px 15px
Text-align: Center
Color: #666666
```

### SVG Icon
```css
Size: 48x48px
Stroke: currentColor
Opacity: 0.4
```

### Text
```css
Title: 12px, 700 weight, #333333, uppercase
Note: 10px, italic, #666666
```

---

## 📱 Responsive & Print

### Mobile (≤ 600px)
```css
body padding: 5px
content padding: 15px
header padding: 15px
info-grid: Single column
```

### Print
```css
body background: White
container: 1px solid #000000, no shadow
page-break-inside: avoid (for steps)
Black and white optimized
```

### Dark Mode
```css
body background: #1a1a1a
container: #2c2c2c, border #666666
sections: #333333, border #555555
text: #e0e0e0
headings: #ffffff
Maintains professional appearance in dark mode
```

---

## 🎨 Design Comparison

### OLD STYLE (v2.0) - Too Soft/Colorful
- Gradient backgrounds (#2c2c2c to #1a1a1a)
- Rounded corners (border-radius: 4px)
- Multiple accent colors (red, amber, green)
- Softer borders and shadows
- Segoe UI font
- Larger padding and spacing

### NEW STYLE (v3.0) - Professional/Industrial
- Solid black/white (#000000, #ffffff)
- Sharp corners (no border-radius)
- Minimal color (black, white, red accent only)
- Strong borders and structure
- Arial/Helvetica font
- Tighter, information-dense layout
- Uppercase labels and headers
- ALLDATA-inspired aesthetics

---

## ✏️ Key Improvements

1. **Removed "Soft" Elements**
   - No gradients
   - No rounded corners
   - No soft colors
   - Eliminated unnecessary spacing

2. **Increased Professionalism**
   - Black and white focus
   - Sharp, defined borders
   - Industrial typography
   - Uppercase headers and labels

3. **Better Print Appearance**
   - High contrast black/white
   - Clean borders for printing
   - Monospace fonts for specs

4. **More Mechanical Feel**
   - Resembles ALLDATA and Mitchell1
   - Technical manual aesthetic
   - Workshop-appropriate design

---

## 🔧 CSS Classes Reference

### Structure
- `.container` - Main wrapper (black border)
- `.header` - Top banner (black background)
- `.content` - Main content area (white)
- `.footer` - Bottom section (black background)

### Information Boxes
- `.vehicle-info` - Gray vehicle details box
- `.service-overview` - Yellow service details box
- `.section` - White content sections

### Content Elements
- `.info-grid` - Responsive grid layout
- `.info-item` - Individual info field
- `.info-label` - Field label (black, uppercase, 10px)
- `.info-value` - Field value (underlined)

### Procedure
- `.procedure-step` - Individual step container
- `.step-number` - Black numbered badge
- `.step-description` - Step text
- `.step-meta` - Time/torque metadata (uppercase)

### Specifications
- `.torque-spec` - Torque specification row
- `.torque-component` - Component name
- `.torque-value` - Torque value (red, monospace)

### Parts & Tools
- `.parts-list` - Parts container
- `.part-item` - Individual part row (striped)
- `.part-name` - Part name
- `.part-number` - OEM number (monospace)

### Messages
- `.warning` - Critical warning box (red)
- `.warning-icon` - Warning badge
- `.tip` - Pro tip box (green)
- `.tip-icon` - Tip badge

### Diagrams
- `.diagram-placeholder` - Diagram placeholder box
- `.diagram-title` - Diagram heading (uppercase)
- `.diagram-note` - Reference note

### Footer
- `.watermark` - Generator info (uppercase)
- `.citations` - Source references

---

## 📸 Design Mockup

### Layout Flow
```
┌─────────────────────────────────────┐
│ [BLACK HEADER] SWOOP SERVICE AUTO   │ ← Black bg, red bottom border
│ PROFESSIONAL AUTOMOTIVE SERVICE     │
├─────────────────────────────────────┤
│ ┌─────────────────────────────────┐ │
│ │ [VEHICLE SPEC - Gray Box]       │ │ ← #f8f8f8, black borders
│ │ YEAR: 2015 | MAKE: TOYOTA       │ │
│ └─────────────────────────────────┘ │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ [SERVICE - Yellow Box]          │ │ ← #ffffcc, black borders
│ │ BRAKE PADS REPLACEMENT          │ │
│ └─────────────────────────────────┘ │
│                                     │
│ ⚠️ SAFETY WARNINGS                  │
│ [Red boxes with black borders]     │
│                                     │
│ 📋 STEP-BY-STEP PROCEDURE           │
│ [1] White boxes, black left border │
│ [2] Black number badges            │
│                                     │
│ 🔧 TORQUE SPECIFICATIONS            │
│ [Gray boxes with red values]       │
│                                     │
│ 💡 PRO TIPS                         │
│ [Green boxes with black borders]   │
├─────────────────────────────────────┤
│ [BLACK FOOTER]                     │ ← Black bg, red top border
│ GENERATED BY SWOOP SERVICE AUTO    │
│ Sources: [links]                   │
└─────────────────────────────────────┘
```

---

## 🚀 Quick Start

### For Developers
```bash
# Regenerate with new professional styles
cd /home/eanhd/projects/vehicles
source venv/bin/activate
python3 -c "
from tools.service_doc_generator import ServiceDocGenerator
gen = ServiceDocGenerator()
gen.generate(year=2015, make='Toyota', model='Camry', 
             service='Brake Pads Replacement (Front)', 
             force_regenerate=True)
"
```

### For Designers
1. Edit CSS in `tools/service_doc_generator.py` (lines 320-670)
2. Test with force regenerate
3. Check browser preview AND print preview
4. Verify professional appearance
5. Test in light and dark modes

---

## 📚 Resources

- **HTML Files**: `service_docs/{Make}/{Model}/{Year}_{Service}.html`
- **Generator**: `tools/service_doc_generator.py`
- **App UI**: `app.py`
- **Streamlit**: http://localhost:8501

---

## 🎯 Design Goals Achieved

✅ **Professional Industrial Look** - Black/white with minimal color  
✅ **High Contrast** - Easy to read in any lighting  
✅ **Sharp/Clean** - No soft edges or gradients  
✅ **Print-Ready** - Perfect black & white prints  
✅ **Mechanic-Friendly** - Technical manual aesthetic  
✅ **ALLDATA-Inspired** - Familiar professional format  
✅ **Information Dense** - Maximum content, minimal fluff  

---

**Status**: Production-ready professional styling for mechanics! 🔧
