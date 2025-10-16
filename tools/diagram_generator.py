#!/usr/bin/env python3
"""
Diagram Generator for Service Documentation
Generates technical diagrams for automotive service procedures
"""

import os
import base64
import requests
from pathlib import Path
from typing import Optional, Dict
from dotenv import load_dotenv

load_dotenv()


class DiagramGenerator:
    """Generate technical diagrams for service documentation"""
    
    def __init__(self, provider: str = None):
        """
        Initialize diagram generator
        
        Args:
            provider: "openai" or "stability" (defaults to env DIAGRAM_AI_PROVIDER)
        """
        self.provider = provider or os.getenv("DIAGRAM_AI_PROVIDER", "openai").lower()
        self.api_key = self._get_api_key()
        
        if not self.api_key:
            raise ValueError(f"API key not found for {self.provider}. Set {self.provider.upper()}_API_KEY in .env")
        
        # Configuration
        self.cache_dir = Path(os.getenv("DIAGRAM_CACHE_DIR", "service_docs/diagrams"))
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def _get_api_key(self) -> Optional[str]:
        """Get API key for the configured provider"""
        key_map = {
            "openai": "OPENAI_API_KEY",
            "stability": "STABILITY_API_KEY",
            "together": "TOGETHER_API_KEY"
        }
        env_var = key_map.get(self.provider)
        return os.getenv(env_var) if env_var else None
    
    def generate_diagram(
        self,
        description: str,
        vehicle_context: Dict,
        style: str = "technical"
    ) -> Optional[str]:
        """
        Generate a technical diagram
        
        Args:
            description: What the diagram should show
            vehicle_context: Dict with year, make, model, etc.
            style: "technical", "schematic", or "photo-realistic"
            
        Returns:
            Path to saved diagram image or None if generation fails
        """
        # Build detailed prompt
        prompt = self._build_diagram_prompt(description, vehicle_context, style)
        
        # Generate based on provider
        if self.provider == "openai":
            return self._generate_openai(prompt, description)
        elif self.provider == "stability":
            return self._generate_stability(prompt, description)
        elif self.provider == "together":
            return self._generate_together(prompt, description)
        else:
            print(f"⚠️  Unknown provider: {self.provider}")
            return None
    
    def _build_diagram_prompt(
        self,
        description: str,
        vehicle_context: Dict,
        style: str
    ) -> str:
        """Build detailed prompt for diagram generation"""
        
        year = vehicle_context.get('year', '')
        make = vehicle_context.get('make', '')
        model = vehicle_context.get('model', '')
        
        style_hints = {
            "technical": "Technical illustration style, clean lines, labeled components, cutaway view, automotive service manual style",
            "schematic": "Schematic diagram, simple line art, clear labels, black and white technical drawing",
            "photo-realistic": "Photo-realistic 3D render, professional automotive photography lighting"
        }
        
        style_hint = style_hints.get(style, style_hints["technical"])
        
        prompt = f"""Technical automotive service diagram: {description}
        
Vehicle: {year} {make} {model}

Style: {style_hint}

Requirements:
- Clear, professional automotive technical illustration
- Visible component labels and callouts
- Accurate mechanical detail
- Service manual quality
- No text in decorative fonts
- Clean white or light gray background
- Focus on mechanical accuracy
- Appropriate for professional mechanic use

Create a clear, labeled diagram showing: {description}"""
        
        return prompt
    
    def _generate_openai(self, prompt: str, description: str) -> Optional[str]:
        """Generate diagram using OpenAI DALL-E"""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Use DALL-E 3 for better quality, or DALL-E 2 for cheaper
            model = os.getenv("OPENAI_IMAGE_MODEL", "dall-e-3")
            size = "1024x1024"  # Standard size
            quality = "standard"  # "standard" or "hd"
            
            payload = {
                "model": model,
                "prompt": prompt[:4000],  # DALL-E has prompt limits
                "n": 1,
                "size": size,
                "quality": quality
            }
            
            print(f"  🎨 Generating diagram with OpenAI {model}...")
            
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            image_url = result["data"][0]["url"]
            
            # Download and save image
            return self._download_and_save_image(image_url, description)
        
        except Exception as e:
            print(f"  ❌ OpenAI diagram generation failed: {e}")
            return None
    
    def _generate_stability(self, prompt: str, description: str) -> Optional[str]:
        """Generate diagram using Stability AI"""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json"
            }
            
            # Use Stable Diffusion XL
            model = os.getenv("STABILITY_MODEL", "stable-diffusion-xl-1024-v1-0")
            
            payload = {
                "text_prompts": [
                    {
                        "text": prompt,
                        "weight": 1.0
                    },
                    {
                        "text": "blurry, low quality, text overlay, watermark, photo, realistic photo",
                        "weight": -0.5
                    }
                ],
                "cfg_scale": 7,
                "height": 1024,
                "width": 1024,
                "samples": 1,
                "steps": 30,
                "style_preset": "digital-art"
            }
            
            print(f"  🎨 Generating diagram with Stability AI...")
            
            response = requests.post(
                f"https://api.stability.ai/v1/generation/{model}/text-to-image",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            
            # Stability returns base64 encoded image
            image_data = base64.b64decode(result["artifacts"][0]["base64"])
            
            # Save image
            return self._save_image_data(image_data, description)
        
        except Exception as e:
            print(f"  ❌ Stability AI diagram generation failed: {e}")
            return None
    
    def _generate_together(self, prompt: str, description: str) -> Optional[str]:
        """Generate diagram using Together AI (cheap FLUX model)"""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Use FLUX.1-schnell for speed and cost-effectiveness
            model = os.getenv("TOGETHER_IMAGE_MODEL", "black-forest-labs/FLUX.1-schnell")
            
            payload = {
                "model": model,
                "prompt": prompt,
                "width": 1024,
                "height": 1024,
                "steps": 4,  # Schnell is optimized for 4 steps
                "n": 1
            }
            
            print(f"  🎨 Generating diagram with Together AI...")
            
            response = requests.post(
                "https://api.together.xyz/v1/images/generations",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            image_url = result["data"][0]["url"]
            
            # Download and save image
            return self._download_and_save_image(image_url, description)
        
        except Exception as e:
            print(f"  ❌ Together AI diagram generation failed: {e}")
            return None
    
    def _download_and_save_image(self, url: str, description: str) -> Optional[str]:
        """Download image from URL and save to cache"""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            return self._save_image_data(response.content, description)
        
        except Exception as e:
            print(f"  ❌ Failed to download image: {e}")
            return None
    
    def _save_image_data(self, image_data: bytes, description: str) -> str:
        """Save image data to file"""
        # Create safe filename from description
        safe_desc = "".join(c for c in description if c.isalnum() or c in (' ', '-', '_'))
        safe_desc = safe_desc.replace(' ', '_')[:50]
        
        # Generate unique filename
        import hashlib
        hash_suffix = hashlib.md5(description.encode()).hexdigest()[:8]
        filename = f"{safe_desc}_{hash_suffix}.png"
        
        filepath = self.cache_dir / filename
        
        with open(filepath, 'wb') as f:
            f.write(image_data)
        
        print(f"  ✅ Diagram saved: {filepath}")
        return str(filepath)


def test_generation():
    """Test diagram generation"""
    print("="*60)
    print("DIAGRAM GENERATOR TEST")
    print("="*60)
    print()
    
    try:
        generator = DiagramGenerator()
        
        print(f"Provider: {generator.provider}")
        print(f"Cache dir: {generator.cache_dir}")
        print()
        
        # Test generation
        vehicle = {
            "year": 2020,
            "make": "Toyota",
            "model": "Camry"
        }
        
        description = "Brake caliper bolt locations showing proper torque sequence"
        
        print(f"Generating test diagram: {description}")
        result = generator.generate_diagram(description, vehicle)
        
        if result:
            print(f"✅ Success! Diagram saved to: {result}")
        else:
            print("❌ Generation failed")
    
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_generation()
    else:
        print("Usage: python diagram_generator.py test")
