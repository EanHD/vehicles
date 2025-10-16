# Diagram Generation Decision

## Summary

**Diagram generation has been disabled by default** as of this update.

## Reasoning

After testing AI-generated technical diagrams for automotive service procedures, we found:

### Issues with AI-Generated Diagrams

1. **Quality**: The diagrams were not accurate enough for professional use
2. **Reliability**: AI image generators struggle with technical accuracy
3. **Cost**: ~$0.005-0.04 per diagram adds up quickly
4. **Value**: The diagrams didn't provide enough value to justify the cost and quality issues

### Problems Encountered

- Diagrams showed generic/incorrect mechanical layouts
- Labels and callouts were often wrong or missing
- No guarantee of mechanical accuracy
- Images didn't match the specific vehicle/procedure

## Current Status

**Diagram generation is DISABLED** in `.env`:

```bash
# Diagram provider (leave empty to disable diagram generation)
# DISABLED: AI-generated diagrams are not reliable enough for technical service information
# To re-enable, uncomment the line below and set to: together, openai, or stability
# DIAGRAM_AI_PROVIDER=together
DIAGRAM_AI_PROVIDER=
```

## If You Want to Re-enable Diagrams

### Option 1: Use Together AI (Cheapest)
```bash
DIAGRAM_AI_PROVIDER=together
TOGETHER_API_KEY=your_key_here
TOGETHER_IMAGE_MODEL=black-forest-labs/FLUX.1-schnell
```

### Option 2: Use OpenAI DALL-E
```bash
DIAGRAM_AI_PROVIDER=openai
# Uses your existing OPENAI_API_KEY
OPENAI_IMAGE_MODEL=dall-e-2  # or dall-e-3 for better quality
```

### Option 3: Use Stability AI
```bash
DIAGRAM_AI_PROVIDER=stability
STABILITY_API_KEY=your_key_here
STABILITY_MODEL=stable-diffusion-xl-1024-v1-0
```

## Alternative Approaches

Instead of AI-generated diagrams, consider:

1. **Manual diagram sourcing**: Find existing service manual diagrams
2. **OEM resources**: Use manufacturer service information
3. **Community contributions**: Allow mechanics to upload diagrams
4. **Hybrid approach**: Generate text descriptions instead of images

## Cache Cleanup

All existing cached documents with diagrams have been removed. When you regenerate them, they will be created **without** diagrams for cleaner, more professional documentation.

## Files Modified

- `.env` - Disabled DIAGRAM_AI_PROVIDER
- `README.md` - Removed diagram references
- Deleted cache documents with old diagrams
- Deleted `service_docs/diagrams/` folder

## Bottom Line

**Focus on what AI does well**: Research, writing, and formatting technical procedures. Leave visual diagrams for when you have access to real service manual images.
