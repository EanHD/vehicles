# RAM Research Progress Tracker

**Last Updated**: January 17, 2025
**Strategy**: Modern RAM brand (2010s-2020s), then historic Dodge Ram trucks (1910s-2000s)
**Current vehicles.json count**: 0 RAM entries
**Status**: Starting comprehensive historical audit

---

## Quick Status Overview

| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | TBD    | 🔄 IN PROGRESS | `2020s.json` | ❌ |
| 2010s  | TBD    | ⏳ TODO | `2010s.json` | ❌ |
| **Modern RAM** | **TBD** | **IN PROGRESS** | - | ❌ |
| 2000s  | TBD    | ⏳ TODO | `2000s.json` | ❌ |
| 1990s  | TBD    | ⏳ TODO | `1990s.json` | ❌ |
| 1980s  | TBD    | ⏳ TODO | `1980s.json` | ❌ |
| 1970s  | TBD    | ⏳ TODO | `1970s.json` | ❌ |
| 1960s  | TBD    | ⏳ TODO | `1960s.json` | ❌ |
| 1950s  | TBD    | ⏳ TODO | `1950s.json` | ❌ |
| 1940s  | TBD    | ⏳ TODO | `1940s.json` | ❌ |
| 1930s  | TBD    | ⏳ TODO | `1930s.json` | ❌ |
| 1920s  | TBD    | ⏳ TODO | `1920s.json` | ❌ |
| 1910s  | TBD    | ⏳ TODO | `1910s.json` | ❌ |
| **Historic Dodge Ram** | **TBD** | **PENDING** | - | ❌ |

**Legend**: ⏳ TODO | 🔄 IN PROGRESS | ✅ DONE

---

## Important Note: RAM Brand History

**RAM split from Dodge in 2009:**
- Pre-2009: Trucks sold as "Dodge Ram"
- 2009+: "RAM" became separate brand focused on trucks/commercial vehicles
- Use "RAM" as make for 2009+ vehicles
- Use "Dodge" as make for pre-2009 trucks (but many already covered)

---

## Modern RAM Brand (2009-2025)

### 2020s Models - 🔄 IN PROGRESS
Per CHECKLIST.md:
- [ ] Ram 1500 refresh (2021–present) - Fifth generation
- [ ] Ram 1500 Classic continuation (DS platform)
- [ ] Ram HD refresh (2020–present) - 2500/3500
- [ ] ProMaster 2023 update
- [ ] ProMaster City (discontinued 2022)
- [ ] Ram 1500 REV EV (2025 launch)
- [ ] Ramcharger EREV (2025)
- [ ] Ram TRX (2021-2023)

### 2010s Models - ⏳ TODO
Per CHECKLIST.md:
- [ ] Ram 1500 DS (2009–2023) - Fourth generation
- [ ] Ram 1500 DT (2019–present) - Fifth generation
- [ ] Ram 2500/3500 HD (2010–present)
- [ ] ProMaster (2014–present)
- [ ] ProMaster City (2015–2022)
- [ ] Ram Chassis Cab (2011–present)

---

## Historic Dodge Ram Trucks (1910s-2000s)

### 2000s Models - ⏳ TODO
- [ ] Third-gen Dodge Ram (2002–2008)
- [ ] Ram SRT-10 (2004–2006) - Viper V10 pickup
- [ ] Mega Cab (2006–2009)
- [ ] Sprinter rebadged vans (2003–2009)
- [ ] Ram 4500/5500 chassis (2008–present)

### 1990s Models - ⏳ TODO
- [ ] Second-gen Dodge Ram (1994–2002)
- [ ] Ram Van (1994–2003)
- [ ] Ramcharger Mexico (1999–2001)
- [ ] Ram 3500/4500/5500 chassis cab (1998–present)

### 1980s Models - ⏳ TODO
- [ ] First-gen Dodge Ram pickup (1981–1993)
- [ ] Ramcharger second-gen (1981–1993)
- [ ] Ram Van B-series (1979–2003)
- [ ] Ram 50 compact (1987–1994) - Already in Dodge

### 1970s Models - ⏳ TODO
- [ ] D/W-Series facelift (1972–1980)
- [ ] Warlock/Lil' Red Express/Utiline specials (1976–1979)
- [ ] Ramcharger/Trail Duster SUVs (1974–1980)

### 1960s Models - ⏳ TODO
- [ ] D/W-Series Sweptline (1961–1971)
- [ ] A100/A108 vans and pickups (1964–1970)
- [ ] Power Wagon WM300 (1960–1969)

### 1950s Models - ⏳ TODO
- [ ] C-Series pickups (1954–1960)
- [ ] Town Panel/Town Wagon (1954–1966)
- [ ] Sweptside pickups (1957–1959)
- [ ] D-Series (1957–1980)

### 1940s Models - ⏳ TODO
- [ ] WC military trucks (1940–1945)
- [ ] Power Wagon (1946–1968)
- [ ] Job-Rated B-Series pickups (1948–1953)

### 1930s Models - ⏳ TODO
- [ ] Dodge KC/LC pickups (1933–1938)
- [ ] Airflow trucks (1939–1940)

### 1920s Models - ⏳ TODO
- [ ] Series 30/50 Light Commercials (1923–1928)
- [ ] Graham-built half-ton pickups (1928–1930)

### 1910s Models - ⏳ TODO
- [ ] Dodge Brothers 1-ton commercial (1917–1922)
- [ ] Screenside delivery trucks (1918–1923)

---

## Notes

- RAM became separate brand 2009 to focus on trucks/commercial vehicles
- Best-selling truck series in America (competed with F-150)
- Known for Cummins diesel engines in HD models
- Modern lineup: Light-duty (1500), Heavy-duty (2500/3500), Commercial vans
- Historic: Power Wagon legendary off-road capability

---

## Quick Commands

```bash
# Validate decade file
jq empty wip/ram/2020s.json

# Count entries
grep -c '"make": "RAM"' vehicles.json
```
