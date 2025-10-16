#!/usr/bin/env python3
"""
AI Client - Unified interface for multiple AI providers
Swoop Service Auto - Standardized AI access across all tools
"""

import os
import json
import requests
from typing import Dict, Optional, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AIClient:
    """Unified AI client supporting multiple providers"""
    
    def __init__(self, purpose: str = "research"):
        """
        Initialize AI client for a specific purpose
        
        Args:
            purpose: "research" or "formatter" (determines which env vars to use)
        """
        self.purpose = purpose
        
        # Load configuration from environment
        if purpose == "research":
            self.provider = os.getenv("RESEARCH_AI_PROVIDER", "perplexity").lower()
            self.model = os.getenv("RESEARCH_AI_MODEL", "sonar-pro")
            self.temperature = float(os.getenv("RESEARCH_TEMPERATURE", "0.2"))
            self.max_tokens = int(os.getenv("RESEARCH_MAX_TOKENS", "4000"))
        elif purpose == "formatter":
            self.provider = os.getenv("FORMATTER_AI_PROVIDER", "openai").lower()
            self.model = os.getenv("FORMATTER_AI_MODEL", "gpt-4o-mini")
            self.temperature = float(os.getenv("FORMATTER_TEMPERATURE", "0.3"))
            self.max_tokens = int(os.getenv("FORMATTER_MAX_TOKENS", "8000"))
        else:
            raise ValueError(f"Unknown purpose: {purpose}. Use 'research' or 'formatter'")
        
        # Get API key for selected provider
        self.api_key = self._get_api_key()
        if not self.api_key:
            raise ValueError(f"API key not found for {self.provider}. Set {self.provider.upper()}_API_KEY in .env")
        
        # Get API endpoint
        self.api_url = self._get_api_url()
    
    def _get_api_key(self) -> Optional[str]:
        """Get API key for the configured provider"""
        key_map = {
            "perplexity": "PERPLEXITY_API_KEY",
            "openai": "OPENAI_API_KEY",
            "anthropic": "ANTHROPIC_API_KEY",
            "openrouter": "OPENROUTER_API_KEY"
        }
        env_var = key_map.get(self.provider)
        return os.getenv(env_var) if env_var else None
    
    def _get_api_url(self) -> str:
        """Get API endpoint for the configured provider"""
        url_map = {
            "perplexity": os.getenv("PERPLEXITY_API_URL", "https://api.perplexity.ai/chat/completions"),
            "openai": os.getenv("OPENAI_API_URL", "https://api.openai.com/v1/chat/completions"),
            "openrouter": os.getenv("OPENROUTER_API_URL", "https://openrouter.ai/api/v1/chat/completions"),
            "anthropic": "https://api.anthropic.com/v1/messages"
        }
        return url_map.get(self.provider, "")
    
    def chat(
        self,
        prompt: str,
        system_message: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Send a chat request to the AI provider
        
        Args:
            prompt: User prompt/question
            system_message: Optional system message to set context
            temperature: Override default temperature
            max_tokens: Override default max tokens
            
        Returns:
            AI response text
        """
        # Use configured defaults if not overridden
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens
        
        # Route to appropriate provider
        if self.provider == "anthropic":
            return self._call_anthropic(prompt, system_message, temp, tokens)
        else:
            return self._call_openai_compatible(prompt, system_message, temp, tokens)
    
    def _call_anthropic(
        self,
        prompt: str,
        system_message: Optional[str],
        temperature: float,
        max_tokens: int
    ) -> str:
        """Call Anthropic Claude API"""
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        if system_message:
            payload["system"] = system_message
        
        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        return result["content"][0]["text"]
    
    def _call_openai_compatible(
        self,
        prompt: str,
        system_message: Optional[str],
        temperature: float,
        max_tokens: int
    ) -> str:
        """Call OpenAI-compatible APIs (OpenAI, Perplexity, OpenRouter)"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        # Add provider-specific parameters
        if self.provider == "openrouter":
            payload["site_url"] = "https://swoopserviceauto.com"
            payload["site_name"] = "Swoop Service Auto"
        
        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]
    
    def extract_json(self, text: str) -> Optional[Dict]:
        """
        Extract JSON from AI response (handles markdown code blocks)
        
        Args:
            text: Response text that may contain JSON
            
        Returns:
            Parsed JSON dict or None if parsing fails
        """
        try:
            # Try to extract from markdown code blocks
            if "```json" in text:
                json_str = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                json_str = text.split("```")[1].split("```")[0].strip()
            else:
                # Try to find JSON object boundaries
                start = text.find("{")
                end = text.rfind("}") + 1
                if start >= 0 and end > start:
                    json_str = text[start:end]
                else:
                    json_str = text
            
            return json.loads(json_str)
        
        except (json.JSONDecodeError, IndexError):
            return None
    
    def get_info(self) -> Dict:
        """Get information about current configuration"""
        return {
            "purpose": self.purpose,
            "provider": self.provider,
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "api_url": self.api_url,
            "has_api_key": bool(self.api_key)
        }


def test_connection(purpose: str = "research") -> bool:
    """
    Test AI connection
    
    Args:
        purpose: "research" or "formatter"
        
    Returns:
        True if connection successful
    """
    try:
        client = AIClient(purpose=purpose)
        
        print(f"Testing {purpose} AI connection...")
        print(f"  Provider: {client.provider}")
        print(f"  Model: {client.model}")
        
        response = client.chat("Say 'OK' if you can hear me.", max_tokens=10)
        
        print(f"  Response: {response[:50]}...")
        print(f"  ✅ Connection successful!")
        
        return True
    
    except Exception as e:
        print(f"  ❌ Connection failed: {e}")
        return False


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("="*60)
        print("AI CLIENT CONNECTION TEST")
        print("="*60)
        print()
        
        # Test research AI
        research_ok = test_connection("research")
        print()
        
        # Test formatter AI
        formatter_ok = test_connection("formatter")
        print()
        
        if research_ok and formatter_ok:
            print("="*60)
            print("✅ All AI connections successful!")
            print("="*60)
            sys.exit(0)
        else:
            print("="*60)
            print("❌ Some connections failed. Check your .env file.")
            print("="*60)
            sys.exit(1)
    
    else:
        # Show current configuration
        print("="*60)
        print("AI CLIENT CONFIGURATION")
        print("="*60)
        print()
        
        for purpose in ["research", "formatter"]:
            try:
                client = AIClient(purpose=purpose)
                info = client.get_info()
                
                print(f"{purpose.upper()}:")
                print(f"  Provider: {info['provider']}")
                print(f"  Model: {info['model']}")
                print(f"  Temperature: {info['temperature']}")
                print(f"  Max Tokens: {info['max_tokens']}")
                print(f"  Has API Key: {info['has_api_key']}")
                print()
            
            except Exception as e:
                print(f"{purpose.upper()}: ❌ {e}")
                print()
        
        print("="*60)
        print("Run 'python ai_client.py test' to test connections")
        print("="*60)
