# AI Diagram Generation Guide

## Overview

The Swoop Service Auto system can now automatically generate technical diagrams for service documentation using AI image generation. This feature adds visual aids to help mechanics understand complex procedures.

## Features

- **Automatic Generation**: Diagrams are generated during document creation based on the procedure steps
- **Technical Style**: Optimized for automotive service manual style illustrations
- **Smart Caching**: Generated diagrams are cached to avoid regeneration costs
- **Multiple Providers**: Support for multiple AI image generation services

## Supported Providers

### 1. Together AI (RECOMMENDED) 🌟
- **Model**: FLUX.1-schnell
- **Cost**: ~$0.005 per diagram
- **Speed**: Very fast (4 steps)
- **Quality**: Good technical illustrations
- **Best for**: Budget-conscious users, high-volume generation

**Setup**:
```bash
DIAGRAM_AI_PROVIDER=together
TOGETHER_API_KEY=your-key-here
TOGETHER_IMAGE_MODEL=black-forest-labs/FLUX.1-schnell
```

Get API key: https://api.together.xyz/

### 2. OpenAI DALL-E
- **Models**: DALL-E 2 (~$0.02) or DALL-E 3 (~$0.04)
- **Cost**: Moderate to high
- **Speed**: Medium
- **Quality**: High quality, good detail
- **Best for**: When you need highest quality

**Setup**:
```bash
DIAGRAM_AI_PROVIDER=openai
OPENAI_API_KEY=your-key-here  # Same as main OpenAI key
OPENAI_IMAGE_MODEL=dall-e-2   # or dall-e-3 for higher quality
```

### 3. Stability AI
- **Model**: Stable Diffusion XL
- **Cost**: ~$0.01 per diagram
- **Speed**: Medium
- **Quality**: Good detail and clarity
- **Best for**: Balance between cost and quality

**Setup**:
```bash
DIAGRAM_AI_PROVIDER=stability
STABILITY_API_KEY=your-key-here
STABILITY_MODEL=stable-diffusion-xl-1024-v1-0
```

Get API key: https://platform.stability.ai/

## Configuration

### Enable Diagram Generation

In your `.env` file:

```bash
# Choose your provider
DIAGRAM_AI_PROVIDER=together

# Add the corresponding API key
TOGETHER_API_KEY=your-api-key-here

# Optional: customize cache directory
DIAGRAM_CACHE_DIR=service_docs/diagrams
```

### Disable Diagram Generation

To turn off diagram generation (free):

```bash
# Leave provider empty or comment out
# DIAGRAM_AI_PROVIDER=

# Or remove/comment API keys
```

## Usage

### In Web Interface

1. Select your vehicle and service
2. Check the "🎨 Generate AI diagrams" checkbox
3. Click "Generate Service Documentation"
4. Diagrams will be generated and embedded in the HTML

### In Python Code

```python
from tools.service_doc_generator import ServiceDocGenerator

# Enable diagrams
generator = ServiceDocGenerator(enable_diagrams=True)

doc_path, from_cache = generator.generate(
    year=2020,
    make="Toyota",
    model="Camry",
    service="Brake Pad Replacement",
    force_regenerate=False
)
```

### In CLI

```bash
# Diagrams are controlled by DIAGRAM_AI_PROVIDER in .env
# If provider is set, diagrams will be generated

python tools/service_doc_generator.py \
    --year 2020 \
    --make Toyota \
    --model Camry \
    --service "Brake Pad Replacement"
```

## How It Works

1. **Research Phase**: AI identifies which steps would benefit from diagrams
2. **Generation Phase**: For each needed diagram:
   - AI creates a detailed technical prompt
   - Image AI generates the diagram
   - Diagram is saved to cache directory
3. **Integration Phase**: Diagrams are embedded in the HTML document

## Diagram Quality

### What Works Well ✅
- Component locations and orientations
- Assembly/disassembly sequences  
- Tool usage illustrations
- Basic mechanical layouts
- Cutaway views
- Labeled part callouts

### Limitations ⚠️
- May not be 100% accurate for specific vehicle configurations
- Should be used as visual aids, not sole reference
- Always cross-reference with factory service manual
- Some complex assemblies may need simplification

## Cost Management

### Reducing Costs

1. **Use Cached Documents**: Don't force regeneration unless needed
2. **Choose Cheaper Provider**: Together AI is most economical
3. **Selective Generation**: Only enable diagrams when truly needed
4. **Batch Processing**: Generate multiple docs in one session

### Cost Examples

For a typical brake service with 3 diagrams:

| Provider | Per Diagram | Total |
|----------|------------|-------|
| Together AI | $0.005 | $0.015 |
| Stability AI | $0.01 | $0.03 |
| DALL-E 2 | $0.02 | $0.06 |
| DALL-E 3 | $0.04 | $0.12 |

**Cache hits are FREE** - diagrams are reused automatically

## Troubleshooting

### "Could not enable diagrams"
- Check that DIAGRAM_AI_PROVIDER is set in .env
- Verify corresponding API key is present and valid
- Test API key with: `python tools/diagram_generator.py test`

### "Diagram generation failed"
- Check API key has sufficient credits
- Verify internet connection
- Check API status (provider's status page)
- Review logs for specific error messages

### Poor Quality Diagrams
- Try a different provider (DALL-E 3 for highest quality)
- Check that prompts are specific and clear
- Consider disabling and using manual diagrams instead

### Slow Generation
- Together AI is fastest (~5 seconds per diagram)
- DALL-E can take 15-30 seconds
- Consider generating during off-peak hours

## Best Practices

1. **Preview First**: Generate without diagrams first to review content
2. **Selective Use**: Enable diagrams for complex procedures only
3. **Review Quality**: Always review generated diagrams before sharing
4. **Supplement, Don't Replace**: Use alongside factory documentation
5. **Cache Management**: Keep cache for frequently-used services

## API Key Security

⚠️ **Never commit API keys to version control**

- Keep `.env` file private (already in .gitignore)
- Use environment variables in production
- Rotate keys regularly
- Monitor usage to detect unauthorized use

## Future Enhancements

Planned features:
- Manual diagram upload and caching
- Custom diagram style profiles
- Diagram quality feedback and regeneration
- Integration with factory diagram databases
- OCR of existing service manual diagrams

## Support

For issues or questions:
- Check logs in terminal output
- Review TROUBLESHOOTING.md
- Test connection: `python tools/diagram_generator.py test`
- Verify .env configuration

## References

- Together AI: https://www.together.ai/
- OpenAI DALL-E: https://platform.openai.com/docs/guides/images
- Stability AI: https://platform.stability.ai/docs
