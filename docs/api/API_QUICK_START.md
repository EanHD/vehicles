# Swoop Service Auto - API Quick Start Guide

## Overview

This guide will help you set up and test the REST API for integration with your mobile mechanic application.

## Prerequisites

- Python 3.8 or higher
- Virtual environment activated (`source venv/bin/activate`)
- API keys configured in `.env` file

## Setup

### 1. Install Dependencies

```bash
# Make sure you're in the project directory
cd /home/eanhd/projects/vehicles

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy example config if you haven't already
cp .env.example .env

# Edit .env and add your API keys
nano .env  # or use your preferred editor
```

**Required settings for API:**
- `API_KEY`: Set a secure API key for your mobile app
- `RESEARCH_AI_*`: Configure your AI provider for research
- `FORMATTER_AI_*`: Configure your AI provider for formatting

### 3. Start the API Server

```bash
# Option 1: Using the startup script (recommended)
./start_api.sh

# Option 2: Direct Python command
python api.py

# Option 3: With custom port
API_PORT=3000 python api.py
```

The API will start on `http://localhost:8000` (or your configured port).

## Testing the API

### Using the Interactive Documentation

1. Open your browser to http://localhost:8000/docs
2. Click "Authorize" button (top right)
3. Enter your API key from `.env`
4. Try the endpoints directly in the browser

### Using curl

```bash
# Set your API key
export API_KEY="your-api-key-from-env"

# Test health check
curl http://localhost:8000/api/v1/health

# List vehicles
curl -H "X-API-Key: $API_KEY" \
  "http://localhost:8000/api/v1/vehicles?make=Toyota&limit=5"

# Search vehicles
curl -H "X-API-Key: $API_KEY" \
  "http://localhost:8000/api/v1/vehicles/search?q=camry"

# List services
curl -H "X-API-Key: $API_KEY" \
  http://localhost:8000/api/v1/services

# Generate documentation
curl -X POST \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "year": 2015,
    "make": "Toyota",
    "model": "Camry",
    "service": "Oil Change",
    "engine": "2.5L 4-Cyl"
  }' \
  http://localhost:8000/api/v1/documentation/generate

# Get HTML document (replace {doc_id} with actual ID from previous response)
curl -H "X-API-Key: $API_KEY" \
  http://localhost:8000/api/v1/documentation/{doc_id}/html \
  -o service_doc.html
```

### Using Python

```python
import requests

API_BASE = "http://localhost:8000"
API_KEY = "your-api-key-from-env"

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

# Generate documentation
response = requests.post(
    f"{API_BASE}/api/v1/documentation/generate",
    headers=headers,
    json={
        "year": 2015,
        "make": "Toyota",
        "model": "Camry",
        "service": "Oil Change",
        "engine": "2.5L 4-Cyl"
    }
)

data = response.json()
print(f"Status: {data['status']}")
print(f"Document ID: {data['doc_id']}")
print(f"From cache: {data['from_cache']}")
print(f"Generation time: {data['generation_time']}s")

# Get HTML
html_response = requests.get(
    f"{API_BASE}{data['html_url']}",
    headers=headers
)

with open("service_doc.html", "w") as f:
    f.write(html_response.text)

print("✅ Document saved to service_doc.html")
```

## Common Use Cases

### 1. Vehicle Selection Flow

```python
# Get list of makes
makes = requests.get(
    f"{API_BASE}/api/v1/vehicles/makes",
    headers=headers
).json()

# Get years for selected make
years = requests.get(
    f"{API_BASE}/api/v1/vehicles/years?make=Toyota",
    headers=headers
).json()

# Search for specific model
vehicles = requests.get(
    f"{API_BASE}/api/v1/vehicles/search?q=camry",
    headers=headers
).json()
```

### 2. Service Documentation for Booked Job

```python
def get_service_doc_for_job(job):
    """Generate service documentation when customer books a job"""
    
    # Generate documentation
    response = requests.post(
        f"{API_BASE}/api/v1/documentation/generate",
        headers=headers,
        json={
            "year": job.vehicle.year,
            "make": job.vehicle.make,
            "model": job.vehicle.model,
            "service": job.service_type,
            "engine": job.vehicle.engine
        }
    )
    
    doc = response.json()
    
    # Return URL for WebView
    return f"{API_BASE}{doc['html_url']}"
```

### 3. Cache Management

```python
# List all cached documents
cached = requests.get(
    f"{API_BASE}/api/v1/documentation",
    headers=headers
).json()

print(f"Total cached: {len(cached)}")

# Delete old documents
for doc in cached:
    if is_old(doc['generated_at']):
        requests.delete(
            f"{API_BASE}/api/v1/documentation/{doc['doc_id']}",
            headers=headers
        )
```

## Performance Tips

### Caching Strategy

The API automatically caches generated documents. To maximize performance:

1. **First Request**: ~15 seconds (AI generation)
2. **Subsequent Requests**: < 100ms (cached)

```python
# Force regeneration (if specs updated)
response = requests.post(
    f"{API_BASE}/api/v1/documentation/generate",
    headers=headers,
    json={
        "year": 2015,
        "make": "Toyota",
        "model": "Camry",
        "service": "Oil Change",
        "force_regenerate": True  # Forces new generation
    }
)
```

### Client-Side Caching

Implement caching in your mobile app to reduce API calls:

```python
# Pseudo-code for mobile app
def get_service_doc(vehicle, service):
    # Check local cache first
    cached_path = local_cache.get_path(vehicle, service)
    if os.path.exists(cached_path):
        return cached_path
    
    # Generate via API
    doc = api.generate_documentation(vehicle, service)
    
    # Save to local cache
    local_cache.save(doc.html_content, vehicle, service)
    
    return cached_path
```

## Deployment

### Local Network (Tailscale)

1. Start API with `0.0.0.0` host (already configured)
2. Access from other devices via Tailscale IP
3. Update mobile app to use: `http://your-tailscale-ip:8000`

### Production Deployment

For production use, consider:

1. **HTTPS**: Use reverse proxy (nginx/caddy) with SSL
2. **API Key Security**: Use environment variables, rotate regularly
3. **CORS**: Restrict to your specific mobile app domain
4. **Rate Limiting**: Add rate limiting middleware
5. **Monitoring**: Add logging and error tracking

Example nginx config:

```nginx
server {
    listen 443 ssl;
    server_name api.swoopservice.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Troubleshooting

### API Won't Start

```bash
# Check if port is in use
lsof -i :8000

# Try different port
API_PORT=8001 python api.py
```

### 401 Unauthorized

```bash
# Verify API key matches .env
grep API_KEY .env

# Check header format
curl -v -H "X-API-Key: your-key" http://localhost:8000/api/v1/vehicles/makes
```

### Slow Generation

- First generation takes ~15 seconds (AI processing)
- Subsequent requests use cache and are instant
- Check your AI provider's API response times

### Empty Vehicle/Service Lists

```bash
# Verify data files exist
ls -lh data/vehicles.json
ls -lh data/services.json

# Check file contents
jq 'length' data/vehicles.json
jq 'length' data/services.json
```

## Next Steps

1. **Test all endpoints** using the interactive docs at `/docs`
2. **Integrate with mobile app** using examples in API_DOCUMENTATION.md
3. **Set up production deployment** with HTTPS and rate limiting
4. **Implement client-side caching** for better performance
5. **Monitor usage** and optimize based on patterns

## Support

- Full API Documentation: `API_DOCUMENTATION.md`
- Streamlit Web Interface: Run `./start_app.sh`
- Issues: Check logs in console output

## Useful Commands

```bash
# Start API server
./start_api.sh

# Start Streamlit web interface
./start_app.sh

# Test API health
curl http://localhost:8000/api/v1/health

# View logs (if running in background)
tail -f api.log

# Stop API server
pkill -f "python api.py"
```
