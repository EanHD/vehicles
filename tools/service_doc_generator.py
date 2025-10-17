#!/usr/bin/env python3
"""
Service Documentation Generator for Swoop Service Auto
Combines vehicles.json + services.json with AI research to generate professional service guides
"""

import json
import os
import hashlib
import sys
import base64
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

# Add tools directory to path for ai_client import
sys.path.insert(0, str(Path(__file__).parent))
from ai_client import AIClient
from diagram_generator import DiagramGenerator


class ServiceDocGenerator:
    """Main generator class for creating service documentation"""
    
    def __init__(
        self,
        vehicles_db: str = None,
        services_db: str = None,
        cache_dir: str = None,
        enable_diagrams: bool = False
    ):
        # Get project root (parent of tools directory)
        project_root = Path(__file__).parent.parent
        
        # Set default paths relative to project root
        if vehicles_db is None:
            vehicles_db = str(project_root / "data" / "vehicles.json")
        if services_db is None:
            services_db = str(project_root / "data" / "services.json")
        if cache_dir is None:
            cache_dir = str(project_root / "service_docs")
            
        self.vehicles_db = vehicles_db
        self.services_db = services_db
        self.cache_dir = Path(cache_dir)
        self.enable_diagrams = enable_diagrams
        
        # Initialize AI clients
        self.research_ai = AIClient(purpose="research")
        self.formatter_ai = AIClient(purpose="formatter")
        
        # Initialize diagram generator (optional, only if enabled and API key available)
        self.diagram_generator = None
        if self.enable_diagrams:
            try:
                self.diagram_generator = DiagramGenerator()
                print(f"✅ Diagram generation enabled ({self.diagram_generator.provider})")
            except Exception as e:
                print(f"⚠️  Diagram generation disabled: {e}")
        
        # Load databases
        with open(vehicles_db, 'r') as f:
            self.vehicles = json.load(f)
        with open(services_db, 'r') as f:
            self.services = json.load(f)
        
        # Create cache structure
        self.cache_dir.mkdir(exist_ok=True)
        self.cache_index_path = self.cache_dir / "cache_index.json"
        self.cache_index = self._load_cache_index()
    
    def _load_cache_index(self) -> Dict:
        """Load or create cache index"""
        if self.cache_index_path.exists():
            with open(self.cache_index_path, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_cache_index(self):
        """Save cache index"""
        with open(self.cache_index_path, 'w') as f:
            json.dump(self.cache_index, f, indent=2)
    
    def _generate_cache_key(self, year: int, make: str, model: str, service: str) -> str:
        """Generate unique cache key for a service document"""
        key_str = f"{year}_{make}_{model}_{service}".lower()
        return hashlib.md5(key_str.encode()).hexdigest()
    
    def _image_to_base64(self, image_path: str) -> str:
        """Convert image file to base64 data URL"""
        try:
            with open(image_path, 'rb') as f:
                image_data = f.read()
            base64_data = base64.b64encode(image_data).decode('utf-8')
            # Detect image format from extension
            ext = Path(image_path).suffix.lower()
            mime_types = {
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.gif': 'image/gif',
                '.webp': 'image/webp'
            }
            mime_type = mime_types.get(ext, 'image/png')
            return f"data:{mime_type};base64,{base64_data}"
        except Exception as e:
            print(f"  ⚠️  Could not convert image to base64: {e}")
            return ""
    
    def _get_vehicle_data(self, year: int, make: str, model: str) -> Optional[Dict]:
        """Find vehicle in database"""
        # Normalize model name (handle parentheses, platform codes)
        model_normalized = model.split('(')[0].strip()
        
        for vehicle in self.vehicles:
            if (year in vehicle.get('years', []) and 
                vehicle.get('make', '').lower() == make.lower()):
                # Check if model matches (handle variations)
                vehicle_model = vehicle.get('model', '').split('(')[0].strip()
                if vehicle_model.lower() == model_normalized.lower():
                    return vehicle
        return None
    
    def _get_service_data(self, service_name: str) -> Optional[Dict]:
        """Find service in database"""
        for service in self.services:
            # Handle both 'service_name' and 'name' fields
            svc_name = service.get('service_name') or service.get('name', '')
            if svc_name.lower() == service_name.lower():
                return service
        return None
    
    def _get_cache_path(self, year: int, make: str, model: str, service: str) -> Path:
        """Generate file path for cached document"""
        # Clean names for filesystem
        make_clean = make.replace(' ', '_').replace('/', '_')
        model_clean = model.split('(')[0].strip().replace(' ', '_').replace('/', '_')
        service_clean = service.replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')
        
        # Create directory structure: cache_dir/Make/Model/
        doc_dir = self.cache_dir / make_clean / model_clean
        doc_dir.mkdir(parents=True, exist_ok=True)
        
        # File: Year_Service.html
        filename = f"{year}_{service_clean}.html"
        return doc_dir / filename
    
    def _check_cache(self, cache_key: str) -> Optional[Path]:
        """Check if document exists in cache"""
        if cache_key in self.cache_index:
            cache_entry = self.cache_index[cache_key]
            doc_path = Path(cache_entry['path'])
            if doc_path.exists():
                return doc_path
        return None
    
    def generate(
        self,
        year: int,
        make: str,
        model: str,
        service: str,
        force_regenerate: bool = False
    ) -> Tuple[Path, bool]:
        """
        Generate service documentation
        
        Returns:
            (document_path, from_cache) tuple
        """
        # Generate cache key
        cache_key = self._generate_cache_key(year, make, model, service)
        
        # Check cache first
        if not force_regenerate:
            cached_path = self._check_cache(cache_key)
            if cached_path:
                print(f"✓ Using cached document: {cached_path}")
                return cached_path, True
        
        print(f"⚡ Generating new document for {year} {make} {model} - {service}")
        
        # Get vehicle and service data
        vehicle_data = self._get_vehicle_data(year, make, model)
        service_data = self._get_service_data(service)
        
        if not vehicle_data:
            raise ValueError(f"Vehicle not found: {year} {make} {model}")
        if not service_data:
            raise ValueError(f"Service not found: {service}")
        
        # Research with AI
        research_data = self._research_service(vehicle_data, service_data)
        
        # Generate diagrams if enabled and needed
        diagram_paths = {}
        if self.diagram_generator and research_data.get('diagrams'):
            diagram_paths = self._generate_diagrams(
                research_data['diagrams'],
                {'year': year, 'make': make, 'model': model}
            )
        
        # Generate HTML document
        doc_path = self._get_cache_path(year, make, model, service)
        self._generate_html(vehicle_data, service_data, research_data, doc_path, diagram_paths)
        
        # Update cache index
        self.cache_index[cache_key] = {
            'path': str(doc_path),
            'year': year,
            'make': make,
            'model': model,
            'service': service,
            'generated': datetime.now().isoformat(),
            'vehicle_difficulty': vehicle_data.get('difficulty_modifier', 1.0)
        }
        self._save_cache_index()
        
        print(f"✓ Document generated: {doc_path}")
        return doc_path, False
    
    def _research_service(self, vehicle_data: Dict, service_data: Dict) -> Dict:
        """Use AI to research service details"""
        
        # Build research prompt
        prompt = self._build_research_prompt(vehicle_data, service_data)
        
        # Use research AI to gather information
        print(f"🔍 Researching with {self.research_ai.provider} ({self.research_ai.model})...")
        
        system_message = """You are an expert automotive technician creating service documentation. 
You MUST respond with ONLY valid JSON - no markdown code blocks, no explanatory text before or after, no preamble.
Start your response with { and end with }. Always provide accurate, specific information based on factory specifications."""
        
        response_text = self.research_ai.chat(prompt, system_message=system_message)
        
        # Try to parse JSON from response
        research_data = self.research_ai.extract_json(response_text)
        
        if not research_data:
            # Fallback: create basic structure from raw text
            print("⚠️  Could not parse JSON from AI response, using fallback structure")
            print(f"    Response preview: {response_text[:200]}...")
            
            # Try to salvage something useful
            research_data = {
                "procedure": [
                    {
                        "step": 1, 
                        "description": "Consult vehicle service manual for detailed procedure", 
                        "time_minutes": 30
                    }
                ],
                "torque_specs": [],
                "special_tools": [],
                "parts_list": [],
                "common_issues": [],
                "safety_warnings": [
                    "Always consult vehicle service manual",
                    "Wear appropriate safety equipment",
                    "Use proper jack stands - never rely on jack alone"
                ],
                "tips": [],
                "diagrams": [],
                "citations": [],
                "error": "Could not parse AI response - manual verification required"
            }
        else:
            print(f"✓ Successfully parsed service data with {len(research_data.get('procedure', []))} steps")
            
            # Validate torque specs - warn if placeholders detected
            torque_specs = research_data.get('torque_specs', [])
            for spec in torque_specs:
                value = spec.get('value', '')
                if '{' in value or 'value' in value.lower() or not value or value == 'N/A':
                    print(f"  ⚠️  WARNING: Placeholder torque spec detected for '{spec.get('component', 'unknown')}': {value}")
                    print(f"      This should be a real value like '27 ft-lbs', not a placeholder")
        
        return research_data
    
    def _build_research_prompt(self, vehicle_data: Dict, service_data: Dict) -> str:
        """Build detailed research prompt for AI"""
        year = vehicle_data['years'][-1]  # Use latest year
        make = vehicle_data['make']
        model = vehicle_data['model']
        engines = ', '.join(vehicle_data.get('engines', []))
        transmissions = ', '.join(vehicle_data.get('transmissions', []))
        
        service_name = service_data.get('name') or service_data.get('service_name', 'Unknown Service')
        category = service_data.get('category', 'N/A')
        labor_time = service_data.get('labor_time_hours') or service_data.get('est_labor_hours', 0)
        
        prompt = f"""Create a detailed service guide for this specific vehicle and service.

VEHICLE INFORMATION:
- Year: {year}
- Make: {make}
- Model: {model}
- Engines: {engines}
- Transmissions: {transmissions}
- Difficulty Modifier: {vehicle_data.get('difficulty_modifier', 1.0)}
- Notes: {vehicle_data.get('notes', 'N/A')}

SERVICE INFORMATION:
- Service: {service_name}
- Category: {category}
- Estimated Labor Time: {labor_time} hours
- Service Notes: {service_data.get('notes', 'N/A')}

Research and provide the following in JSON format ONLY (no explanatory text, just the JSON):

1. STEP-BY-STEP PROCEDURE (detailed, numbered steps)
2. TORQUE SPECIFICATIONS (all critical bolts/fasteners with EXACT factory specs - DO NOT USE GENERIC VALUES)
   - CRITICAL: Research actual manufacturer torque specifications
   - Example: Oil drain plugs are typically 25-33 ft-lbs for most vehicles, but VERIFY for this specific model
   - Wheel lug nuts vary by vehicle (typically 70-110 ft-lbs depending on vehicle size)
   - Always specify the exact value from factory service manual if available
3. SPECIAL TOOLS REQUIRED (specific to this vehicle)
4. PARTS LIST (OEM part numbers if available)
5. COMMON ISSUES & TROUBLESHOOTING (specific to this model/year)
6. SAFETY WARNINGS (critical safety information)
7. TIME BREAKDOWN (realistic time per major step)
8. TIPS & TRICKS (professional insights)
9. DIAGRAMS NEEDED (identify where diagrams would be helpful)

Return ONLY valid JSON in exactly this structure (no markdown, no preamble, no explanation):
{{
    "procedure": [
        {{"step": 1, "description": "Clear detailed step description", "time_minutes": 5, "torque_spec": "27 ft-lbs (if applicable)", "needs_diagram": false}},
        {{"step": 2, "description": "Next step...", "time_minutes": 10, "needs_diagram": false}}
    ],
    "torque_specs": [
        {{"component": "Oil drain plug", "value": "27 ft-lbs", "pattern": "Straight", "notes": "Verify torque - critical specification"}},
        {{"component": "Oil filter housing", "value": "18 ft-lbs", "pattern": "Hand-tighten then 3/4 turn"}},
        {{"component": "Wheel lug nuts", "value": "76 ft-lbs", "pattern": "Star pattern"}}
    ],
    "special_tools": ["Torque wrench (0-150 ft-lbs)", "Oil filter wrench", "Jack and jack stands"],
    "parts_list": [
        {{"name": "Engine oil (5W-30 synthetic)", "oem_number": "00279-0WQTE-01", "qty": 1}},
        {{"name": "Oil filter", "oem_number": "04152-YZZA6", "qty": 1}},
        {{"name": "Drain plug washer", "oem_number": "90430-12031", "qty": 1}}
    ],
    "common_issues": [
        "**Oil leaks from drain plug**: Often caused by worn or reused crush washer. Always replace washer at each service. If threads are damaged, consider using an oversized drain plug or helicoil insert.",
        "**Stripped drain plug threads**: If overtorqued or cross-threaded during previous service. Use correct 14mm socket and verify torque. Consider oil pan replacement if severe.",
        "**Incorrect oil viscosity**: Using wrong oil grade can affect engine performance and fuel economy. Verify correct viscosity in owner's manual (typically 0W-20 or 5W-30 for this model)."
    ],
    "safety_warnings": ["Never work under vehicle supported only by jack", "Use proper jack stands", "Allow engine to cool before draining oil", "Wear gloves and eye protection"],
    "tips": ["Replace drain plug washer every oil change", "Hand-tighten oil filter first, then 3/4 turn with wrench", "Run engine for 30 seconds after refilling, then check for leaks"],
    "diagrams": [
        {{"step": 2, "description": "Oil drain plug location and orientation"}},
        {{"step": 5, "description": "Oil filter mounting and removal"}}
    ],
    "citations": ["https://www.toyota.com/owners/resources/warranty-owners-manuals"]
}}

CRITICAL REQUIREMENTS:
1. Use REAL NUMBERS for all torque specifications - NO PLACEHOLDERS like "25-30" or "{{value}}"
2. Each torque spec must have an EXACT value like "27 ft-lbs" or "18 ft-lbs"
3. Use actual OEM part numbers when available
4. All specifications must be specific to the {year} {make} {model}
5. Oil drain plugs are typically 25-33 ft-lbs depending on vehicle - research the specific value
6. Common issues must include DETAILED descriptions with causes, symptoms, and solutions (use bold **Issue**: format)
7. Return ONLY the JSON - no extra text before or after
"""
        return prompt
    
    def _generate_diagrams(self, diagram_specs: List[Dict], vehicle_context: Dict) -> Dict[int, str]:
        """
        Generate diagrams for specified steps
        
        Args:
            diagram_specs: List of diagram specifications from research
            vehicle_context: Vehicle information for context
            
        Returns:
            Dict mapping step numbers to diagram file paths
        """
        diagram_paths = {}
        
        print(f"🎨 Generating {len(diagram_specs)} diagrams...")
        
        for spec in diagram_specs:
            step = spec.get('step')
            description = spec.get('description', '')
            
            if not description or not step:
                continue
            
            try:
                # Generate diagram
                diagram_path = self.diagram_generator.generate_diagram(
                    description,
                    vehicle_context,
                    style="technical"
                )
                
                if diagram_path:
                    diagram_paths[step] = diagram_path
                    print(f"  ✅ Step {step} diagram generated")
                else:
                    print(f"  ⚠️  Step {step} diagram generation failed")
            
            except Exception as e:
                print(f"  ❌ Error generating diagram for step {step}: {e}")
        
        return diagram_paths
    
    def _generate_html(
        self,
        vehicle_data: Dict,
        service_data: Dict,
        research_data: Dict,
        output_path: Path,
        diagram_paths: Dict[int, str] = None
    ):
        """Generate professional HTML document"""
        
        if diagram_paths is None:
            diagram_paths = {}
        
        year = vehicle_data['years'][-1]
        make = vehicle_data['make']
        model = vehicle_data['model']
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{year} {make} {model} - {service_data.get('name') or service_data.get('service_name', 'Service')} | Swoop Service Auto</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Arial', sans-serif;
            line-height: 1.6;
            color: #1a1a1a;
            background: #e0e0e0;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: #ffffff;
            border: 2px solid #3a3a3a;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            border-radius: 12px;
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
            color: #ffffff;
            padding: 24px 30px;
            border-bottom: 5px solid #d32f2f;
        }}
        
        .header h1 {{
            font-size: 24px;
            margin-bottom: 6px;
            font-weight: 700;
            letter-spacing: 0.3px;
        }}
        
        .header .subtitle {{
            font-size: 11px;
            color: #b8b8b8;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            font-weight: 600;
        }}
        
        .content {{
            padding: 28px;
            background: #f5f5f5;
        }}
        
        .vehicle-info {{
            background: #ffffff;
            border: 2px solid #4a4a4a;
            padding: 0;
            margin-bottom: 24px;
            border-radius: 10px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.12);
            overflow: hidden;
        }}
        
        .vehicle-info h2 {{
            color: #ffffff;
            font-size: 14px;
            margin: 0;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            background: linear-gradient(135deg, #3a3a3a 0%, #1e1e1e 100%);
            padding: 14px 20px;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 14px 20px;
            padding: 20px;
        }}
        
        .info-item {{
            display: flex;
            flex-direction: column;
        }}
        
        .info-label {{
            font-weight: 700;
            color: #666666;
            font-size: 10px;
            text-transform: uppercase;
            margin-bottom: 6px;
            letter-spacing: 0.6px;
        }}
        
        .info-value {{
            color: #1a1a1a;
            font-size: 14px;
            font-weight: 600;
            background: #f0f0f0;
            padding: 8px 12px;
            border-radius: 6px;
            border: 1px solid #d0d0d0;
        }}
        
        .service-overview {{
            background: linear-gradient(135deg, #fff9e6 0%, #fff3d4 100%);
            border: 2px solid #d4a600;
            border-left: 6px solid #d32f2f;
            padding: 18px;
            margin-bottom: 24px;
            border-radius: 10px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.1);
        }}
        
        .service-overview h2 {{
            color: #1a1a1a;
            font-size: 15px;
            margin-bottom: 14px;
            font-weight: 700;
            text-transform: uppercase;
        }}
        
        .section {{
            margin-bottom: 22px;
            background: #ffffff;
            padding: 16px;
            border: 2px solid #d0d0d0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        }}
        
        .section h3 {{
            color: #1a1a1a;
            font-size: 14px;
            margin-bottom: 14px;
            padding-bottom: 10px;
            border-bottom: 3px solid #d32f2f;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }}
        
        .procedure-step {{
            background: #f8f8f8;
            padding: 14px;
            margin-bottom: 12px;
            border: 1px solid #d5d5d5;
            border-left: 5px solid #3a3a3a;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        }}
        
        .step-number {{
            display: inline-block;
            background: linear-gradient(135deg, #3a3a3a 0%, #1e1e1e 100%);
            color: #ffffff;
            min-width: 32px;
            height: 32px;
            line-height: 32px;
            text-align: center;
            font-weight: 700;
            margin-right: 12px;
            font-size: 14px;
            border-radius: 6px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.15);
        }}
        
        .step-description {{
            display: inline;
            font-size: 13px;
            color: #1a1a1a;
            font-weight: 500;
            line-height: 1.6;
        }}
        
        .step-meta {{
            margin-top: 10px;
            font-size: 11px;
            color: #666666;
            font-weight: 600;
            padding-left: 44px;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }}
        
        .torque-spec {{
            background: #f4f4f4;
            padding: 12px 14px;
            margin-bottom: 10px;
            border: 1px solid #d0d0d0;
            border-left: 4px solid #d32f2f;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        }}
        
        .torque-component {{
            font-weight: 600;
            color: #1a1a1a;
            font-size: 13px;
        }}
        
        .torque-value {{
            color: #d32f2f;
            font-weight: 700;
            font-size: 15px;
            font-family: 'Courier New', monospace;
            background: #ffffff;
            padding: 4px 10px;
            border-radius: 4px;
            border: 1px solid #d32f2f;
        }}
        
        .warning {{
            background: #ffebee;
            border: 2px solid #d32f2f;
            border-left: 6px solid #b71c1c;
            padding: 14px;
            margin-bottom: 12px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(211, 47, 47, 0.15);
        }}
        
        .warning-icon {{
            display: inline-block;
            background: #d32f2f;
            color: white;
            padding: 5px 10px;
            font-weight: 700;
            font-size: 11px;
            margin-right: 10px;
            border-radius: 5px;
        }}
        
        .tip {{
            background: #e8f5e9;
            border: 2px solid #4caf50;
            border-left: 6px solid #2e7d32;
            padding: 12px 14px;
            margin-bottom: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(76, 175, 80, 0.15);
        }}
        
        .tip-icon {{
            display: inline-block;
            background: #4caf50;
            color: white;
            padding: 5px 10px;
            font-weight: 700;
            font-size: 11px;
            margin-right: 10px;
            border-radius: 5px;
        }}
        
        .parts-list {{
            background: #ffffff;
            border: 1px solid #d0d0d0;
            border-radius: 4px;
            overflow: hidden;
        }}
        
        .part-item {{
            padding: 10px 12px;
            border-bottom: 1px solid #e0e0e0;
            display: flex;
            align-items: center;
            background: #fafafa;
        }}
        
        .part-item:last-child {{
            border-bottom: none;
        }}
        
        .part-item:nth-child(even) {{
            background: #ffffff;
        }}
        
        .part-checkbox {{
            margin-right: 10px;
            width: 16px;
            height: 16px;
        }}
        
        .part-name {{
            flex: 1;
            font-weight: 600;
            color: #1a1a1a;
            font-size: 12px;
        }}
        
        .part-number {{
            color: #666666;
            font-size: 11px;
            font-weight: 400;
            font-family: 'Courier New', monospace;
        }}
        
        .issue-item {{
            background: #fff8e1;
            padding: 14px;
            margin-bottom: 10px;
            border-radius: 8px;
            border-left: 5px solid #ff9800;
            color: #1a1a1a;
            font-size: 13px;
            font-weight: 500;
            line-height: 1.6;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        }}
        
        .issue-item strong {{
            color: #1a1a1a;
        }}
        
        .footer {{
            background: linear-gradient(135deg, #1a1a1a 0%, #2c2c2c 100%);
            color: #d0d0d0;
            padding: 15px 25px;
            text-align: center;
            border-top: 4px solid #cc0000;
        }}
        
        .watermark {{
            color: #999999;
            font-size: 10px;
            margin-bottom: 8px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .citations {{
            margin-top: 12px;
            font-size: 10px;
            color: #999999;
            text-align: left;
        }}
        
        .citations a {{
            color: #ff6666;
            text-decoration: none;
        }}
        
        .diagram-placeholder {{
            background: #f5f5f5;
            border: 2px dashed #999999;
            padding: 30px 15px;
            margin: 12px 0;
            text-align: center;
            color: #666666;
            border-radius: 6px;
        }}
        
        .diagram-placeholder svg {{
            width: 48px;
            height: 48px;
            margin-bottom: 8px;
            opacity: 0.4;
        }}
        
        .diagram-title {{
            font-weight: 700;
            font-size: 12px;
            color: #444444;
            margin-bottom: 4px;
            text-transform: uppercase;
        }}
        
        .diagram-note {{
            font-size: 10px;
            color: #777777;
            font-style: italic;
        }}
        
        @media print {{
            body {{ background: white; padding: 0; }}
            .container {{ box-shadow: none; border: 1px solid #000000; }}
            .procedure-step {{ page-break-inside: avoid; }}
        }}
        
        @media (max-width: 600px) {{
            body {{ padding: 5px; }}
            .content {{ padding: 15px; }}
            .header {{ padding: 15px; }}
            .info-grid {{ grid-template-columns: 1fr; }}
        }}
        
        @media (prefers-color-scheme: dark) {{
            body {{ background: #0a0a0a; color: #e0e0e0; }}
            .container {{ background: #1a1a1a; border-color: #444444; }}
            .content {{ background: #1a1a1a; }}
            .section {{ background: #252525; border-color: #444444; }}
            .section h3 {{ color: #ffffff; border-color: #cc0000; }}
            .procedure-step {{ background: #2a2a2a; border-color: #444444; color: #e0e0e0; }}
            .step-description {{ color: #e0e0e0; }}
            .step-meta {{ color: #999999; }}
            .vehicle-info {{ background: #252525; border-color: #444444; }}
            .vehicle-info h2 {{ background: linear-gradient(135deg, #2c2c2c 0%, #1a1a1a 100%); }}
            .info-label {{ color: #999999; }}
            .info-value {{ color: #e0e0e0; background: #2a2a2a; }}
            .service-overview {{ background: linear-gradient(135deg, #3a3a00 0%, #2a2a00 100%); border-color: #ccaa00; }}
            .service-overview h2 {{ color: #ffffff; }}
            .service-overview .info-value {{ background: #4a4a10; color: #ffffff; }}
            .torque-spec {{ background: #2a2a2a; border-color: #444444; }}
            .torque-component {{ color: #e0e0e0; }}
            .warning {{ background: #3a1a1a; border-color: #cc0000; }}
            .warning-icon {{ background: #ff3333; }}
            .tip {{ background: #1a2a1a; border-color: #4caf50; }}
            .tip-icon {{ background: #5cb85c; }}
            .parts-list {{ background: #252525; border-color: #444444; }}
            .part-item {{ background: #2a2a2a; border-color: #333333; }}
            .part-item:nth-child(even) {{ background: #252525; }}
            .part-name {{ color: #e0e0e0; }}
            .part-number {{ color: #999999; }}
            .issue-item {{ background: #3a3000; border-color: #ff9800; color: #f5f5f5; }}
            .issue-item strong {{ color: #ffffff; }}
            .diagram-placeholder {{ background: #252525; border-color: #555555; }}
            .diagram-title {{ color: #cccccc; }}
            .diagram-note {{ color: #888888; }}
        }}
        
        /* Mobile Responsive Design */
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            
            .header {{
                padding: 18px 16px;
            }}
            
            .header h1 {{
                font-size: 18px;
                line-height: 1.3;
            }}
            
            .header .subtitle {{
                font-size: 10px;
            }}
            
            .content {{
                padding: 16px;
            }}
            
            .section {{
                padding: 16px;
                margin-bottom: 16px;
            }}
            
            .section h3 {{
                font-size: 14px;
                padding: 10px 14px;
            }}
            
            .info-grid {{
                grid-template-columns: 1fr;
                gap: 12px;
                padding: 16px;
            }}
            
            .procedure-step {{
                padding: 12px;
            }}
            
            .step-number {{
                width: 32px;
                height: 32px;
                font-size: 14px;
                line-height: 32px;
                margin-right: 12px;
            }}
            
            .step-description {{
                font-size: 13px;
            }}
            
            .step-meta {{
                font-size: 11px;
                flex-direction: column;
                align-items: flex-start;
                gap: 4px;
            }}
            
            .torque-spec {{
                padding: 10px;
            }}
            
            .torque-component {{
                font-size: 13px;
            }}
            
            .torque-value {{
                font-size: 13px;
            }}
            
            .warning, .tip {{
                padding: 12px;
            }}
            
            .warning-icon, .tip-icon {{
                width: 32px;
                height: 32px;
                font-size: 16px;
                line-height: 32px;
            }}
            
            .part-item {{
                padding: 10px;
            }}
            
            .part-name {{
                font-size: 13px;
            }}
            
            .part-number {{
                font-size: 11px;
            }}
            
            .issue-item {{
                padding: 12px;
                font-size: 13px;
            }}
            
            table {{
                font-size: 12px;
            }}
            
            table th, table td {{
                padding: 8px 6px;
            }}
            
            /* Make tables horizontally scrollable on mobile */
            .section table {{
                display: block;
                overflow-x: auto;
                white-space: nowrap;
            }}
        }}
        
        @media (max-width: 480px) {{
            body {{
                padding: 8px;
            }}
            
            .header {{
                padding: 14px 12px;
            }}
            
            .header h1 {{
                font-size: 16px;
            }}
            
            .content {{
                padding: 12px;
            }}
            
            .section {{
                padding: 12px;
            }}
            
            .section h3 {{
                font-size: 13px;
                padding: 8px 12px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔧 SWOOP SERVICE AUTO</h1>
            <div class="subtitle">Professional Automotive Service Documentation</div>
        </div>
        
        <div class="content">
            <div class="vehicle-info">
                <h2>VEHICLE SPECIFICATION</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <span class="info-label">YEAR</span>
                        <span class="info-value">{year}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">MAKE</span>
                        <span class="info-value">{make}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">MODEL</span>
                        <span class="info-value">{model}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">ENGINE(S)</span>
                        <span class="info-value">{', '.join(vehicle_data.get('engines', ['N/A']))}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">TRANSMISSION(S)</span>
                        <span class="info-value">{', '.join(vehicle_data.get('transmissions', ['N/A']))}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">DRIVETRAIN</span>
                        <span class="info-value">{', '.join(vehicle_data.get('drivetrain', ['N/A']))}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">DIFFICULTY</span>
                        <span class="info-value">{vehicle_data.get('difficulty_modifier', 1.0)}x</span>
                    </div>
                </div>
            </div>
            
            <div class="service-overview">
                <h2>SERVICE: {service_data.get('name') or service_data.get('service_name', 'Service')}</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <span class="info-label">CATEGORY</span>
                        <span class="info-value">{service_data.get('category', 'N/A')}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">LABOR TIME</span>
                        <span class="info-value">{service_data.get('labor_time_hours') or service_data.get('est_labor_hours', 0)} HRS</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">LABOR RATE</span>
                        <span class="info-value">${service_data.get('labor_rate_local', 150)}/HR</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">SKILL LEVEL</span>
                        <span class="info-value">{service_data.get('skill_level', 'INTERMEDIATE')}</span>
                    </div>
                </div>
            </div>
            
            {self._render_safety_warnings(research_data.get('safety_warnings', []))}
            
            {self._render_procedure(research_data.get('procedure', []), diagram_paths)}
            
            {self._render_torque_specs(research_data.get('torque_specs', []))}
            
            {self._render_diagrams(research_data.get('diagrams', []), diagram_paths)}
            
            {self._render_parts_list(research_data.get('parts_list', []))}
            
            {self._render_special_tools(research_data.get('special_tools', []))}
            
            {self._render_common_issues(research_data.get('common_issues', []))}
            
            {self._render_tips(research_data.get('tips', []))}
        </div>
        
        <div class="footer">
            <div class="watermark">
                GENERATED BY SWOOP SERVICE AUTO AI DOCUMENTATION SYSTEM<br>
                {datetime.now().strftime('%B %d, %Y - %I:%M %p').upper()}
            </div>
            {self._render_citations(research_data.get('citations', []))}
        </div>
    </div>
</body>
</html>
"""
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
    
    def _render_safety_warnings(self, warnings: List[str]) -> str:
        if not warnings:
            return ""
        
        html = '<div class="section"><h3>⚠️ Safety Warnings</h3>'
        for warning in warnings:
            html += f'<div class="warning"><span class="warning-icon">⚠️</span>{warning}</div>'
        html += '</div>'
        return html
    
    def _render_procedure(self, steps: List[Dict], diagram_paths: Dict[int, str] = None) -> str:
        if not steps:
            return ""
        
        if diagram_paths is None:
            diagram_paths = {}
        
        html = '<div class="section"><h3>📋 Step-by-Step Procedure</h3>'
        for step in steps:
            step_num = step.get('step', 0)
            description = step.get('description', '')
            time = step.get('time_minutes', 0)
            torque = step.get('torque_spec', '')
            
            html += f'<div class="procedure-step">'
            html += f'<span class="step-number">{step_num}</span>'
            html += f'<span class="step-description">{description}</span>'
            
            meta = []
            if time:
                meta.append(f'⏱️ {time} min')
            if torque:
                meta.append(f'🔧 {torque}')
            
            if meta:
                html += f'<div class="step-meta">{" | ".join(meta)}</div>'
            
            # Add actual diagram if we have one for this step
            if step_num in diagram_paths:
                diagram_path = diagram_paths[step_num]
                try:
                    # Convert image to base64 data URL for embedding
                    base64_img = self._image_to_base64(diagram_path)
                    if base64_img:
                        html += f'''
                    <div style="margin-top: 12px; text-align: center;">
                        <img src="{base64_img}" alt="Diagram for step {step_num}" 
                             style="max-width: 100%; height: auto; border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
                    </div>
                    '''
                except Exception as e:
                    # If conversion fails, skip diagram
                    print(f"  ⚠️  Could not add diagram for step {step_num}: {e}")
            
            html += '</div>'
        
        html += '</div>'
        return html
    
    def _render_torque_specs(self, specs: List[Dict]) -> str:
        if not specs:
            return ""
        
        html = '<div class="section"><h3>🔧 Torque Specifications</h3>'
        html += '<div style="background: #fff9e6; border: 2px solid #d4a600; border-left: 6px solid #ff6b00; padding: 14px; margin-bottom: 16px; border-radius: 8px;">'
        html += '<strong style="color: #1a1a1a;">⚠️ CRITICAL:</strong> <span style="color: #1a1a1a;">Always verify torque specifications in factory service manual. Incorrect torque can cause damage or safety issues.</span>'
        html += '</div>'
        
        for spec in specs:
            component = spec.get('component', '')
            value = spec.get('value', '')
            pattern = spec.get('pattern', 'N/A')
            notes = spec.get('notes', '')
            
            html += '<div class="torque-spec">'
            html += f'<div><span class="torque-component">{component}</span>'
            if notes:
                html += f'<div style="font-size: 11px; color: #ff6b00; font-weight: 600; margin-top: 4px;">⚠️ {notes}</div>'
            html += '</div>'
            html += f'<div style="text-align: right;"><span class="torque-value">{value}'
            if pattern != 'N/A':
                html += f' ({pattern})'
            html += '</span></div></div>'
        
        html += '</div>'
        return html
    
    def _render_parts_list(self, parts: List[Dict]) -> str:
        if not parts:
            return ""
        
        html = '<div class="section"><h3>🛠️ Required Parts</h3><div class="parts-list">'
        for part in parts:
            name = part.get('name', '')
            oem = part.get('oem_number', '')
            qty = part.get('qty', 1)
            
            html += '<div class="part-item">'
            html += '<input type="checkbox" class="part-checkbox">'
            html += f'<span class="part-name">{name} (x{qty})</span>'
            if oem:
                html += f'<span class="part-number">OEM: {oem}</span>'
            html += '</div>'
        
        html += '</div></div>'
        return html
    
    def _render_special_tools(self, tools: List[str]) -> str:
        if not tools:
            return ""
        
        html = '<div class="section"><h3>🔨 Special Tools Required</h3><ul style="list-style-position: inside; padding-left: 0;">'
        for tool in tools:
            html += f'<li style="padding: 8px 0; border-bottom: 1px solid #eee;">{tool}</li>'
        html += '</ul></div>'
        return html
    
    def _render_common_issues(self, issues: List[str]) -> str:
        if not issues:
            return ""
        
        html = '<div class="section"><h3>🔍 Common Issues & Troubleshooting</h3>'
        for issue in issues:
            # Convert markdown-style bold to HTML bold
            parts = issue.split('**')
            issue_html = ''
            for i, part in enumerate(parts):
                if i % 2 == 1:  # Odd indices should be bold
                    issue_html += f'<strong>{part}</strong>'
                else:
                    issue_html += part
            
            # Use CSS class for proper styling - ensure proper contrast
            html += f'<div class="issue-item">{issue_html}</div>'
        html += '</div>'
        return html
    
    def _render_tips(self, tips: List[str]) -> str:
        if not tips:
            return ""
        
        html = '<div class="section"><h3>💡 Pro Tips</h3>'
        for tip in tips:
            html += f'<div class="tip"><span class="tip-icon">💡</span>{tip}</div>'
        html += '</div>'
        return html
    
    def _render_diagrams(self, diagrams: List[Dict], diagram_paths: Dict[int, str] = None) -> str:
        """Render standalone diagram section - ONLY if diagrams have actual generated content"""
        if not diagrams:
            return ""
        
        if diagram_paths is None or len(diagram_paths) == 0:
            # No actual diagrams were generated, don't show this section at all
            return ""
        
        # Filter to only show diagrams that were actually generated
        real_diagrams = []
        for diagram in diagrams:
            step = diagram.get('step', '')
            description = diagram.get('description', '')
            
            # Only include if we have a real generated diagram for this step
            if step in diagram_paths and description and description.lower() not in ['placeholder', 'n/a', '']:
                real_diagrams.append(diagram)
        
        if not real_diagrams:
            return ""
        
        html = '<div class="section"><h3>📐 Reference Diagrams</h3>'
        html += '<div style="background: #e8f5e9; border: 2px solid #4caf50; border-left: 6px solid #2e7d32; padding: 14px; margin-bottom: 16px; border-radius: 8px;">'
        html += '<strong style="color: #1b5e20;">✓ AI-Generated Diagrams:</strong> <span style="color: #1b5e20;">Technical illustrations generated by AI to assist with this service procedure.</span>'
        html += '</div>'
        
        for diagram in real_diagrams:
            step = diagram.get('step', '')
            description = diagram.get('description', '')
            
            diagram_path = diagram_paths[step]
            try:
                # Convert image to base64 data URL for embedding
                base64_img = self._image_to_base64(diagram_path)
                if base64_img:
                    html += f'''
                <div style="margin-bottom: 20px; padding: 15px; background: #f9f9f9; border: 2px solid #ddd; border-radius: 8px;">
                    <div style="font-weight: 700; font-size: 13px; margin-bottom: 10px; color: #333;">
                        📐 {description} (Step {step})
                    </div>
                    <img src="{base64_img}" alt="{description}" 
                         style="max-width: 100%; height: auto; border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
                </div>
                '''
            except Exception as e:
                print(f"  ⚠️  Could not add diagram for standalone section: {e}")
        
        html += '</div>'
        return html
    
    def _render_citations(self, citations: List[str]) -> str:
        if not citations:
            return ""
        
        html = '<div class="citations"><strong>Research Sources:</strong><br>'
        for i, citation in enumerate(citations, 1):
            if citation.startswith('http'):
                html += f'{i}. <a href="{citation}" target="_blank">{citation}</a><br>'
            else:
                html += f'{i}. {citation}<br>'
        html += '</div>'
        return html


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate service documentation')
    parser.add_argument('--year', type=int, required=True, help='Vehicle year')
    parser.add_argument('--make', required=True, help='Vehicle make')
    parser.add_argument('--model', required=True, help='Vehicle model')
    parser.add_argument('--service', required=True, help='Service name')
    parser.add_argument('--force', action='store_true', help='Force regenerate')
    
    args = parser.parse_args()
    
    generator = ServiceDocGenerator()
    
    try:
        doc_path, from_cache = generator.generate(
            year=args.year,
            make=args.make,
            model=args.model,
            service=args.service,
            force_regenerate=args.force
        )
        
        print(f"\n{'📋' if from_cache else '✨'} Document ready: {doc_path}")
        print(f"{'(from cache)' if from_cache else '(newly generated)'}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise


if __name__ == '__main__':
    main()
