# AI Document Editor Assistant Guide

## Overview

The AI Document Editor Assistant is a guided, token-efficient tool for editing and updating your cached service documentation with verified information. Unlike a simple chat interface, this assistant is specifically designed to help you improve documents while ensuring accuracy through fact-checking and source verification.

## Key Features

### 🎯 **Guided Workflow**
- Select a specific document from your cache to edit
- Assistant guides you through adding/modifying information step-by-step
- Clear action prompts and confirmation steps

### ✅ **Automatic Verification**
- AI fact-checks all information before adding it to documents
- Uses web research to verify technical specifications
- Provides confidence scores for all changes

### 📎 **Source Upload**
- Upload supporting documentation (URLs, PDFs, images, text)
- Assistant verifies your edits against provided sources
- Ensures accuracy when adding non-standard information

### 💰 **Token Optimized**
- Minimal API usage - only for verification and updates
- No wasted tokens on general conversation
- Focused queries for maximum efficiency

## How to Use

### Step 1: Select a Document

1. Navigate to **💬 AI Assistant** page
2. Choose a document from the **Select Document to Edit** dropdown
3. Click **📂 Load Document**
4. View available sections in the expandable section list

### Step 2: Make Your Request

Type your edit request in the chat. Examples:

**Adding Information:**
- "Add oil drain plug torque: 18 ft-lbs"
- "Add troubleshooting tip: Check for oil leaks at filter housing"
- "Add fluid spec: Use DEX-COOL coolant per GM spec"
- "The fuel pressure should be 58-62 PSI"

**Asking Questions:**
- "What's the torque spec for the oil pan bolts?"
- "Is there a section on cooling system bleeding?"
- "What engine options are covered in this document?"

**Reviewing:**
- "Review this document for accuracy"
- "What's missing from this document?"
- "Check for completeness"

### Step 3: Review Verification

The assistant will:

1. **Analyze your request** - Understand what you want to add/change
2. **Fact-check the information** - Verify against online sources and databases
3. **Provide confidence score** - Rate the accuracy (0-100%)
4. **Present findings** - Show what was found and any concerns

#### ✅ High Confidence (80%+)
```
✅ Verification Passed (confidence: 95%)

Information to add:
Oil drain plug torque: 18 ft-lbs (24 Nm)

Target section: torque-specifications

Verification summary:
Confirmed via multiple sources including Toyota service manual
and trusted automotive databases.

Sources: Toyota FSM, AllData, TorqueSpec Database

Reply with "add it" or "yes" to confirm
```

#### ⚠️ Medium Confidence (50-79%)
```
⚠️ Verification Uncertain (confidence: 65%)

Information to add:
Oil capacity: 5.5 quarts

Verification summary:
Found conflicting information. Some sources say 5.0 quarts,
others say 5.5 quarts depending on filter.

Concerns:
Capacity varies by engine variant and oil filter type.

Please upload a source document or clarify which engine.
```

#### ❌ Low Confidence (<50%)
```
❌ Verification Failed (confidence: 30%)

Information to add:
Spark plug gap: 0.035"

Issues found:
This specification doesn't match factory data. OEM spec
is 0.044" for this engine.

Please verify your source or revise the information.
```

### Step 4: Confirm or Provide Source

**If verification passed:**
- Type: `yes`, `add it`, or `confirm`
- Assistant will update the document

**If verification uncertain:**
- Upload a source document (see Source Upload section)
- Or type `cancel` to abort

**If verification failed:**
- Check your information for errors
- Upload an authoritative source
- Or type `cancel` to abort

## Source Upload

When the assistant needs verification, you can upload sources:

### URL Source
1. Expand **📎 Upload Source for Verification**
2. Select **URL**
3. Enter URL to:
   - Factory service manual pages
   - OEM website specifications
   - Trusted forum posts with documentation
   - Technical bulletins (TSBs)
4. Assistant will fetch and analyze the content

### Text/Paste Source
1. Select **Text/Paste**
2. Copy and paste text from:
   - PDF service manuals
   - Technical documentation
   - Forum posts or guides
3. Assistant will verify against this text

### PDF Documents (Coming Soon)
- Upload PDF service manuals
- Automatic text extraction and verification

### Images/Screenshots (Coming Soon)
- Upload photos of service manual pages
- OCR text extraction for verification

## What Information Can Be Added?

### ✅ Supported
- **Torque specifications** - Bolt/fastener torque values
- **Fluid specifications** - Type, capacity, part numbers
- **Procedure steps** - Additional steps or clarifications
- **Troubleshooting tips** - Common issues and solutions
- **Part numbers** - OEM and aftermarket alternatives
- **Specifications** - Gaps, clearances, pressures, etc.

### ⚠️ Requires Careful Verification
- **Labor times** - Varies by technician skill
- **Diagnostic procedures** - May need specialized equipment
- **Electrical specifications** - Voltage, resistance values

### ❌ Not Recommended
- **Personal opinions** - Keep documentation objective
- **Unverified information** - Always verify first
- **Marketing content** - Stick to technical facts

## Quick Actions

Use the quick action buttons for common tasks:

- **📋 Review Document** - Get an overall assessment of document quality
- **❓ Ask Question** - Prompts you to ask about the document
- **➕ Add Information** - Guides you through adding new content

## Token Usage & Cost

The assistant is designed to minimize API costs:

### Typical Operation Costs (OpenRouter/Perplexity)
- **Document selection**: ~0 tokens (local operation)
- **Intent analysis**: ~100-200 tokens ($0.0001-0.0003)
- **Verification**: ~500-1000 tokens ($0.0005-0.0015)
- **Document update**: ~200-500 tokens ($0.0002-0.0007)

**Total per edit: ~$0.001-0.003** (0.1-0.3 cents)

### Cost Optimization Tips
1. **Batch edits** - Make multiple edits in one session
2. **Be specific** - Clear requests need less back-and-forth
3. **Upload sources** - Reduces web research API calls
4. **Use high confidence info** - Verified info doesn't need re-checking

## Workflow Examples

### Example 1: Adding a Torque Spec

**User:** "Add oil drain plug torque: 18 ft-lbs"

**Assistant:** 
```
🔍 Analyzing... (100 tokens)
✅ Verification Passed (confidence: 95%)

Information to add: Oil drain plug torque: 18 ft-lbs (24 Nm)
Target section: torque-specifications
Sources: Toyota FSM, TorqueSpec DB

Reply "yes" to confirm.
```

**User:** "yes"

**Assistant:** 
```
✅ Successfully added information to torque-specifications section!
```

**Total cost:** ~$0.002

---

### Example 2: Adding with Source Verification

**User:** "The fuel pressure regulator vacuum line should have 18-20 in-Hg at idle"

**Assistant:**
```
⚠️ Verification Uncertain (confidence: 60%)

This specification seems unusual. Please upload a source
for verification.
```

**User:** [Uploads URL to service manual page]

**Assistant:**
```
✅ Source Verified! (confidence: 98%)

Your source confirms this specification. Would you like
to add this to the troubleshooting section?

Reply "yes" to add.
```

**Total cost:** ~$0.004 (includes source verification)

---

### Example 3: Document Review

**User:** [Clicks "📋 Review Document"]

**Assistant:**
```
📋 Document Review:

Overall: Good coverage of basic procedure

Strengths:
- Complete torque specifications
- Clear step-by-step procedure
- Good safety warnings

Areas for improvement:
- Missing fluid capacity information
- Coolant bleeding procedure could be more detailed
- No troubleshooting section for common issues

Suggestions:
1. Add coolant capacity to fluids section
2. Expand bleeding procedure with air pocket locations
3. Add troubleshooting tips for stuck thermostats
```

**Total cost:** ~$0.003

## Best Practices

### ✅ DO
- Be specific and clear in your requests
- Provide sources for non-standard specifications
- Confirm information before adding
- Use quick actions for common tasks
- Review documents periodically for completeness

### ❌ DON'T
- Add unverified information
- Override high-confidence rejections without good reason
- Make vague requests that need clarification
- Argue with verification results without sources
- Add personal opinions or non-technical content

## Troubleshooting

### "No document selected"
**Solution:** Load a document from the dropdown before making requests

### "Verification failed"
**Solution:** 
1. Check your information for accuracy
2. Upload a reliable source document
3. Revise your request with correct information

### "Could not find section"
**Solution:**
- Check available sections in the document info
- Use standard section names (torque-specifications, steps, troubleshooting, etc.)

### "Source could not be accessed"
**Solution:**
- Verify URL is accessible
- Try copying and pasting text instead
- Use a different source

## Future Enhancements

Coming soon:
- ✨ PDF document parsing
- ✨ Image OCR for service manual photos
- ✨ Bulk editing capabilities
- ✨ Version history and rollback
- ✨ AI-suggested improvements
- ✨ Citation tracking for all specs

## Support

For issues or questions:
1. Check this guide first
2. Review the system documentation
3. Check verification messages for guidance
4. Contact support with specific error messages

---

**Version:** 1.0  
**Last Updated:** January 2025  
**Compatible With:** Swoop Service Auto v2.0+
