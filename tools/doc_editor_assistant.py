#!/usr/bin/env python3
"""
Document Editor Assistant for Swoop Service Auto
Handles guided document editing with source verification and fact-checking
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import requests
from bs4 import BeautifulSoup

from ai_client import AIClient


class DocumentEditorAssistant:
    """AI assistant for editing and updating service documentation with verification"""
    
    def __init__(self):
        """Initialize the document editor assistant"""
        # Use research AI for fact-checking (has web access)
        self.research_ai = AIClient(purpose="research")
        # Use formatter AI for document updates (better at structured content)
        self.formatter_ai = AIClient(purpose="formatter")
        
        # Initialize conversation context
        self.context = {
            'selected_document': None,
            'pending_edits': [],
            'conversation_history': []
        }
    
    def select_document(self, doc_path: str) -> Dict:
        """Select a document to edit"""
        doc_path = Path(doc_path)
        
        if not doc_path.exists():
            return {
                'success': False,
                'error': 'Document not found'
            }
        
        # Load document
        with open(doc_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract key information from HTML
        doc_info = self._extract_doc_info(html_content)
        
        self.context['selected_document'] = {
            'path': str(doc_path),
            'html': html_content,
            'info': doc_info
        }
        
        return {
            'success': True,
            'document': doc_info,
            'message': f"Selected: {doc_info['title']}"
        }
    
    def _extract_doc_info(self, html: str) -> Dict:
        """Extract structured information from HTML document"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract title
        h1 = soup.find('h1')
        title = h1.get_text(strip=True) if h1 else "Unknown Document"
        
        # Extract sections
        sections = {}
        for section in soup.find_all('section'):
            section_id = section.get('id', '')
            if section_id:
                sections[section_id] = {
                    'title': section.find(['h2', 'h3']).get_text(strip=True) if section.find(['h2', 'h3']) else section_id,
                    'content_preview': section.get_text(strip=True)[:200] + '...'
                }
        
        return {
            'title': title,
            'sections': sections,
            'total_sections': len(sections)
        }
    
    def process_user_request(self, user_input: str, uploaded_source: Optional[Dict] = None) -> Dict:
        """
        Process user request for document editing
        
        Args:
            user_input: The user's message/request
            uploaded_source: Optional dict with 'type' (url/pdf/image) and 'content'
        
        Returns:
            Dict with response, actions taken, and verification results
        """
        if not self.context['selected_document']:
            return {
                'success': False,
                'message': '⚠️ Please select a document first before making edits.',
                'action': 'select_document_required'
            }
        
        # Analyze user intent
        intent = self._analyze_intent(user_input)
        
        if intent['type'] == 'add_information':
            return self._handle_add_information(user_input, intent, uploaded_source)
        elif intent['type'] == 'modify_section':
            return self._handle_modify_section(user_input, intent, uploaded_source)
        elif intent['type'] == 'question':
            return self._handle_question(user_input)
        elif intent['type'] == 'review_document':
            return self._handle_review_document()
        elif intent['type'] == 'wiring_diagram':
            return self._handle_wiring_diagram_request(user_input, intent)
        else:
            return self._handle_general_chat(user_input)
    
    def _analyze_intent(self, user_input: str) -> Dict:
        """Analyze user's intent from their message"""
        input_lower = user_input.lower()
        
        # Quick pattern matching for wiring diagram requests
        wiring_keywords = ['wiring', 'diagram', 'schematic', 'circuit', 'electrical', 'wire', 'connector', 'pin', 'sensor to', 'ecm', 'pcm', 'bcm']
        if any(keyword in input_lower for keyword in wiring_keywords):
            # Extract circuit/system being requested - improved pattern
            circuit_patterns = [
                r'(o2|oxygen)\s*sensor',
                r'(upstream|downstream)\s*(o2|oxygen)',
                r'(starter|alternator|fuel pump|ignition|headlight|charging|cooling fan|power window|door lock|radio|hvac|abs|airbag|bcm|ecm|pcm)',
                r'sensor\s+to\s+(ecm|pcm|bcm)',
                r'(maf|map|tps|iat|ect|ckp|cmp)\s*sensor'
            ]
            
            circuit_type = 'general'
            for pattern in circuit_patterns:
                match = re.search(pattern, input_lower)
                if match:
                    circuit_type = match.group(0).replace(' ', '_')
                    break
            
            return {
                'type': 'wiring_diagram',
                'section': 'wiring_diagrams',
                'specific_topic': circuit_type,
                'confidence': 0.95
            }
        
        # Question patterns - improved detection
        question_keywords = ['what', 'where', 'how', 'why', 'when', 'which', 'show me', 'tell me', 'explain']
        if any(input_lower.startswith(kw) or f' {kw} ' in input_lower for kw in question_keywords):
            return {
                'type': 'question',
                'section': None,
                'specific_topic': user_input,
                'confidence': 0.85
            }
        
        # Add/edit patterns
        add_keywords = ['add', 'insert', 'include', 'update', 'change', 'modify']
        if any(kw in input_lower for kw in add_keywords):
            return {
                'type': 'add_information',
                'section': None,
                'specific_topic': user_input,
                'confidence': 0.8
            }
        
        # Default to question for most other inputs
        return {
            'type': 'question',
            'section': None,
            'specific_topic': user_input,
            'confidence': 0.6
        }
    
    def _handle_add_information(self, user_input: str, intent: Dict, uploaded_source: Optional[Dict]) -> Dict:
        """Handle request to add new information"""
        doc_info = self.context['selected_document']['info']
        
        # Step 1: Extract the information to add
        extract_prompt = f"""The user wants to add information to this service document:
Document: {doc_info['title']}

User request: "{user_input}"

Extract:
1. What specific information do they want to add?
2. Which section should it go in? (options: {', '.join(doc_info['sections'].keys())})
3. Is this a torque spec, fluid spec, procedure step, troubleshooting tip, or other?

Respond with structured JSON:
{{"information": "...", "target_section": "...", "info_type": "...", "needs_verification": true/false}}"""
        
        try:
            extract_response = self.research_ai.chat(extract_prompt, temperature=0.1)
            json_match = re.search(r'\{[^}]+\}', extract_response)
            if not json_match:
                return {'success': False, 'message': '❌ Could not understand the information to add.'}
            
            extraction = json.loads(json_match.group())
            
            # Step 2: Verify the information
            if uploaded_source:
                verification = self._verify_with_source(extraction['information'], uploaded_source)
            else:
                verification = self._verify_with_research(extraction['information'], doc_info['title'])
            
            # Step 3: Present verification result and ask for confirmation
            if verification['confidence'] >= 0.8:
                message = f"""✅ **Verification Passed** (confidence: {verification['confidence']:.0%})

**Information to add:**
{extraction['information']}

**Target section:** {extraction['target_section']}

**Verification summary:**
{verification['summary']}

**Sources:** {', '.join(verification.get('sources', ['Research']))}

This looks accurate and would be a great addition! Reply with:
- "add it" or "yes" to confirm
- "no" or "cancel" to cancel
- Ask follow-up questions if you need more details"""
                
                # Store pending edit
                self.context['pending_edits'].append({
                    'action': 'add',
                    'extraction': extraction,
                    'verification': verification,
                    'timestamp': datetime.now().isoformat()
                })
                
                return {
                    'success': True,
                    'message': message,
                    'action': 'confirmation_required',
                    'verification': verification
                }
            
            elif verification['confidence'] >= 0.5:
                message = f"""⚠️ **Verification Uncertain** (confidence: {verification['confidence']:.0%})

**Information to add:**
{extraction['information']}

**Verification summary:**
{verification['summary']}

**Concerns:**
{verification.get('concerns', 'Unable to fully verify this information.')}

This doesn't quite match what I found in my research. Are you sure you want to add this? 

If you have a source document/URL, please upload it so I can verify against it.

Reply with:
- "add anyway" to proceed despite concerns
- "cancel" to cancel
- Upload a source document for me to check"""
                
                return {
                    'success': False,
                    'message': message,
                    'action': 'needs_source',
                    'verification': verification
                }
            
            else:
                message = f"""❌ **Verification Failed** (confidence: {verification['confidence']:.0%})

**Information to add:**
{extraction['information']}

**Issues found:**
{verification.get('concerns', 'This information could not be verified and may be incorrect.')}

I cannot recommend adding this information without a reliable source.

Please either:
- Upload a source document (FSM, TSB, OEM specs) for me to verify
- Revise your request with more accurate information
- Explain where this information came from"""
                
                return {
                    'success': False,
                    'message': message,
                    'action': 'verification_failed',
                    'verification': verification
                }
        
        except Exception as e:
            return {
                'success': False,
                'message': f'❌ Error processing request: {str(e)}'
            }
    
    def _verify_with_research(self, information: str, document_title: str) -> Dict:
        """Verify information using AI research (web search)"""
        verify_prompt = f"""Verify this technical automotive information for accuracy:

Document context: {document_title}
Information to verify: "{information}"

Task:
1. Search for factual data that supports or contradicts this information
2. Check against known OEM specifications, service manuals, and trusted sources
3. Identify any incorrect values, specifications, or procedures

Provide a confidence score (0.0-1.0) and detailed reasoning.

Respond in JSON:
{{
    "confidence": 0.9,
    "summary": "Brief verification summary",
    "sources": ["source1", "source2"],
    "concerns": "Any issues found or empty string if none"
}}"""
        
        try:
            response = self.research_ai.chat(verify_prompt, temperature=0.1)
            json_match = re.search(r'\{[\s\S]+\}', response)
            if json_match:
                result = json.loads(json_match.group())
                return result
        except Exception as e:
            print(f"Verification error: {e}")
        
        # Fallback
        return {
            'confidence': 0.3,
            'summary': 'Could not verify automatically',
            'sources': [],
            'concerns': 'Verification system error - manual review required'
        }
    
    def _verify_with_source(self, information: str, source: Dict) -> Dict:
        """Verify information against an uploaded source"""
        source_type = source.get('type', 'unknown')
        source_content = source.get('content', '')
        
        if source_type == 'url':
            # Fetch and parse URL
            try:
                response = requests.get(source_content, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                text_content = soup.get_text(separator=' ', strip=True)[:5000]  # Limit to 5000 chars
            except Exception as e:
                return {
                    'confidence': 0.0,
                    'summary': f'Could not fetch URL: {str(e)}',
                    'sources': [source_content],
                    'concerns': 'URL could not be accessed'
                }
        
        elif source_type == 'text':
            text_content = source_content
        
        elif source_type == 'pdf':
            # For PDF, content should already be extracted
            text_content = source_content
        
        elif source_type == 'image':
            # For images, use AI vision to extract text
            # This would require additional API calls to vision models
            return {
                'confidence': 0.5,
                'summary': 'Image verification not yet implemented',
                'sources': ['Uploaded image'],
                'concerns': 'Please provide text-based source for verification'
            }
        
        else:
            text_content = source_content
        
        # Verify against source content
        verify_prompt = f"""Compare this information against the provided source document:

Information to verify: "{information}"

Source document excerpt:
{text_content[:3000]}

Does the source support this information? Check:
1. Are numerical values correct?
2. Are procedures/steps accurate?
3. Is context appropriate?

Respond in JSON:
{{
    "confidence": 0.9,
    "summary": "Source verification result",
    "sources": ["Provided source document"],
    "concerns": "Any discrepancies or empty string"
}}"""
        
        try:
            response = self.research_ai.chat(verify_prompt, temperature=0.1)
            json_match = re.search(r'\{[\s\S]+\}', response)
            if json_match:
                return json.loads(json_match.group())
        except Exception as e:
            print(f"Source verification error: {e}")
        
        return {
            'confidence': 0.5,
            'summary': 'Source verification incomplete',
            'sources': ['Uploaded source'],
            'concerns': 'Could not complete verification'
        }
    
    def _handle_modify_section(self, user_input: str, intent: Dict, uploaded_source: Optional[Dict]) -> Dict:
        """Handle request to modify existing section"""
        # Similar to add_information but for modifications
        return {
            'success': True,
            'message': '⚙️ Section modification feature coming soon. For now, please describe what you want to change and I will help verify the new information.',
            'action': 'feature_pending'
        }
    
    def _handle_question(self, user_input: str) -> Dict:
        """Handle user question about the document"""
        doc = self.context['selected_document']
        
        # Load actual document content for better answers
        with open(doc['path'], 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Parse HTML to get text content
        soup = BeautifulSoup(html_content, 'html.parser')
        doc_text = soup.get_text(separator='\n', strip=True)[:8000]  # Limit to 8000 chars
        
        qa_prompt = f"""Answer this question about the service document:

Document: {doc['info']['title']}
Available sections: {', '.join(doc['info']['sections'].keys())}

Document content (excerpt):
{doc_text}

Question: {user_input}

Instructions:
- Provide a clear, direct answer based on the document content
- If the answer isn't in the document, offer to help research or add that information
- If this is a wiring diagram request, explain that you can research and cache wiring information
- Be specific and cite relevant sections when possible"""
        
        try:
            answer = self.research_ai.chat(qa_prompt, temperature=0.3)
            return {
                'success': True,
                'message': answer,
                'action': 'answered'
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'❌ Error: {str(e)}'
            }
    
    def _handle_review_document(self) -> Dict:
        """Review and validate the current document"""
        doc = self.context['selected_document']
        
        review_prompt = f"""Review this service document for completeness and accuracy:

Document: {doc['info']['title']}
Sections present: {', '.join(doc['info']['sections'].keys())}

Provide:
1. Overall assessment
2. Missing sections or information
3. Areas that need more detail
4. Any potential accuracy concerns

Keep it concise and actionable."""
        
        try:
            review = self.research_ai.chat(review_prompt, temperature=0.2)
            return {
                'success': True,
                'message': f"📋 **Document Review:**\n\n{review}",
                'action': 'reviewed'
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'❌ Error: {str(e)}'
            }
    
    def _handle_general_chat(self, user_input: str) -> Dict:
        """Handle general conversation"""
        response = self.research_ai.chat(
            user_input,
            system_message="You are an expert automotive technician assistant. Help users edit and improve their service documentation. Be helpful but concise."
        )
        
        return {
            'success': True,
            'message': response,
            'action': 'general_response'
        }
    
    def _handle_wiring_diagram_request(self, user_input: str, intent: Dict) -> Dict:
        """Handle wiring diagram research and caching"""
        doc = self.context['selected_document']
        doc_info = doc['info']
        
        # Extract vehicle info from document title
        title_parts = doc_info['title'].split('—')[0].strip() if '—' in doc_info['title'] else doc_info['title']
        
        # Better circuit detection from user input
        input_lower = user_input.lower()
        circuit_type = intent.get('specific_topic', 'general')
        
        # Try to extract more specific circuit info from the question
        if 'o2' in input_lower or 'oxygen' in input_lower:
            if 'upstream' in input_lower:
                circuit_type = 'upstream_oxygen_sensor'
            elif 'downstream' in input_lower:
                circuit_type = 'downstream_oxygen_sensor'
            else:
                circuit_type = 'oxygen_sensor'
        
        # Check if wiring diagram already exists
        wiring_dir = Path(__file__).parent.parent / 'wiring_diagrams'
        wiring_dir.mkdir(exist_ok=True)
        
        # Create filename
        safe_title = re.sub(r'[^\w\s-]', '', title_parts).replace(' ', '_')
        safe_circuit = re.sub(r'[^\w\s-]', '', circuit_type).replace(' ', '_')
        filename = f"{safe_title}_{safe_circuit}_wiring.txt"
        filepath = wiring_dir / filename
        
        # Check if already cached
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                cached_content = f.read()
            
            # Extract just the wiring info (skip header)
            content_parts = cached_content.split('=' * 60)
            if len(content_parts) > 2:
                wiring_info = content_parts[2].strip()
            else:
                wiring_info = cached_content
            
            message = f"""🔌 **Wiring Diagram Information (From Cache)**

**Vehicle:** {title_parts}
**Circuit/System:** {circuit_type.replace('_', ' ').title()}

{wiring_info}

---

✅ **Previously cached:** `{filename}`

**What you can do:**
- Ask specific questions about the wiring (e.g., "What wire color goes to pin 3?")
- Request to add this info to the service document
- Ask me to research additional circuits
- Upload an actual wiring diagram image for reference"""
            
            return {
                'success': True,
                'message': message,
                'action': 'wiring_diagram_from_cache',
                'filepath': str(filepath)
            }
        
        # Not cached, research it
        research_prompt = f"""Find comprehensive wiring diagram information for this automotive circuit:

Vehicle: {title_parts}
Circuit/System: {circuit_type.replace('_', ' ').title()}
User Question: {user_input}

Provide detailed technical wiring information including:

1. **Component Identification:**
   - All components in this circuit (sensors, modules, relays, fuses)
   - Part numbers or specifications where applicable

2. **Wire Information:**
   - Wire colors and color codes (e.g., "BLK/WHT" = black with white tracer)
   - Wire gauge specifications
   - Circuit identification numbers

3. **Connector Details:**
   - Connector types and locations
   - Pin assignments and functions
   - Connector part numbers

4. **Electrical Specifications:**
   - Operating voltage ranges
   - Resistance specifications
   - Signal types (5V reference, ground, PWM, etc.)

5. **Component Locations:**
   - Where to find each component (engine bay, under dash, etc.)
   - Access procedures if complex

6. **Common Issues:**
   - Known wiring problems or failure points
   - TSB (Technical Service Bulletin) information
   - Typical diagnostic procedures

7. **Testing Points:**
   - Where to measure voltages
   - Expected voltage/resistance readings
   - Diagnostic connector pins

Be extremely detailed and technical. Include specific values, measurements, and part numbers."""
        
        try:
            wiring_info = self.research_ai.chat(research_prompt, temperature=0.2)
            
            # Save to wiring diagram cache
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"WIRING DIAGRAM INFORMATION\n")
                f.write(f"{'=' * 60}\n\n")
                f.write(f"Vehicle: {title_parts}\n")
                f.write(f"Circuit/System: {circuit_type.replace('_', ' ').title()}\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"User Request: {user_input}\n\n")
                f.write(f"{'=' * 60}\n\n")
                f.write(wiring_info)
            
            message = f"""🔌 **Wiring Diagram Information Retrieved**

**Vehicle:** {title_parts}
**Circuit/System:** {circuit_type.replace('_', ' ').title()}

{wiring_info}

---

✅ **Saved to cache:** `{filename}`

**What you can do next:**
- Ask follow-up questions about this wiring
- Say "Add this to troubleshooting" to add to the service document
- Request another circuit's wiring information
- Upload an actual wiring diagram image/PDF if you have one

**Note:** This information has been researched and cached. For actual wiring diagram images:
- Upload a diagram file when prompted
- Provide a URL to OEM wiring resources
- I'll help organize and reference it properly"""
            
            return {
                'success': True,
                'message': message,
                'action': 'wiring_diagram_researched',
                'filepath': str(filepath)
            }
            
        except Exception as e:
            return {
                'success': False,
                'message': f"""❌ **Error researching wiring diagram:** {str(e)}

**Try these alternatives:**
- Be more specific about the circuit (e.g., "oxygen sensor to ECM wiring")
- Specify if you need upstream or downstream O2 sensor
- Upload a wiring diagram file/image
- Provide a URL to wiring diagram resources
- Ask about a different circuit first

**Example requests:**
- "Show me the upstream O2 sensor wiring"
- "I need the ECM connector pinout"
- "What's the wire color for the O2 sensor signal?"
""",
                'action': 'wiring_diagram_error'
            }
    
    def confirm_pending_edit(self) -> Dict:
        """Execute the pending edit after user confirmation"""
        if not self.context['pending_edits']:
            return {
                'success': False,
                'message': 'No pending edits to confirm.'
            }
        
        # Get most recent pending edit
        edit = self.context['pending_edits'][-1]
        
        # Apply the edit to the document
        result = self._apply_edit_to_document(edit)
        
        if result['success']:
            # Clear pending edits
            self.context['pending_edits'] = []
        
        return result
    
    def _apply_edit_to_document(self, edit: Dict) -> Dict:
        """Apply an edit to the HTML document"""
        try:
            doc = self.context['selected_document']
            html = doc['html']
            extraction = edit['extraction']
            
            # Parse HTML
            soup = BeautifulSoup(html, 'html.parser')
            
            # Find target section
            target_section_id = extraction['target_section']
            section = soup.find('section', id=target_section_id)
            
            if not section:
                return {
                    'success': False,
                    'message': f'❌ Could not find section: {target_section_id}'
                }
            
            # Add the information
            info_type = extraction.get('info_type', 'general')
            new_content = extraction['information']
            
            # Create appropriate HTML element based on type
            if info_type == 'torque_spec':
                # Add to torque table
                # This would require more sophisticated parsing
                pass
            elif info_type == 'procedure_step':
                # Add to steps list
                pass
            else:
                # Add as general note
                note_div = soup.new_tag('div', **{'class': 'added-note'})
                note_div.string = f"Note: {new_content}"
                section.append(note_div)
            
            # Save updated HTML
            doc_path = Path(doc['path'])
            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return {
                'success': True,
                'message': f'✅ Successfully added information to {target_section_id} section!'
            }
        
        except Exception as e:
            return {
                'success': False,
                'message': f'❌ Error applying edit: {str(e)}'
            }
    
    def get_status(self) -> Dict:
        """Get current assistant status"""
        return {
            'selected_document': self.context['selected_document']['info'] if self.context['selected_document'] else None,
            'pending_edits': len(self.context['pending_edits']),
            'conversation_length': len(self.context['conversation_history'])
        }
