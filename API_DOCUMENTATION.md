# Swoop Service Auto - API Documentation

## Overview

The Swoop Service Auto API provides programmatic access to professional automotive service documentation. This API is designed specifically for integration with mobile mechanic applications, enabling automatic generation and retrieval of detailed service procedures when customers book jobs.

## Base URL

```
Production: https://api.swoopservice.com
Development: http://localhost:8000
```

## Authentication

All API endpoints (except `/` and `/docs`) require authentication using an API key passed in the request header:

```http
X-API-Key: your-api-key-here
```

### Getting an API Key

Contact support@swoopserviceauto.com to obtain an API key for your application.

## Quick Start

### 1. Install Dependencies

```bash
pip install requests
```

### 2. Basic Usage Example

```python
import requests

API_BASE = "http://localhost:8000"
API_KEY = "your-api-key"

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
print(f"Document ID: {data['doc_id']}")
print(f"From cache: {data['from_cache']}")
print(f"HTML URL: {data['html_url']}")

# Retrieve HTML
html_response = requests.get(
    f"{API_BASE}{data['html_url']}",
    headers=headers
)

with open("service_doc.html", "w") as f:
    f.write(html_response.text)
```

## API Endpoints

### General Endpoints

#### GET `/`
Root endpoint with basic API information.

**Authentication:** Not required

**Response:**
```json
{
  "message": "Swoop Service Auto API",
  "version": "1.0.0",
  "documentation": "/docs",
  "health_check": "/api/v1/health"
}
```

#### GET `/api/v1/health`
Health check endpoint.

**Authentication:** Not required

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-01-17T12:00:00",
  "database_stats": {
    "total_vehicles": 5247,
    "total_services": 156,
    "cached_documents": 42
  }
}
```

---

### Vehicle Endpoints

#### GET `/api/v1/vehicles`
List vehicles with optional filtering.

**Authentication:** Required

**Query Parameters:**
- `make` (optional): Filter by manufacturer
- `year` (optional): Filter by year
- `limit` (optional): Max results (default: 100, max: 1000)

**Example:**
```bash
curl -X GET "http://localhost:8000/api/v1/vehicles?make=Toyota&year=2015&limit=10" \
  -H "X-API-Key: your-api-key"
```

**Response:**
```json
[
  {
    "year": 2015,
    "make": "Toyota",
    "model": "Camry",
    "engine": "2.5L 4-Cyl",
    "transmission": "Automatic",
    "body_style": "Sedan"
  }
]
```

#### GET `/api/v1/vehicles/search`
Search vehicles by keyword.

**Authentication:** Required

**Query Parameters:**
- `q` (required): Search query (min 2 characters)
- `limit` (optional): Max results (default: 50, max: 500)

**Example:**
```bash
curl -X GET "http://localhost:8000/api/v1/vehicles/search?q=camry&limit=20" \
  -H "X-API-Key: your-api-key"
```

#### GET `/api/v1/vehicles/makes`
Get list of all manufacturers.

**Authentication:** Required

**Response:**
```json
["Acura", "BMW", "Chevrolet", "Ford", "Honda", "Toyota", ...]
```

#### GET `/api/v1/vehicles/years`
Get list of model years.

**Authentication:** Required

**Query Parameters:**
- `make` (optional): Filter years by manufacturer

**Response:**
```json
[2025, 2024, 2023, 2022, ...]
```

---

### Service Endpoints

#### GET `/api/v1/services`
List all available services.

**Authentication:** Required

**Query Parameters:**
- `category` (optional): Filter by category

**Response:**
```json
[
  {
    "id": "oil_change",
    "name": "Oil Change",
    "category": "Maintenance",
    "description": "Engine oil and filter replacement",
    "flat_rate_hours": 0.5,
    "difficulty": 1,
    "skill_level": "Basic"
  }
]
```

#### GET `/api/v1/services/categories`
Get list of service categories.

**Authentication:** Required

**Response:**
```json
["Maintenance", "Brakes", "Electrical", "Engine", "Transmission", ...]
```

---

### Documentation Endpoints

#### POST `/api/v1/documentation/generate`
Generate service documentation.

**Authentication:** Required

**Request Body:**
```json
{
  "year": 2015,
  "make": "Toyota",
  "model": "Camry",
  "service": "Oil Change",
  "engine": "2.5L 4-Cyl",
  "transmission": "Automatic",
  "body_style": "Sedan",
  "force_regenerate": false
}
```

**Required Fields:**
- `year`: Model year (1940-2026)
- `make`: Manufacturer name
- `model`: Model name
- `service`: Service name

**Optional Fields:**
- `engine`: Engine specification
- `transmission`: Transmission type
- `body_style`: Body style
- `force_regenerate`: Force new generation (default: false)

**Response:**
```json
{
  "status": "success",
  "doc_id": "abc123def456",
  "from_cache": false,
  "generation_time": 14.52,
  "html_url": "/api/v1/documentation/abc123def456/html",
  "metadata": {
    "vehicle": {
      "year": 2015,
      "make": "Toyota",
      "model": "Camry",
      "engine": "2.5L 4-Cyl",
      "transmission": "Automatic",
      "body_style": "Sedan"
    },
    "service": "Oil Change",
    "generated_at": "2025-01-17T12:00:00",
    "file_size": 52480
  }
}
```

**Performance:**
- Cached: < 100ms
- New generation: ~15 seconds (AI processing)

#### GET `/api/v1/documentation/{doc_id}/html`
Retrieve HTML documentation.

**Authentication:** Required

**Response:** HTML document (Content-Type: text/html)

**Example:**
```bash
curl -X GET "http://localhost:8000/api/v1/documentation/abc123def456/html" \
  -H "X-API-Key: your-api-key" \
  -o service_doc.html
```

#### GET `/api/v1/documentation/{doc_id}/metadata`
Get document metadata.

**Authentication:** Required

**Response:**
```json
{
  "doc_id": "abc123def456",
  "vehicle": {
    "year": 2015,
    "make": "Toyota",
    "model": "Camry",
    "engine": "2.5L 4-Cyl",
    "transmission": "Automatic",
    "body_style": "Sedan"
  },
  "service": "Oil Change",
  "generated_at": "2025-01-17T12:00:00",
  "file_size": 52480,
  "cached": true
}
```

#### GET `/api/v1/documentation`
List all cached documents.

**Authentication:** Required

**Query Parameters:**
- `limit` (optional): Max results (default: 100, max: 1000)

**Response:** Array of DocumentMetadata objects

#### DELETE `/api/v1/documentation/{doc_id}`
Delete a cached document.

**Authentication:** Required

**Response:**
```json
{
  "status": "deleted",
  "doc_id": "abc123def456"
}
```

---

## Integration Examples

### JavaScript/React Native

```javascript
const API_BASE = 'https://api.swoopservice.com';
const API_KEY = 'your-api-key';

async function generateServiceDoc(vehicle, service) {
  const response = await fetch(`${API_BASE}/api/v1/documentation/generate`, {
    method: 'POST',
    headers: {
      'X-API-Key': API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      year: vehicle.year,
      make: vehicle.make,
      model: vehicle.model,
      service: service,
      engine: vehicle.engine
    })
  });
  
  const data = await response.json();
  return data;
}

// Usage in your app
const doc = await generateServiceDoc(
  { year: 2015, make: 'Toyota', model: 'Camry', engine: '2.5L 4-Cyl' },
  'Oil Change'
);

// Display in WebView
webViewRef.current.source = {
  uri: `${API_BASE}${doc.html_url}`,
  headers: { 'X-API-Key': API_KEY }
};
```

### Swift/iOS

```swift
import Foundation

struct ServiceDocRequest: Codable {
    let year: Int
    let make: String
    let model: String
    let service: String
    let engine: String?
}

struct ServiceDocResponse: Codable {
    let status: String
    let doc_id: String
    let from_cache: Bool
    let generation_time: Double
    let html_url: String
}

func generateServiceDoc(vehicle: Vehicle, service: String, completion: @escaping (Result<ServiceDocResponse, Error>) -> Void) {
    let url = URL(string: "https://api.swoopservice.com/api/v1/documentation/generate")!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("your-api-key", forHTTPHeaderField: "X-API-Key")
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    let requestBody = ServiceDocRequest(
        year: vehicle.year,
        make: vehicle.make,
        model: vehicle.model,
        service: service,
        engine: vehicle.engine
    )
    
    request.httpBody = try? JSONEncoder().encode(requestBody)
    
    URLSession.shared.dataTask(with: request) { data, response, error in
        if let error = error {
            completion(.failure(error))
            return
        }
        
        guard let data = data else {
            completion(.failure(NSError(domain: "NoData", code: -1)))
            return
        }
        
        do {
            let response = try JSONDecoder().decode(ServiceDocResponse.self, from: data)
            completion(.success(response))
        } catch {
            completion(.failure(error))
        }
    }.resume()
}
```

### Kotlin/Android

```kotlin
import okhttp3.*
import kotlinx.serialization.*
import kotlinx.serialization.json.*

@Serializable
data class ServiceDocRequest(
    val year: Int,
    val make: String,
    val model: String,
    val service: String,
    val engine: String? = null
)

@Serializable
data class ServiceDocResponse(
    val status: String,
    val doc_id: String,
    val from_cache: Boolean,
    val generation_time: Double,
    val html_url: String
)

class ServiceDocAPI(private val apiKey: String) {
    private val baseUrl = "https://api.swoopservice.com"
    private val client = OkHttpClient()
    private val json = Json { ignoreUnknownKeys = true }
    
    fun generateDoc(
        vehicle: Vehicle,
        service: String,
        callback: (Result<ServiceDocResponse>) -> Unit
    ) {
        val requestBody = ServiceDocRequest(
            year = vehicle.year,
            make = vehicle.make,
            model = vehicle.model,
            service = service,
            engine = vehicle.engine
        )
        
        val request = Request.Builder()
            .url("$baseUrl/api/v1/documentation/generate")
            .addHeader("X-API-Key", apiKey)
            .post(json.encodeToString(requestBody).toRequestBody())
            .build()
        
        client.newCall(request).enqueue(object : Callback {
            override fun onResponse(call: Call, response: Response) {
                val body = response.body?.string() ?: ""
                val result = json.decodeFromString<ServiceDocResponse>(body)
                callback(Result.success(result))
            }
            
            override fun onFailure(call: Call, e: IOException) {
                callback(Result.failure(e))
            }
        })
    }
}

// Usage in Activity/Fragment
val api = ServiceDocAPI("your-api-key")
api.generateDoc(vehicle, "Oil Change") { result ->
    result.onSuccess { response ->
        // Load in WebView
        webView.loadUrl(
            "${api.baseUrl}${response.html_url}",
            mapOf("X-API-Key" to "your-api-key")
        )
    }
}
```

---

## Workflow Recommendation

### For Mobile Mechanic App

1. **Customer Books Job:**
   - Customer selects vehicle (year/make/model) and describes concern
   - App maps concern to service category

2. **Generate Documentation:**
   - Call `/api/v1/documentation/generate` with vehicle + service
   - Show loading indicator (~15s for first time, instant if cached)

3. **Display in Dashboard:**
   - Load HTML in WebView using returned `html_url`
   - Tech can view procedures, torque specs, parts needed

4. **Cache on Device (Optional):**
   - Save HTML locally for offline access
   - Check cache before API call to reduce latency

5. **Update as Needed:**
   - If customer concern changes, regenerate with new service
   - Use `force_regenerate=true` if specs may have updated

### Caching Strategy

```python
# Pseudo-code for smart caching in your app
def get_service_doc(vehicle, service):
    # 1. Check local cache first
    local_doc = local_cache.get(vehicle, service)
    if local_doc and not is_stale(local_doc):
        return local_doc
    
    # 2. Call API (will use server cache if available)
    response = api.generate_documentation(vehicle, service)
    
    # 3. Save to local cache
    local_cache.save(response.html_content)
    
    return response
```

---

## Error Handling

### HTTP Status Codes

- `200 OK`: Successful request
- `401 Unauthorized`: Invalid or missing API key
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Invalid request parameters
- `500 Internal Server Error`: Server error

### Error Response Format

```json
{
  "error": "Error message",
  "detail": "Detailed error information",
  "status_code": 404
}
```

### Common Errors

**Invalid API Key:**
```json
{
  "error": "Invalid or missing API key. Include 'X-API-Key' header.",
  "status_code": 401
}
```

**Vehicle Not Found:**
```json
{
  "error": "Failed to generate documentation: Vehicle not found: 2015 Toyota Camry",
  "status_code": 500
}
```

**Service Not Found:**
```json
{
  "error": "Failed to generate documentation: Service not found: Invalid Service",
  "status_code": 500
}
```

---

## Rate Limits

- **No rate limits** for cached document retrieval
- **15 second average** for new document generation (AI processing time)
- **Recommended:** Implement client-side caching to minimize API calls

---

## Interactive API Documentation

Visit `/docs` endpoint for interactive Swagger UI documentation:

```
http://localhost:8000/docs
```

Features:
- Try all endpoints directly in browser
- See request/response schemas
- Test authentication
- View example requests

Alternative ReDoc documentation:

```
http://localhost:8000/redoc
```

---

## Support & Contact

- **Email:** support@swoopserviceauto.com
- **Documentation:** https://docs.swoopservice.com
- **Status Page:** https://status.swoopservice.com

---

## Changelog

### Version 1.0.0 (2025-01-17)
- Initial API release
- Vehicle database: 5000+ configurations
- Service catalog: 150+ services
- Documentation generation with AI research
- Smart caching system
- Mobile-optimized HTML output
