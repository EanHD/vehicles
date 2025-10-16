# 🤖 AI Configuration Guide
**Swoop Service Auto - Unified AI System**

## Overview

All Python tools in this repository now use a unified AI client system that supports multiple AI providers. This makes it easy to:

- **Switch between AI providers** without changing code
- **Use different AI models for different purposes** (research vs. formatting)
- **Control costs** by choosing appropriate models for each task
- **Maintain consistency** across all tools

---

## 🎯 Quick Start

### 1. Copy the Environment Template

```bash
cp .env.example .env
```

### 2. Add Your API Keys

Edit `.env` and add your API keys:

```bash
# At minimum, add one of these:
PERPLEXITY_API_KEY=pplx-your-key-here
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### 3. Configure AI Providers (Optional)

The system is pre-configured with optimal defaults:
- **Research AI**: Perplexity Sonar Pro (best for web-based research)
- **Formatter AI**: OpenAI GPT-4o-mini (good quality, lower cost)

To change providers, edit these lines in `.env`:

```bash
# Research AI (for finding information)
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro

# Formatter AI (for generating HTML/docs)
FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
```

### 4. Test Your Configuration

```bash
source venv/bin/activate
python tools/ai_client.py test
```

---

## 🔧 Configuration Options

### Supported AI Providers

| Provider | Best For | Cost | Web Access | Notes |
|----------|----------|------|------------|-------|
| **Perplexity** | Research, specs | $ | ✅ Yes | **Recommended for research** - Has real-time web access |
| **OpenAI** | Formatting, general | $$ | ❌ No | Good balance of quality and cost |
| **Anthropic** | High-quality output | $$$ | ❌ No | Premium quality, higher cost |
| **OpenRouter** | Flexibility | Varies | Varies | Access to multiple models |

### Available Models

#### Perplexity
- `sonar-pro` - Best quality, web access (recommended)
- `sonar` - Lower cost option

#### OpenAI
- `gpt-4o-mini` - Fast, cost-effective (recommended for formatting)
- `gpt-4o` - Higher quality, more expensive
- `gpt-4-turbo` - Older model, still good

#### Anthropic
- `claude-3-5-sonnet-20241022` - Latest, best quality
- `claude-3-opus-20240229` - Most capable, expensive
- `claude-3-sonnet-20240229` - Balanced option

---

## 💡 Recommended Configurations

### Budget-Friendly (Best Value)
```bash
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar

FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
```
**Estimated cost**: ~$0.03-0.05 per document

### Balanced (Recommended)
```bash
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro

FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
```
**Estimated cost**: ~$0.05-0.08 per document

### Premium Quality
```bash
RESEARCH_AI_PROVIDER=perplexity
RESEARCH_AI_MODEL=sonar-pro

FORMATTER_AI_PROVIDER=anthropic
FORMATTER_AI_MODEL=claude-3-5-sonnet-20241022
```
**Estimated cost**: ~$0.10-0.15 per document

### Single Provider (OpenAI Only)
```bash
RESEARCH_AI_PROVIDER=openai
RESEARCH_AI_MODEL=gpt-4o

FORMATTER_AI_PROVIDER=openai
FORMATTER_AI_MODEL=gpt-4o-mini
```
**Note**: OpenAI doesn't have web access, so research quality may be lower

---

## 🛠️ Advanced Configuration

### Temperature Settings

Control creativity vs. consistency:

```bash
# Research (lower = more factual)
RESEARCH_TEMPERATURE=0.2

# Formatter (slightly higher for better HTML)
FORMATTER_TEMPERATURE=0.3
```

### Token Limits

Control response length (affects cost):

```bash
# Research responses
RESEARCH_MAX_TOKENS=4000

# Formatter responses (HTML needs more space)
FORMATTER_MAX_TOKENS=8000
```

### Custom API Endpoints

For self-hosted or alternative endpoints:

```bash
PERPLEXITY_API_URL=https://api.perplexity.ai/chat/completions
OPENAI_API_URL=https://api.openai.com/v1/chat/completions
OPENROUTER_API_URL=https://openrouter.ai/api/v1/chat/completions
```

---

## 📊 Cost Comparison

Approximate costs for generating one service document:

| Configuration | Research | Formatting | Total | Quality |
|--------------|----------|------------|-------|---------|
| Budget | $0.02 | $0.01 | **$0.03** | Good |
| Balanced | $0.04 | $0.01 | **$0.05** | Very Good |
| Premium | $0.04 | $0.06 | **$0.10** | Excellent |

**Estimated tokens per document:**
- Research: ~3,000-4,000 tokens
- Formatting: ~2,000-3,000 tokens

---

## 🔍 Tools That Use AI

All these tools now use the unified AI client:

### Research Tools
- `research_tools/service_doc_generator.py` - Uses **RESEARCH** AI
- `research_tools/torque_spec_finder.py` - Uses **RESEARCH** AI
- `research_tools/wiring_diagram_helper.py` - Uses **RESEARCH** AI

### Documentation Tools
- `tools/service_doc_generator.py` - Uses **RESEARCH** + **FORMATTER** AI
- `tools/batch_generate.py` - Uses **RESEARCH** + **FORMATTER** AI

### API Server
- `tools/service_api.py` - Uses **RESEARCH** + **FORMATTER** AI

---

## 🚀 Usage Examples

### Generate Service Documentation

```bash
source venv/bin/activate

# Uses configured AI providers automatically
python tools/service_doc_generator.py \
  --year 2020 \
  --make Ford \
  --model "F-150" \
  --service "Oil Change"
```

### Find Torque Specifications

```bash
source venv/bin/activate

# Uses RESEARCH AI
python research_tools/torque_spec_finder.py \
  2020 Ford "F-150" "cylinder head"
```

### Get Wiring Diagram Help

```bash
source venv/bin/activate

# Uses RESEARCH AI
python research_tools/wiring_diagram_helper.py \
  2020 Ford "F-150" "fuel pump" "no start"
```

### Batch Generate Documentation

```bash
source venv/bin/activate

# Generate 50 popular combinations
python tools/batch_generate.py --max 50 --delay 2
```

---

## 🐛 Troubleshooting

### "API key not found" Error

**Problem**: No API key configured for the selected provider

**Solution**: 
```bash
# Check which provider is configured
python tools/ai_client.py

# Add the appropriate API key to .env
echo "PERPLEXITY_API_KEY=your-key-here" >> .env
```

### "Connection failed" Error

**Problem**: API endpoint not reachable or invalid key

**Solution**:
```bash
# Test the connection
python tools/ai_client.py test

# Verify your API key is valid
# Check https://perplexity.ai or https://platform.openai.com
```

### "Could not parse JSON response"

**Problem**: AI returned non-JSON text

**Solution**: 
- Try increasing `MAX_TOKENS` (response might be truncated)
- Try a different model (some models are better at structured output)
- Check if provider has rate limits

### High Costs

**Solution**:
```bash
# Switch to cheaper models
RESEARCH_AI_MODEL=sonar  # Instead of sonar-pro
FORMATTER_AI_MODEL=gpt-4o-mini  # Instead of gpt-4o

# Reduce token limits
RESEARCH_MAX_TOKENS=3000  # Instead of 4000
FORMATTER_MAX_TOKENS=6000  # Instead of 8000

# Use caching - documents are cached automatically!
```

---

## 📚 API Key Setup

### Perplexity (Recommended for Research)

1. Visit https://www.perplexity.ai/
2. Sign up for an account
3. Go to Settings → API
4. Generate an API key
5. Add to `.env`: `PERPLEXITY_API_KEY=pplx-...`

**Pricing**: ~$5/month for typical usage

### OpenAI (Good for Formatting)

1. Visit https://platform.openai.com/
2. Create an account
3. Add payment method
4. Go to API Keys → Create new key
5. Add to `.env`: `OPENAI_API_KEY=sk-...`

**Pricing**: Pay-as-you-go, ~$10/month for typical usage

### Anthropic (Premium Quality)

1. Visit https://www.anthropic.com/
2. Sign up for Claude API access
3. Add payment method
4. Generate API key
5. Add to `.env`: `ANTHROPIC_API_KEY=sk-ant-...`

**Pricing**: Pay-as-you-go, ~$20/month for typical usage

---

## 🔐 Security Best Practices

1. **Never commit .env to git**
   ```bash
   # .env is already in .gitignore
   # .env.example is safe to commit (no real keys)
   ```

2. **Rotate API keys regularly**
   - Generate new keys every 3-6 months
   - Revoke old keys immediately if compromised

3. **Use separate keys for development/production**
   ```bash
   # Development
   PERPLEXITY_API_KEY=pplx-dev-key-here
   
   # Production (different key)
   PERPLEXITY_API_KEY=pplx-prod-key-here
   ```

4. **Monitor usage**
   - Check API dashboards regularly
   - Set up billing alerts
   - Review generated documents for quality

---

## 💾 Caching System

All generated documents are **automatically cached** to avoid regenerating the same content:

- **First generation**: Uses AI, takes 5-30 seconds, costs money
- **Subsequent lookups**: Instant, free, reads from cache

Cache location: `service_docs/` directory

To regenerate a cached document:
```bash
python tools/service_doc_generator.py \
  --year 2020 --make Ford --model "F-150" \
  --service "Oil Change" \
  --force  # Force regeneration
```

---

## 📞 Support

If you encounter issues:

1. Check this guide first
2. Run diagnostics: `python tools/ai_client.py test`
3. Check API provider status pages
4. Verify API keys are valid and have credits
5. Review `.env` configuration

For questions about specific AI providers, consult their documentation:
- Perplexity: https://docs.perplexity.ai/
- OpenAI: https://platform.openai.com/docs
- Anthropic: https://docs.anthropic.com/

---

## 🎯 Summary

✅ **All tools use unified AI client**  
✅ **Configure once in .env**  
✅ **Easy to switch providers**  
✅ **Automatic caching saves money**  
✅ **Flexible for different budgets**  

**Recommended Setup:**
- Research: Perplexity Sonar Pro (web access)
- Formatter: OpenAI GPT-4o-mini (cost-effective)
- Total cost: ~$0.05 per document

Happy documenting! 🚗🔧
