#!/usr/bin/env python3
"""
Chevrolet Gap Analysis Tool
Compares CHECKLIST.md models against vehicles.json entries
"""

# Models from CHECKLIST.md organized by decade
checklist_models = {
    "1910s": [
        "Series C Classic Six",
        "Light Six",
        "Series H",
        "Series 490",
        "Series F",
        "Series D",
        "Series FA",
        "Series FB"
    ],
    "1920s": [
        "Superior",
        "Series M Copper-Cooled",
        "Series AA Capitol",
        "Series AB National",
        "Series AC International"
    ],
    "1930s": [
        "Series AD Universal",
        "Series AE Independence",
        "Series BA Confederate",
        "CA Eagle/Master",
        "Standard Six",
        "Master",
        "Suburban"
    ],
    "1940s": [
        "AK Series",
        "Deluxe",
        "Fleetmaster",
        "Stylemaster",
        "Advance Design"
    ],
    "1950s": [
        "Bel Air",
        "150",
        "210",
        "Townsman",
        "Nomad",
        "Task Force",
        "Biscayne",
        "Brookwood",
        "Impala",
        "El Camino",
        "Kingswood",
        "Corvette C1"
    ],
    "1960s": [
        "C/K",
        "Corvair",
        "Corvair 95",
        "Chevy II / Nova",
        "Corvette C2",
        "Chevelle",
        "Chevy Van",
        "Caprice",
        "Camaro",
        "Corvette C3",
        "K5 Blazer",
        "Kingswood Estate",
        "Monte Carlo"
    ],
    "1970s": [
        "Vega",
        "LUV",
        "Chevelle Laguna",
        "Chevette",
        "Monza",
        "Malibu",
        "Citation"
    ],
    "1980s": [
        "Kodiak",
        "Celebrity",
        "Cavalier",
        "S-10",
        "Corvette C4",
        "Astro",
        "Sprint",
        "Corsica",
        "Beretta",
        "GMT400",
        "Lumina APV",
        "Tracker"
    ],
    "1990s": [
        "Lumina",
        "Tahoe",
        "Express",
        "Venture",
        "Corvette C5",
        "Metro",
        "Prizm",
        "Silverado"
    ],
    "2000s": [
        "Avalanche",
        "TrailBlazer",
        "SSR",
        "Aveo",
        "Colorado",
        "Equinox",
        "Corvette C6",
        "Uplander",
        "HHR",
        "Cobalt",
        "Cruze"
    ],
    "2010s": [
        "Volt",
        "Traverse",
        "Captiva Sport",
        "Sonic",
        "Corvette C7",
        "City Express",
        "Camaro",
        "Malibu",
        "Colorado",
        "Equinox",
        "Bolt EV",
        "Bolt EUV"
    ],
    "2020s": [
        "Blazer",
        "Blazer EV",
        "Trailblazer",
        "Equinox EV",
        "Silverado EV",
        "Silverado HD",
        "Silverado Medium Duty",
        "Colorado",
        "Traverse",
        "Trax",
        "Tahoe",
        "Suburban",
        "Corvette C8",
        "Express",
        "BrightDrop Zevo"
    ]
}

# Models from vehicles.json (simplified names for matching)
in_json = [
    "AK Series", "Advance Design", "Astro", "Avalanche", "Aveo",
    "Bel Air", "Beretta", "Biscayne", "Blazer", "Blazer EV",
    "Bolt EUV", "Bolt EV", "BrightDrop Zevo", "Brookwood",
    "C/K", "Camaro", "Caprice", "Captiva Sport", "Cavalier",
    "Celebrity", "Chevelle", "Chevelle Laguna", "Chevette",
    "Chevy II / Nova", "Chevy Van", "Citation", "City Express",
    "Cobalt", "Colorado", "Corsica", "Corvair", "Corvair 95",
    "Corvette C1", "Corvette C2", "Corvette C3", "Corvette C4",
    "Corvette C5", "Corvette C6", "Corvette C7", "Corvette C8",
    "Cruze", "Deluxe", "El Camino", "Equinox", "Equinox EV",
    "Express", "Fleetmaster", "HHR", "Impala", "K5 Blazer",
    "Kingswood", "Kingswood Estate", "Kodiak", "LUV",
    "Lumina", "Lumina APV", "Malibu", "Master", "Metro",
    "Monte Carlo", "Monza", "Nomad", "150", "Prizm",
    "S-10", "SSR", "Series 490", "Series AA Capitol",
    "Series AB National", "Series AC International",
    "Series AD Universal", "Series AE Independence",
    "Series BA Confederate", "Series C Classic Six",
    "Series CA Eagle/Master", "Series D", "Series F",
    "Series FA", "Series FB", "Series H", "Series L Light Six",
    "Series M Copper-Cooled", "Silverado", "Silverado EV",
    "Silverado HD", "Silverado Medium Duty", "Sonic",
    "Sprint", "Standard Six", "Stylemaster", "Suburban",
    "Superior", "Tahoe", "Task Force", "Townsman",
    "Tracker", "TrailBlazer", "Trailblazer", "Traverse",
    "Trax", "210", "Uplander", "Vega", "Venture", "Volt"
]

print("# Chevrolet Gap Analysis Results\n")
print("=" * 80)

total_models = 0
found_models = 0
missing_models = 0

for decade, models in sorted(checklist_models.items()):
    print(f"\n## {decade}")
    print("-" * 80)

    for model in models:
        total_models += 1
        # Normalize for matching
        model_simple = model.replace(" (C1)", " C1").replace(" (C2)", " C2").replace(" (C3)", " C3").replace(" (C4)", " C4").replace(" (C5)", " C5").replace(" (C6)", " C6").replace(" (C7)", " C7").replace(" (C8)", " C8")

        # Check if model is in JSON
        found = False
        for json_model in in_json:
            if model_simple.lower() in json_model.lower() or json_model.lower() in model_simple.lower():
                found = True
                break

        if found:
            print(f"  [x] {model}")
            found_models += 1
        else:
            print(f"  [ ] {model} ← MISSING")
            missing_models += 1

print("\n" + "=" * 80)
print(f"\nSummary:")
print(f"  Total models in CHECKLIST.md: {total_models}")
print(f"  Found in vehicles.json: {found_models}")
print(f"  Missing from vehicles.json: {missing_models}")
print(f"  Coverage: {(found_models/total_models*100):.1f}%")
