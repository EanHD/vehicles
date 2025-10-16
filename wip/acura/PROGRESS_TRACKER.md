# Acura Research Progress Tracker

**Last Updated**: January 17, 2025
**Strategy**: Complete North American Acura lineup (1986-2025)
**Current vehicles.json count**: 45 Acura entries
**Status**: COMPLETE ✅

---

## Quick Status Overview

| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | 9    | ✅ DONE | `2020s_APPENDED.json` | ✅ |
| 2010s  | 13    | ✅ DONE | `2010s_APPENDED.json` | ✅ |
| 2000s  | 14    | ✅ DONE | `2000s_APPENDED.json` | ✅ |
| 1990s  | 7    | ✅ DONE | `1990s_APPENDED.json` | ✅ |
| 1980s  | 2    | ✅ DONE | `1980s_APPENDED.json` | ✅ |
| **Acura Total** | **45** | **✅ COMPLETE** | - | ✅ |

**Legend**: ⏳ TODO | 🔄 IN PROGRESS | ✅ DONE

---

## Strategy: North American Focus

**Acura = Honda's luxury brand, launched 1986 in USA**
- First Japanese luxury brand in North America
- All models sold in North America
- Focus on comprehensive coverage (sedans, SUVs, sports cars)
- Performance division (Type S models)

**Key Model Lines:**
- **Legend** - First flagship sedan (1986-1995, 2014-2020)
- **Integra** - Sport compact (1986-2001, 2023-present)
- **NSX** - Supercar icon (1990-2005, 2016-2022)
- **RL/RLX** - Flagship sedan evolution
- **TL/TLX** - Mid-size sedan line
- **CL** - Coupe variant
- **RSX** - Sport compact successor
- **TSX** - Compact sedan/wagon
- **ILX** - Entry luxury sedan
- **MDX** - Three-row luxury SUV
- **RDX** - Compact luxury SUV
- **ZDX** - Coupe-SUV (2010-2013, EV 2024+)

---

## High Priority Models by Era

### 1980s (Launch Era)
- Legend (1986-1990)
- Integra (1986-1989)

### 1990s (Expansion)
- Legend (1991-1995)
- Integra (1990-2001)
- NSX (1990-2005)
- Vigor (1992-1994)
- TL (1996-1998)
- RL (1996-1998)
- CL (1997-1999)
- SLX (1996-1999) - Isuzu rebadge

### 2000s (Growth)
- TL (1999-2014)
- RL (1999-2004, 2005-2012)
- CL (2001-2003)
- RSX (2002-2006)
- TSX (2004-2014)
- MDX (2001-present)
- RDX (2007-present)
- ZDX (2010-2013)

### 2010s (Refresh)
- ILX (2013-2022)
- TLX (2015-present)
- RLX (2014-2020)
- NSX (2016-2022)
- MDX (continuing)
- RDX (continuing)

### 2020s (Electrification)
- TLX (continuing)
- MDX (continuing)
- RDX (continuing)
- Integra (2023-present, revival)
- ZDX (2024-present, EV)
- ILX discontinued 2022
- RLX discontinued 2020
- NSX discontinued 2022

---

## Research Notes

- **Acura founded**: 1986 (first Japanese luxury brand in NA)
- **Platform sharing**: Honda-based platforms
- **Performance**: Type S variants, SH-AWD system
- **Hybrid/EV**: MDX Sport Hybrid, RLX Sport Hybrid, ZDX EV
- **Wikipedia sources**:
  - Main: https://en.wikipedia.org/wiki/Acura
  - List of vehicles: https://en.wikipedia.org/wiki/List_of_Acura_vehicles

---

## Current Focus

**Starting with 2020s decade** to capture current lineup, then work backwards chronologically.

---

## Quick Commands

```bash
# Validate decade file
jq empty wip/acura/2020s.json

# Count entries
grep -c '"make": "Acura"' vehicles.json

# List models
grep -A 1 '"make": "Acura"' vehicles.json | grep '"model":' | sort | uniq
```
