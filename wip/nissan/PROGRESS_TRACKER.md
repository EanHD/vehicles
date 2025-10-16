# Nissan Research Progress Tracker

**Last Updated**: October 14, 2025  
**Strategy**: Modern-first (2020s → 1980s), then work backward through historic decades  
**Current vehicles.json count**: 96 Nissan entries (all decades appended October 14, 2025)

---

## Quick Status Overview

| Decade | Models (target) | Status | JSON File | Validation | Appended |
|--------|-----------------|--------|-----------|------------|----------|
| 2020s  | 14              | ✅ 14/14 | `wip/nissan/2020s.json` | ✅ | ✅ APPENDED |
| 2010s  | 14              | ✅ 14/14 | `wip/nissan/2010s.json` | ✅ | ✅ APPENDED |
| 2000s  | 19              | ✅ 19/19 | `wip/nissan/2000s.json` | ✅ | ✅ APPENDED |
| 1990s  | 11              | ✅ 11/11 | `wip/nissan/1990s.json` | ✅ | ✅ APPENDED |
| 1980s  | 11              | ✅ 11/11 | `wip/nissan/1980s.json` | ✅ | ✅ APPENDED |
| 1970s  | 7               | ✅ 7/7 | `wip/nissan/1970s.json` | ✅ | ✅ APPENDED |
| 1960s  | 6               | ✅ 6/6 | `wip/nissan/1960s.json` | ✅ | ✅ APPENDED |
| 1950s  | 5               | ✅ 5/5 | `wip/nissan/1950s.json` | ✅ | ✅ APPENDED |
| 1940s  | 3               | ✅ 3/3 | `wip/nissan/1940s.json` | ✅ | ✅ APPENDED |
| 1930s  | 4               | ✅ 4/4 | `wip/nissan/1930s.json` | ✅ | ✅ APPENDED |

**Legend**: ⏳ TODO | 🔄 IN PROGRESS | ✅ DONE | 🔜 LATER | ⚠️ NEEDS REVIEW

---

## Validation Checklist (per decade)

- [x] Decade JSON validates with `jq empty`
- [x] All required schema fields populated (years, engines, transmissions, etc.)
- [x] Hybrid and diesel flags aligned with powertrain data
- [x] Difficulty modifiers ≥ 1.00 with notes justification
- [x] Service-critical notes + platform sharing captured
- [x] Notes include Wikipedia citation + revision date

---

## Decade Work Queues & Model Coverage

### 2020s Focus List (14 models)
- [x] Altima (L34, 2019–present)
- [x] Sentra (B18, 2020–present)
- [x] Rogue (T33, 2021–present)
- [x] Pathfinder (R53, 2022–present)
- [x] Frontier (D41, 2022–present)
- [x] Ariya (2023–present)
- [x] Z (RZ34, 2023–present)
- [x] Leaf (ZE1 updates, 2020s)
- [x] Versa (N18, 2020–present)
- [x] Maxima (A36, 2020–2023)
- [x] Murano (Z52, 2020–2024)
- [x] Murano (4th generation 2025 launch)
- [x] Titan/Titan XD (A61, 2020–2024 sunset)
- [x] Kicks (P15, 2020–present NA)
- [x] GT-R (R35, 2020s updates)

### 2010s Focus List (14 models)
- [x] Altima (L33, 2013–2018)
- [x] Sentra (B17, 2013–2019)
- [x] Versa (N17 sedan, 2012–2019)
- [x] Maxima (A36, 2016–2020)
- [x] Leaf (ZE0, 2011–2017)
- [x] Juke (F15, 2011–2017)
- [x] Murano (Z52, 2015–2019)
- [x] Pathfinder (R52, 2013–2020)
- [x] Rogue (T32, 2014–2020)
- [x] Titan XD / second-gen Titan (A61, 2016–2019 NA)
- [x] NV200 (2013–2021)
- [x] Kicks (P15, 2018–2019 intro)
- [x] Rogue Sport / Qashqai (2017–2019 NA)
- [x] GT-R (R35 updates 2017–2020)

- [x] 350Z (Z33, 2003–2009)
- [x] 370Z (Z34 initial years 2009–2010)
- [x] Altima (L31, 2002–2006)
- [x] Altima (L32, 2007–2012)
- [x] Sentra (B15, 2000–2006)
- [x] Sentra (B16, 2007–2012)
- [x] Maxima (A34, 2004–2008)
- [x] Maxima (A35, 2009–2014)
- [x] Murano (Z50/Z51, 2003–2014)
- [x] Armada (TA60, 2004–2015; NA focus)
- [x] Titan (A60, 2004–2015)
- [x] Frontier (D40, 2005–2021 early years)
- [x] Quest (V42, 2004–2009)
- [x] Versa (C11 hatch/sedan 2007–2012)
- [x] Rogue (S35, 2008–2013)
- [x] GT-R (R35 launch 2009–2011)
- [x] Cube (Z12, 2009–2014)
- [x] NV Cargo/Passenger (2012–2021 early years)
- [x] NV Cargo/Passenger (2012–2021 early years)
- [ ] 370Z (Z34 initial years 2009–2010)
- [ ] Altima (L31/L32, 2002–2012)
- [ ] Sentra (B15/B16/B17 early, 2000–2012)
- [ ] Maxima (A34/A35, 2004–2014)
- [ ] Murano (Z50/Z51, 2003–2014)
- [ ] Armada (TA60, 2004–2015; NA focus)
- [ ] Titan (A60, 2004–2015)
- [ ] Frontier (D40, 2005–2021 early years)
- [ ] Quest (2004–2009, 2011–2017)
- [ ] Versa (C11 hatch/sedan 2007–2012)
- [ ] Rogue (S35, 2008–2013)
- [ ] GT-R (R35 launch 2009–2011 NA)
- [ ] Cube (Z12, 2009–2014)
- [ ] NV Cargo/Passenger (2012–2021 early years)

### 1990s Focus List (10 models)
- [x] 300ZX (Z32, 1990–1996 NA)
- [x] Sentra (B13/B14, 1991–1999)
- [x] Altima (U13, 1993–1997)
- [x] Maxima (A32/A33, 1995–2000)
- [x] 240SX (S13/S14, 1989–1998 NA)
- [x] Pathfinder (R50, 1996–2004)
- [x] Frontier (D22, 1998–2004)
- [x] Quest (1993–2002, NA)
- [x] Xterra (WD22, 2000–2004 early)
- [x] GT-R (R32/R33 grey import status)

### 1980s Focus List (10 models)
- [x] 280ZX (S130 late, 1979–1983)
- [x] 300ZX (Z31, 1984–1989)
- [x] Sentra / Sunny (B11/B12, 1982–1990 NA)
- [x] Maxima (U11/J30, 1981–1988)
- [x] Stanza (T11, 1982–1986)
- [x] Pulsar NX (1987–1990)
- [x] Pathfinder (WD21, 1986–1995)
- [x] Hardbody (D21, 1986–1997)
- [x] 200SX (S12, 1984–1988)
- [x] Axxess (1990 model year – confirm NA)

### 1970s Focus List (6 models)
- [ ] 240Z/260Z/280Z (S30, 1969–1978 NA)
- [x] 240Z/260Z/280Z (S30, 1969–1978 NA)
- [ ] 510/610/710 sedans (1970–1976)
- [ ] B210/Sunny (1973–1978)
- [ ] 200SX (S10, 1975–1979)
- [ ] 620 Pickup (1972–1979)
- [ ] Vanette (C20, 1978–1980 NA evaluation)
- [x] 510/610/710 sedans (1970–1976)
- [x] B210/Sunny (1973–1978)
- [x] 200SX (S10, 1975–1979)
- [x] 620 Pickup (1972–1979)
- [x] Vanette (C20, 1978–1980 NA evaluation)

### 1960s Focus List (6 models)
- [ ] Fairlady Roadsters (SP/SR311, 1961–1970)
- [x] Fairlady Roadsters (SP/SR311, 1961–1970)
- [x] Bluebird 410/510 (1963–1973 NA)
- [x] Cedric 130 (1965–1971 North American presence? verify)
- [x] Silvia (CSP311, 1965–1968 limited import)
- [x] Patrol (60/K60, 1962–1969 NA)
- [x] Skyline (Prince/Nissan C10/C110, 1968–1977 NA racing homologation?)

### 1950s Focus List (5 models)
- [x] Datsun 110/210 (1955–1959)
- [x] 113/114 sedans (1957–1959)
- [x] Datsun 220/223 trucks (1957–1965)
- [x] Sports DC-3 (1959 limited export)
- [x] Patrol 60 launch (1959–1965 NA intro)

### 1940s Focus List (3 models)
- [x] Datsun 212/312 trucks (1946–1949)
- [x] Datsun 1121 passenger car (1946–1947)
- [x] Datsun 5147 truck (1947–1954 production overlap)

### 1930s Focus List (4 models)
- [x] Datsun Type 10/11 (1932–1934)
- [x] Datsun Type 12/13 (1933–1935)
- [x] Datsun Roadster 15/16 (1935–1938)
- [x] Datsun Type 17 truck (1938–1939)

---

## Wikipedia Source Log

| Model | URL | Revision Date | Notes |
|-------|-----|---------------|-------|
| Altima (L34) | https://en.wikipedia.org/wiki/Nissan_Altima | October 13, 2025 | 6th-gen NA spec (PR25DD, KR20DDET) |
| Sentra (B18) | https://en.wikipedia.org/wiki/Nissan_Sentra | October 9, 2025 | 8th-gen NA sedan |
| Altima (L33) | https://en.wikipedia.org/wiki/Nissan_Altima | October 13, 2025 | 5th-gen NA sedan (QR25DE/VQ35DE) |
| Sentra (B17) | https://en.wikipedia.org/wiki/Nissan_Sentra | October 14, 2025 | 7th-gen NA sedan (MRA8DE/MR16DDT) |
| Rogue (T33) | https://en.wikipedia.org/wiki/Nissan_Rogue | October 14, 2025 | 3rd-gen NA crossover |
| Rogue (T32) | https://en.wikipedia.org/wiki/Nissan_Rogue | October 14, 2025 | 2nd-gen NA crossover (hybrid) |
| Rogue (S35) | https://en.wikipedia.org/wiki/Nissan_Rogue | October 14, 2025 | 1st-gen NA crossover |
| Rogue Sport (J11) | https://en.wikipedia.org/wiki/Nissan_Rogue_Sport | October 10, 2025 | NA Qashqai launch (MR20DD) |
| Pathfinder (R53) | https://en.wikipedia.org/wiki/Nissan_Pathfinder | October 14, 2025 | 5th-gen NA SUV |
| Pathfinder (R52) | https://en.wikipedia.org/wiki/Nissan_Pathfinder | October 14, 2025 | 4th-gen NA crossover (hybrid CVT) |
| Frontier (D41) | https://en.wikipedia.org/wiki/Nissan_Frontier | October 6, 2025 | 3rd-gen NA pickup |
| Frontier (D40) | https://en.wikipedia.org/wiki/Nissan_Frontier | October 6, 2025 | 2nd-gen NA pickup (PRO-4X) |
| Ariya | https://en.wikipedia.org/wiki/Nissan_Ariya | October 12, 2025 | NA launch (63/87 kWh, e-4ORCE) |
| Z (RZ34) | https://en.wikipedia.org/wiki/Nissan_Z_(RZ34) | October 13, 2025 | 7th-gen sports coupe |
| Leaf (ZE1) | https://en.wikipedia.org/wiki/Nissan_Leaf | October 14, 2025 | 2nd-gen EV (40/62 kWh) |
| Leaf (ZE0) | https://en.wikipedia.org/wiki/Nissan_Leaf | October 14, 2025 | 1st-gen EV (24/30 kWh) |
| Versa (N18) | https://en.wikipedia.org/wiki/Nissan_Almera | October 14, 2025 | US Versa sedan coverage |
| Versa (N17) | https://en.wikipedia.org/wiki/Nissan_Almera | October 14, 2025 | 2nd-gen Versa sedan (HR16DE) |
| Maxima (A36) | https://en.wikipedia.org/wiki/Nissan_Maxima | October 14, 2025 | 8th-gen NA sedan |
| Maxima (A35) | https://en.wikipedia.org/wiki/Nissan_Maxima | October 14, 2025 | 7th-gen CVT sport sedan |
| Maxima (A34) | https://en.wikipedia.org/wiki/Nissan_Maxima | October 14, 2025 | 6th-gen FF-L manual option |
| Altima (L31) | https://en.wikipedia.org/wiki/Nissan_Altima | October 13, 2025 | 4th-gen FF-L sedan (QR25DE/VQ35DE) |
| Altima (L32) | https://en.wikipedia.org/wiki/Nissan_Altima | October 13, 2025 | 5th-gen D-platform sedan/coupe (hybrid, CVT) |
| Sentra (B15) | https://en.wikipedia.org/wiki/Nissan_Sentra | October 14, 2025 | MS-platform sedan with SE-R/Spec V |
| Sentra (B16) | https://en.wikipedia.org/wiki/Nissan_Sentra | October 14, 2025 | C-platform sedan + SE-R Spec V |
| Murano (Z52/4th gen) | https://en.wikipedia.org/wiki/Nissan_Murano | October 14, 2025 | 3rd-gen refresh + 2025 redesign |
| Murano (Z51) | https://en.wikipedia.org/wiki/Nissan_Murano | October 14, 2025 | 2nd-gen NA crossover |
| Murano (Z50) | https://en.wikipedia.org/wiki/Nissan_Murano | October 14, 2025 | 1st-gen high-torque CVT launch |
| Armada (TA60) | https://en.wikipedia.org/wiki/Nissan_Armada | October 14, 2025 | F-Alpha full-size SUV (VK56DE) |
| Titan (A60) | https://en.wikipedia.org/wiki/Nissan_Titan | October 14, 2025 | 1st-gen F-Alpha pickup |
| Titan (A61) | https://en.wikipedia.org/wiki/Nissan_Titan | October 14, 2025 | 2020 refresh, XD details |
| Quest (V42) | https://en.wikipedia.org/wiki/Nissan_Quest | October 14, 2025 | 3rd-gen minivan (SkyView/power doors) |
| Versa (C11) | https://en.wikipedia.org/wiki/Nissan_Tiida | October 5, 2025 | NA Versa hatch (MR18DE, manual/CVT) |
| NV Cargo/Passenger | https://en.wikipedia.org/wiki/Nissan_NV_(North_America) | October 5, 2025 | F-Alpha full-size van |
| NV200 | https://en.wikipedia.org/wiki/Nissan_NV200 | October 10, 2025 | US cargo van & NYC Taxi configuration |
| Kicks (P15) | https://en.wikipedia.org/wiki/Nissan_Kicks | October 14, 2025 | NA P15 refresh |
| GT-R (R35) | https://en.wikipedia.org/wiki/Nissan_GT-R | October 14, 2025 | 2020 update + 2024 T-spec |
| GT-R (R35 launch) | https://en.wikipedia.org/wiki/Nissan_GT-R | October 14, 2025 | 2009–2011 NA introduction |
| Juke (F15) | https://en.wikipedia.org/wiki/Nissan_Juke | October 9, 2025 | NA turbo crossover (MR16DDT, torque-vectoring AWD) |
| 350Z (Z33) | https://en.wikipedia.org/wiki/Nissan_350Z | September 22, 2024 | FM-platform sports coupe (VQ35DE/VQ35HR) |
| 370Z (Z34) | https://en.wikipedia.org/wiki/Nissan_370Z | October 5, 2025 | Launch models with SynchroRev Match |
| Cube (Z12) | https://en.wikipedia.org/wiki/Nissan_Cube | October 6, 2025 | Lounge-style subcompact (MR18DE) |
| 300ZX (Z32) | https://en.wikipedia.org/wiki/Nissan_300ZX | October 10, 2025 | Twin-turbo Z32 with HICAS |
| 300ZX (Z31) | https://en.wikipedia.org/wiki/Nissan_300ZX | October 10, 2025 | First-gen VG-powered Z for NA |
| 280ZX (S130) | https://en.wikipedia.org/wiki/Nissan_S130 | October 11, 2025 | Turbo grand-tourer (L28E/L28ET) |
| Sentra (B11/B12) | https://en.wikipedia.org/wiki/Nissan_Sentra | October 14, 2025 | Early FWD GA/E-series models |
| Pulsar NX | https://en.wikipedia.org/wiki/Nissan_Pulsar_NX | October 6, 2025 | Modular SportBak coupe |
| Pathfinder (WD21) | https://en.wikipedia.org/wiki/Nissan_Pathfinder | October 14, 2025 | First-gen body-on-frame SUV |
| Hardbody (D21) | https://en.wikipedia.org/wiki/Nissan_Navara | October 11, 2025 | D21 pickup (Z24i/KA24E/VG30E) |
| 200SX (S12) | https://en.wikipedia.org/wiki/Nissan_200SX | October 8, 2025 | Turbo/V6 RWD hatch |
| Axxess (M11) | https://en.wikipedia.org/wiki/Nissan_Prairie | October 6, 2025 | Sliding-door compact MPV |
| S30 Z | https://en.wikipedia.org/wiki/Nissan_S30 | October 11, 2025 | Original Z-car (240Z/260Z/280Z) |
| Datsun 510 | https://en.wikipedia.org/wiki/Datsun_510 | October 12, 2025 | PL510 independent rear suspension sedan |
| Datsun 610 | https://en.wikipedia.org/wiki/Datsun_610 | October 10, 2025 | Bluebird U (610/710) NA lineup |
| Datsun Sunny (B210) | https://en.wikipedia.org/wiki/Datsun_Sunny | October 9, 2025 | B210 fuel-economy hatch/sedan |
| Nissan Silvia (S10) | https://en.wikipedia.org/wiki/Nissan_Silvia | October 8, 2025 | Datsun 200SX fastback |
| Datsun Truck | https://en.wikipedia.org/wiki/Datsun_truck | October 9, 2025 | 620 pickup (L-series) |
| Nissan Vanette | https://en.wikipedia.org/wiki/Nissan_Vanette | October 7, 2025 | Compact C20 van |
| Datsun Fairlady Roadster | https://en.wikipedia.org/wiki/Datsun_Sports | October 9, 2025 | SP/SR roadsters for NA |
| Nissan Bluebird (410/411) | https://en.wikipedia.org/wiki/Nissan_Bluebird | October 10, 2025 | Mid-60s Bluebird exports |
| Nissan Cedric 130 | https://en.wikipedia.org/wiki/Nissan_Cedric | October 12, 2025 | Luxury sedan limited NA |
| Nissan Silvia CSP311 | https://en.wikipedia.org/wiki/Nissan_Silvia | October 8, 2025 | Hand-built coupe export |
| Nissan Patrol 60 | https://en.wikipedia.org/wiki/Nissan_Patrol | October 11, 2025 | Early U.S. off-road SUV |
| Nissan Skyline C10 | https://en.wikipedia.org/wiki/Nissan_Skyline | October 12, 2025 | Hakosuka limited imports |
| Datsun 210 | https://en.wikipedia.org/wiki/Datsun_210 | October 9, 2025 | First U.S. Datsun sedan |
| Datsun 1000 (113/114) | https://en.wikipedia.org/wiki/Datsun_1000 | October 8, 2025 | Mid-50s export sedans |
| Datsun Truck 220 | https://en.wikipedia.org/wiki/Datsun_truck | October 9, 2025 | Early U.S. pickup |
| Datsun Sports DC-3 | https://en.wikipedia.org/wiki/Datsun_Sports | October 9, 2025 | Pre-Fairlady roadster |
| Datsun 1121 | https://en.wikipedia.org/wiki/Datsun_1121 | October 8, 2025 | Immediate postwar sedan |
| Datsun Type 11 | https://en.wikipedia.org/wiki/Datsun_Type_11 | October 7, 2025 | Prewar compact exports |
| 240SX (S13/S14) | https://en.wikipedia.org/wiki/Nissan_240SX | October 8, 2025 | KA24-powered RWD coupe/hatch |
| Pathfinder (R50) | https://en.wikipedia.org/wiki/Nissan_Pathfinder | October 14, 2025 | Unibody second-gen SUV (VG33E/VQ35DE) |
| Frontier (D22) | https://en.wikipedia.org/wiki/Nissan_Frontier | October 6, 2025 | First-gen NA pickup (KA24DE/VG33E) |
| Quest (A32) | https://en.wikipedia.org/wiki/Nissan_Quest | October 14, 2025 | First-gen minivan (VG30E) |
| Xterra (WD22) | https://en.wikipedia.org/wiki/Nissan_Xterra | October 13, 2025 | Early supercharged off-road SUV |
| Nissan NV | https://en.wikipedia.org/wiki/Nissan_NV_(North_America) | October 5, 2025 | Full-size commercial van |
| Skyline GT-R (R32) | https://en.wikipedia.org/wiki/Nissan_Skyline_GT-R | October 12, 2025 | Motorex federalized RB26DETT |

---

## Next Steps
- Maintain the Nissan completion report (`wip/nissan/NISSAN_COMPLETION_REPORT.md`) with any future revisions
- Monitor for future Nissan model launches (e.g., 2026 Murano AWD standard, Ariya refresh) and update decade files as needed
