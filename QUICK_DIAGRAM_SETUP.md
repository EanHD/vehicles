# 🎨 Quick Diagram Setup Guide

## 5-Minute Setup

### Option 1: Together AI (Recommended - Cheapest)

**Cost**: ~$0.005 per diagram (~$0.015 for typical service)

```bash
# 1. Get free API key: https://api.together.xyz/
#    - Sign up (free)
#    - Get $5 credit = ~1000 diagrams!

# 2. Add to .env:
DIAGRAM_AI_PROVIDER=together
TOGETHER_API_KEY=paste-your-key-here

# 3. Done! Use the checkbox in web UI
```

### Option 2: OpenAI (If you already have OpenAI)

**Cost**: $0.02-$0.04 per diagram

```bash
# Uses your existing OPENAI_API_KEY

# In .env:
DIAGRAM_AI_PROVIDER=openai
OPENAI_IMAGE_MODEL=dall-e-2

# Done!
```

### Option 3: Stay Free (No diagrams)

```bash
# Leave blank or comment out:
# DIAGRAM_AI_PROVIDER=

# Still get full documentation, just no AI images
```

## Using Diagrams

### In Web Interface

1. Select your vehicle and service
2. ✅ Check "🎨 Generate AI diagrams" 
3. Click "Generate Service Documentation"
4. Wait 30-60 seconds (includes diagram generation)
5. View HTML with embedded diagrams!

### Cost Per Service (Together AI)

| Service Type | Diagrams | Cost |
|--------------|----------|------|
| Oil Change | 2 | $0.01 |
| Brake Job | 3 | $0.015 |
| Alternator | 4 | $0.02 |
| Transmission | 5 | $0.025 |

**Cached diagrams = FREE!** (Reused automatically)

## Test It

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate

# Test your setup
python tools/diagram_generator.py test

# Generate a test doc with diagrams
python tools/service_doc_generator.py \
    --year 2020 \
    --make Toyota \
    --model Camry \
    --service "Oil Change" \
    --force
```

## Provider Comparison

| Provider | Cost | Speed | Quality | Free Credits |
|----------|------|-------|---------|--------------|
| **Together AI** 🌟 | $0.005 | ⚡⚡⚡ | ⭐⭐⭐ | $5 (~1000 diagrams) |
| OpenAI DALL-E 2 | $0.02 | ⚡⚡ | ⭐⭐⭐⭐ | $5 (~250 diagrams) |
| OpenAI DALL-E 3 | $0.04 | ⚡ | ⭐⭐⭐⭐⭐ | $5 (~125 diagrams) |
| Stability AI | $0.01 | ⚡⚡ | ⭐⭐⭐⭐ | None |

## Full Documentation

See `docs/DIAGRAM_GENERATION.md` for complete guide.

---

**Ready in 5 minutes!** 🚀
