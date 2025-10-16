#!/usr/bin/env python3
"""
wiring_diagram_helper.py - Generate wiring diagram assistance and electrical diagnostics
Swoop Service Auto - Electrical System Diagnostics

Usage:
    python wiring_diagram_helper.py <year> <make> <model> <system> [issue]
    
Example:
    python wiring_diagram_helper.py 2018 Honda Civic "fuel pump" "no start"
    python wiring_diagram_helper.py 2020 Ford F-150 "headlights"
"""

import os
import json
import sys
from pathlib import Path

# Add tools directory to path for ai_client import
sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))
from ai_client import AIClient


class WiringDiagramHelper:
    """Generate electrical system documentation and diagnostic procedures"""
    
    def __init__(self):
        self.client = AIClient(purpose="research")
    
    def get_wiring_help(self, year, make, model, system, issue=""):
        """Generate wiring diagram assistance and diagnostic steps"""
        
        issue_context = f"\nSpecific Issue: {issue}" if issue else "\nRequest: General diagnostics and wiring information"
        
        prompt = f"""You are an expert automotive electrical technician with decades of experience in electrical diagnostics and wiring. Provide comprehensive wiring diagram assistance and diagnostic procedures for:

Vehicle: {year} {make} {model}
System: {system}{issue_context}

Please provide a comprehensive electrical diagnostic guide in JSON format:

{{
  "vehicle": {{
    "year": {year},
    "make": "{make}",
    "model": "{model}",
    "system": "{system}",
    "issue": "{issue if issue else 'General diagnostics'}"
  }},
  "system_overview": {{
    "description": "How this electrical system works",
    "components": [
      {{"name": "Component", "function": "What it does", "location": "Where to find it"}}
    ],
    "power_flow": "Describe the electrical path from battery to end component"
  }},
  "circuit_information": {{
    "power_source": "Battery/Fuse/Relay details",
    "ground_points": [
      {{"location": "Description", "wire_color": "Color"}}
    ],
    "main_wires": [
      {{
        "color": "Wire color code",
        "function": "What this wire does",
        "from": "Source",
        "to": "Destination",
        "voltage": "Expected voltage"
      }}
    ],
    "connectors": [
      {{
        "name": "Connector designation (C123, etc.)",
        "location": "Where to find it",
        "pins": "Number of pins",
        "notes": "Testing access notes"
      }}
    ]
  }},
  "fuses_and_relays": {{
    "fuses": [
      {{
        "name": "Fuse name/number",
        "location": "Under-hood or interior box",
        "rating": "XX amps",
        "circuits_protected": ["What it protects"]
      }}
    ],
    "relays": [
      {{
        "name": "Relay name/number",
        "location": "Box location",
        "part_number": "OEM part number if available",
        "function": "What it controls",
        "testing_procedure": "How to test"
      }}
    ]
  }},
  "diagnostic_procedure": {{
    "tools_required": [
      "Multimeter (voltage, continuity, resistance)",
      "Test light",
      "Other specialized tools"
    ],
    "safety_precautions": [
      "Disconnect battery before testing",
      "Avoid shorts",
      "Wear safety glasses"
    ],
    "step_by_step": [
      {{
        "step": 1,
        "description": "What to do",
        "expected_result": "What you should see/measure",
        "if_failed": "What to check next if test fails"
      }}
    ]
  }},
  "voltage_tests": [
    {{
      "test_point": "Where to test",
      "test_condition": "Key on/engine running/etc.",
      "expected_voltage": "12V/5V/Ground/etc.",
      "meter_setup": "DC voltage, black to ground, red to test point"
    }}
  ],
  "resistance_tests": [
    {{
      "component": "What to test",
      "test_points": "Where to connect meter leads",
      "expected_resistance": "XX ohms or XX-XX ohm range",
      "notes": "Disconnect component, check for opens/shorts"
    }}
  ],
  "common_failures": [
    {{
      "symptom": "What the problem looks like",
      "likely_cause": "Most common cause",
      "diagnostic_steps": ["How to confirm"],
      "repair": "How to fix",
      "parts_needed": ["Required parts"]
    }}
  ],
  "wire_repair": {{
    "splice_procedure": "How to properly splice wires",
    "terminal_repair": "How to replace terminals",
    "recommended_materials": ["Solder and heat shrink", "Crimp connectors", "etc."]
  }},
  "technical_specifications": {{
    "voltage_standards": "12V system, etc.",
    "can_bus_present": "Yes/No - if yes, special precautions",
    "computer_control": "ECM/BCM/PCM involvement",
    "scan_tool_access": "Can this system be diagnosed with OBD2 scanner?"
  }},
  "research_sources": [
    "Factory wiring diagram reference",
    "Forum or technical source"
  ]
}}

**CRITICAL REQUIREMENTS:**
1. Provide SPECIFIC wire colors for this vehicle generation
2. Include exact fuse/relay locations and ratings
3. Specify voltage/resistance values for testing
4. Include step-by-step diagnostic procedure
5. Note any CAN bus or computer-controlled components
6. Warn about high-voltage systems (hybrids/EVs)
7. Include ground point locations (common failure points)
8. Specify connector locations and access procedures
9. Note generation-specific differences if applicable
10. Include common failure patterns from forums/experience

**Safety Notes:**
- Always disconnect battery when working on electrical systems
- Identify high-voltage systems (orange wires on hybrids/EVs)
- Never probe airbag system connectors
- Use proper fuse ratings - never bypass

Output ONLY valid JSON."""

        print(f"🔌 Researching electrical system for {year} {make} {model} - {system}...")
        if issue:
            print(f"   Issue: {issue}")
        print(f"   Using {self.client.provider} ({self.client.model})")
        
        system_message = "You are an expert automotive electrical technician with decades of experience."
        
        response = self.client.chat(prompt, system_message=system_message)
        
        return response
    
    def parse_and_display(self, response_text):
        """Parse JSON response and display in readable format"""
        # Try to parse JSON using AI client helper
        data = self.client.extract_json(response_text)
        
        if not data:
            print(f"\n⚠️  Could not parse JSON response")
            print("\nRaw response:")
            print("="*80)
            print(response_text)
            print("="*80)
            return None
            
            # Display formatted output
            print("\n" + "="*80)
            print("🔌 ELECTRICAL SYSTEM DIAGNOSTICS")
            print("="*80)
            
            # Vehicle info
            if 'vehicle' in data:
                v = data['vehicle']
                print(f"\n🚗 VEHICLE: {v['year']} {v['make']} {v['model']}")
                print(f"⚡ SYSTEM: {v['system']}")
                if v.get('issue'):
                    print(f"🔍 ISSUE: {v['issue']}")
            
            # System overview
            if 'system_overview' in data:
                so = data['system_overview']
                print(f"\n📋 SYSTEM OVERVIEW:")
                print(f"   {so.get('description', 'N/A')}")
                if 'power_flow' in so:
                    print(f"\n   Power Flow: {so['power_flow']}")
                if 'components' in so:
                    print(f"\n   Components:")
                    for comp in so['components']:
                        print(f"      • {comp['name']}: {comp['function']}")
                        print(f"        Location: {comp['location']}")
            
            # Fuses and relays
            if 'fuses_and_relays' in data:
                far = data['fuses_and_relays']
                print(f"\n🔌 FUSES & RELAYS:")
                
                if 'fuses' in far and far['fuses']:
                    print(f"\n   Fuses:")
                    for fuse in far['fuses']:
                        print(f"      • {fuse['name']} - {fuse['rating']}")
                        print(f"        Location: {fuse['location']}")
                        if 'circuits_protected' in fuse:
                            print(f"        Protects: {', '.join(fuse['circuits_protected'])}")
                
                if 'relays' in far and far['relays']:
                    print(f"\n   Relays:")
                    for relay in far['relays']:
                        print(f"      • {relay['name']}")
                        print(f"        Location: {relay['location']}")
                        print(f"        Function: {relay['function']}")
            
            # Circuit information
            if 'circuit_information' in data:
                ci = data['circuit_information']
                print(f"\n🔧 CIRCUIT INFORMATION:")
                
                if 'power_source' in ci:
                    print(f"   Power Source: {ci['power_source']}")
                
                if 'main_wires' in ci and ci['main_wires']:
                    print(f"\n   Wire Colors:")
                    for wire in ci['main_wires']:
                        print(f"      • {wire['color']}: {wire['function']}")
                        print(f"        {wire['from']} → {wire['to']} ({wire.get('voltage', 'N/A')})")
                
                if 'ground_points' in ci and ci['ground_points']:
                    print(f"\n   Ground Points:")
                    for gnd in ci['ground_points']:
                        print(f"      • {gnd['location']} (Wire: {gnd.get('wire_color', 'N/A')})")
            
            # Diagnostic procedure
            if 'diagnostic_procedure' in data:
                dp = data['diagnostic_procedure']
                print(f"\n🔍 DIAGNOSTIC PROCEDURE:")
                
                if 'tools_required' in dp:
                    print(f"\n   Tools Required:")
                    for tool in dp['tools_required']:
                        print(f"      • {tool}")
                
                if 'safety_precautions' in dp:
                    print(f"\n   ⚠️  Safety Precautions:")
                    for safety in dp['safety_precautions']:
                        print(f"      • {safety}")
                
                if 'step_by_step' in dp:
                    print(f"\n   Steps:")
                    for step in dp['step_by_step']:
                        print(f"\n      Step {step['step']}: {step['description']}")
                        print(f"         Expected: {step.get('expected_result', 'N/A')}")
                        if 'if_failed' in step:
                            print(f"         If Failed: {step['if_failed']}")
            
            # Voltage tests
            if 'voltage_tests' in data and data['voltage_tests']:
                print(f"\n⚡ VOLTAGE TESTS:")
                for test in data['voltage_tests']:
                    print(f"\n   Test Point: {test['test_point']}")
                    print(f"   Condition: {test['test_condition']}")
                    print(f"   Expected: {test['expected_voltage']}")
                    print(f"   Setup: {test.get('meter_setup', 'N/A')}")
            
            # Resistance tests
            if 'resistance_tests' in data and data['resistance_tests']:
                print(f"\n🔧 RESISTANCE TESTS:")
                for test in data['resistance_tests']:
                    print(f"\n   Component: {test['component']}")
                    print(f"   Test Points: {test['test_points']}")
                    print(f"   Expected: {test['expected_resistance']}")
                    if 'notes' in test:
                        print(f"   Notes: {test['notes']}")
            
            # Common failures
            if 'common_failures' in data and data['common_failures']:
                print(f"\n⚠️  COMMON FAILURES:")
                for failure in data['common_failures']:
                    print(f"\n   Symptom: {failure['symptom']}")
                    print(f"   Likely Cause: {failure['likely_cause']}")
                    print(f"   Diagnostic Steps:")
                    for step in failure.get('diagnostic_steps', []):
                        print(f"      • {step}")
                    print(f"   Repair: {failure['repair']}")
                    if 'parts_needed' in failure:
                        print(f"   Parts: {', '.join(failure['parts_needed'])}")
            
            # Technical specs
            if 'technical_specifications' in data:
                ts = data['technical_specifications']
                print(f"\n📊 TECHNICAL SPECIFICATIONS:")
                for key, value in ts.items():
                    print(f"   {key.replace('_', ' ').title()}: {value}")
            
            # Sources
            if 'research_sources' in data:
                print(f"\n📚 SOURCES:")
                for source in data['research_sources']:
                    print(f"   • {source}")
            
            print("\n" + "="*80 + "\n")
            
            return data


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 5:
        print("="*80)
        print("WIRING DIAGRAM HELPER")
        print("Swoop Service Auto - Electrical System Diagnostics")
        print("="*80)
        print("\nUsage:")
        print("  python wiring_diagram_helper.py <year> <make> <model> <system> [issue]")
        print("\nExamples:")
        print('  python wiring_diagram_helper.py 2018 Honda Civic "fuel pump" "no start"')
        print('  python wiring_diagram_helper.py 2020 Ford F-150 "headlights"')
        print('  python wiring_diagram_helper.py 2019 Toyota Camry "starter" "clicking noise"')
        print('  python wiring_diagram_helper.py 2022 Chevrolet Silverado "power windows"')
        print("\nCommon Systems:")
        print("  • fuel pump           • starter motor       • alternator")
        print("  • headlights          • power windows       • door locks")
        print("  • ignition system     • cooling fans        • horn")
        print("  • radio/audio         • power mirrors       • wipers")
        print("\nConfiguration:")
        print("  Configure AI provider in .env file (RESEARCH_AI_PROVIDER)")
        print("\n" + "="*80)
        sys.exit(1)
    
    year = int(sys.argv[1])
    make = sys.argv[2]
    model = sys.argv[3]
    system = sys.argv[4]
    issue = sys.argv[5] if len(sys.argv) > 5 else ""
    
    try:
        helper = WiringDiagramHelper()
        response = helper.get_wiring_help(year, make, model, system, issue)
        data = helper.parse_and_display(response)
        
        # Save to JSON if requested
        if '--save' in sys.argv and data:
            filename = f"wiring_{make}_{model}_{year}_{system}.json".lower().replace(' ', '_')
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"💾 Saved to: {filename}")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}\n")
        sys.exit(1)
