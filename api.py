#!/usr/bin/env python3
"""
Swoop Service Auto - REST API
FastAPI-based REST API for mobile mechanic app integration
Provides service documentation generation and retrieval endpoints
"""

from fastapi import FastAPI, HTTPException, Query, Path as PathParam, BackgroundTasks, Depends, Header
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from pathlib import Path
import json
import sys
import os
from datetime import datetime
import hashlib

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent / "tools"))
from service_doc_generator import ServiceDocGenerator

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# API Configuration
API_VERSION = "1.0.0"
API_TITLE = "Swoop Service Auto API"
API_DESCRIPTION = """
## Professional Automotive Service Documentation API

This API provides programmatic access to the Swoop Service Auto documentation system.
It enables mobile mechanic apps to automatically generate and retrieve professional service documentation
based on vehicle specifications and customer concerns.

### Key Features
- 🚗 **Vehicle Database**: 5000+ vehicle configurations (1940s-2025)
- 🔧 **Service Catalog**: 150+ common automotive services
- 📄 **Auto-Generation**: AI-powered service documentation with torque specs, fluids, parts, and procedures
- 💾 **Smart Caching**: Automatic caching to reduce generation time and API costs
- 🔒 **API Key Auth**: Secure access with API key authentication
- 📱 **Mobile-Optimized**: HTML output optimized for mobile viewing

### Authentication
All endpoints (except `/` and `/docs`) require an API key passed via the `X-API-Key` header:
```
X-API-Key: your-api-key-here
```

### Typical Workflow
1. **Search Vehicles**: Use `/api/v1/vehicles/search` to find the exact vehicle
2. **List Services**: Use `/api/v1/services` to get available service types
3. **Generate Documentation**: Call `/api/v1/documentation/generate` with vehicle + service
4. **Retrieve HTML**: Use the returned `doc_id` or `html_url` to get the formatted documentation
5. **Display in App**: Show the HTML in a WebView or embedded browser

### Rate Limits
- Cached documents: No limit (instant retrieval)
- New generations: ~15 seconds per document (AI processing time)
- Recommended: Cache on your end and only regenerate when needed

### Support
For issues or questions, contact: support@swoopserviceauto.com
"""

# Initialize FastAPI app
app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/api/openapi.json"
)

# CORS Configuration - adjust origins for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your mobile app domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key Configuration
API_KEY = os.getenv("API_KEY", "swoop-dev-key-change-in-production")

def verify_api_key(x_api_key: Optional[str] = Header(None)):
    """Verify API key from header"""
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key. Include 'X-API-Key' header."
        )
    return x_api_key

# Initialize generator (singleton pattern)
_generator = None

def get_generator() -> ServiceDocGenerator:
    """Get or create the service doc generator instance"""
    global _generator
    if _generator is None:
        _generator = ServiceDocGenerator(enable_diagrams=False)
    return _generator

# ============================================================================
# Pydantic Models (Request/Response schemas)
# ============================================================================

class HealthResponse(BaseModel):
    status: str = Field(..., description="API health status")
    version: str = Field(..., description="API version")
    timestamp: str = Field(..., description="Current server timestamp")
    database_stats: Dict[str, int] = Field(..., description="Database statistics")

class Vehicle(BaseModel):
    year: int = Field(..., description="Model year", example=2015)
    make: str = Field(..., description="Manufacturer", example="Toyota")
    model: str = Field(..., description="Model name", example="Camry")
    engine: Optional[str] = Field(None, description="Engine specification", example="2.5L 4-Cyl")
    transmission: Optional[str] = Field(None, description="Transmission type", example="Automatic")
    body_style: Optional[str] = Field(None, description="Body style", example="Sedan")

class Service(BaseModel):
    id: str = Field(..., description="Service ID")
    name: str = Field(..., description="Service name", example="Oil Change")
    category: str = Field(..., description="Service category", example="Maintenance")
    description: str = Field(..., description="Service description")
    flat_rate_hours: Optional[float] = Field(None, description="Standard labor time in hours")
    difficulty: Optional[int] = Field(None, description="Difficulty rating (1-5)")
    skill_level: Optional[str] = Field(None, description="Required skill level")

class GenerateDocRequest(BaseModel):
    year: int = Field(..., description="Model year", ge=1940, le=2026, example=2015)
    make: str = Field(..., description="Manufacturer", example="Toyota")
    model: str = Field(..., description="Model name", example="Camry")
    service: str = Field(..., description="Service name", example="Oil Change")
    engine: Optional[str] = Field(None, description="Engine specification")
    transmission: Optional[str] = Field(None, description="Transmission type")
    body_style: Optional[str] = Field(None, description="Body style")
    force_regenerate: bool = Field(False, description="Force regeneration even if cached")
    
    class Config:
        schema_extra = {
            "example": {
                "year": 2015,
                "make": "Toyota",
                "model": "Camry",
                "service": "Oil Change",
                "engine": "2.5L 4-Cyl",
                "transmission": "Automatic",
                "body_style": "Sedan",
                "force_regenerate": False
            }
        }

class GenerateDocResponse(BaseModel):
    status: str = Field(..., description="Generation status")
    doc_id: str = Field(..., description="Unique document identifier")
    from_cache: bool = Field(..., description="Whether document was retrieved from cache")
    generation_time: float = Field(..., description="Generation time in seconds")
    html_url: str = Field(..., description="URL to retrieve HTML document")
    metadata: Dict[str, Any] = Field(..., description="Document metadata")

class DocumentMetadata(BaseModel):
    doc_id: str
    vehicle: Vehicle
    service: str
    generated_at: str
    file_size: int
    cached: bool

class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")

# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/", response_model=Dict[str, str], tags=["General"])
async def root():
    """
    API root endpoint - provides basic information and quick links
    """
    return {
        "message": "Swoop Service Auto API",
        "version": API_VERSION,
        "documentation": "/docs",
        "health_check": "/api/v1/health"
    }

@app.get("/api/v1/health", response_model=HealthResponse, tags=["General"])
async def health_check():
    """
    Health check endpoint - verify API is operational and get database stats
    
    Returns current API status, version, and database statistics.
    No authentication required.
    """
    gen = get_generator()
    
    return HealthResponse(
        status="healthy",
        version=API_VERSION,
        timestamp=datetime.now().isoformat(),
        database_stats={
            "total_vehicles": len(gen.vehicles),
            "total_services": len(gen.services),
            "cached_documents": len(gen.cache_index)
        }
    )

@app.get("/api/v1/vehicles", response_model=List[Vehicle], tags=["Vehicles"])
async def list_vehicles(
    make: Optional[str] = Query(None, description="Filter by manufacturer"),
    year: Optional[int] = Query(None, description="Filter by year", ge=1940, le=2026),
    limit: int = Query(100, description="Maximum results to return", ge=1, le=1000),
    api_key: str = Depends(verify_api_key)
):
    """
    List vehicles from database with optional filtering
    
    Returns a list of vehicles matching the specified filters.
    Use this endpoint to help users select their vehicle.
    """
    gen = get_generator()
    vehicles = gen.vehicles
    
    # Apply filters
    if make:
        vehicles = [v for v in vehicles if v.get("make", "").lower() == make.lower()]
    if year:
        vehicles = [v for v in vehicles if v.get("year") == year]
    
    # Limit results
    vehicles = vehicles[:limit]
    
    # Convert to response model
    result = []
    for v in vehicles:
        result.append(Vehicle(
            year=v["year"],
            make=v["make"],
            model=v["model"],
            engine=v.get("engine"),
            transmission=v.get("transmission"),
            body_style=v.get("body_style")
        ))
    
    return result

@app.get("/api/v1/vehicles/search", response_model=List[Vehicle], tags=["Vehicles"])
async def search_vehicles(
    q: str = Query(..., description="Search query (searches make, model, engine)", min_length=2),
    limit: int = Query(50, description="Maximum results to return", ge=1, le=500),
    api_key: str = Depends(verify_api_key)
):
    """
    Search vehicles by keyword
    
    Searches across make, model, and engine fields. Returns best matches.
    Useful for autocomplete and vehicle selection in mobile apps.
    """
    gen = get_generator()
    q_lower = q.lower()
    
    # Search vehicles
    matches = []
    for v in gen.vehicles:
        # Create searchable string
        searchable = f"{v.get('make', '')} {v.get('model', '')} {v.get('engine', '')}".lower()
        if q_lower in searchable:
            matches.append(Vehicle(
                year=v["year"],
                make=v["make"],
                model=v["model"],
                engine=v.get("engine"),
                transmission=v.get("transmission"),
                body_style=v.get("body_style")
            ))
    
    return matches[:limit]

@app.get("/api/v1/vehicles/makes", response_model=List[str], tags=["Vehicles"])
async def list_makes(
    api_key: str = Depends(verify_api_key)
):
    """
    Get list of all manufacturers in database
    
    Returns unique list of makes for populating dropdowns.
    """
    gen = get_generator()
    makes = sorted(set(v["make"] for v in gen.vehicles))
    return makes

@app.get("/api/v1/vehicles/years", response_model=List[int], tags=["Vehicles"])
async def list_years(
    make: Optional[str] = Query(None, description="Filter years by manufacturer"),
    api_key: str = Depends(verify_api_key)
):
    """
    Get list of model years in database
    
    Returns unique list of years, optionally filtered by make.
    """
    gen = get_generator()
    vehicles = gen.vehicles
    
    if make:
        vehicles = [v for v in vehicles if v.get("make", "").lower() == make.lower()]
    
    years = sorted(set(v["year"] for v in vehicles), reverse=True)
    return years

@app.get("/api/v1/services", response_model=List[Service], tags=["Services"])
async def list_services(
    category: Optional[str] = Query(None, description="Filter by category"),
    api_key: str = Depends(verify_api_key)
):
    """
    List all available service types
    
    Returns complete service catalog. Use to populate service selection UI.
    """
    gen = get_generator()
    services = gen.services
    
    # Apply category filter if provided
    if category:
        services = [s for s in services if s.get("category", "").lower() == category.lower()]
    
    # Convert to response model
    result = []
    for s in services:
        result.append(Service(
            id=s.get("id", s["name"].lower().replace(" ", "_")),
            name=s["name"],
            category=s.get("category", "General"),
            description=s.get("description", ""),
            flat_rate_hours=s.get("flat_rate_hours"),
            difficulty=s.get("difficulty"),
            skill_level=s.get("skill_level")
        ))
    
    return result

@app.get("/api/v1/services/categories", response_model=List[str], tags=["Services"])
async def list_service_categories(
    api_key: str = Depends(verify_api_key)
):
    """
    Get list of service categories
    
    Returns unique list of service categories for filtering.
    """
    gen = get_generator()
    categories = sorted(set(s.get("category", "General") for s in gen.services))
    return categories

@app.post("/api/v1/documentation/generate", response_model=GenerateDocResponse, tags=["Documentation"])
async def generate_documentation(
    request: GenerateDocRequest,
    background_tasks: BackgroundTasks,
    api_key: str = Depends(verify_api_key)
):
    """
    Generate service documentation for a specific vehicle and service
    
    This is the primary endpoint for creating service documentation.
    Returns immediately with document metadata and URL.
    
    ### Process:
    1. Checks cache for existing document
    2. If not cached or force_regenerate=true, generates new documentation
    3. AI researches service procedures, specs, and common issues
    4. Formats professional HTML document
    5. Saves to cache for future requests
    
    ### Response includes:
    - `doc_id`: Unique identifier for retrieving the document
    - `html_url`: Direct URL to HTML document
    - `from_cache`: Whether document was cached (instant) or newly generated (~15s)
    - `metadata`: Vehicle and service information
    
    ### Usage in Mobile App:
    ```javascript
    // Generate documentation when job is booked
    const response = await fetch('/api/v1/documentation/generate', {
        method: 'POST',
        headers: {
            'X-API-Key': 'your-api-key',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            year: 2015,
            make: 'Toyota',
            model: 'Camry',
            service: 'Oil Change',
            engine: '2.5L 4-Cyl'
        })
    });
    
    const data = await response.json();
    
    // Display HTML in WebView
    webView.loadUrl(data.html_url);
    ```
    """
    gen = get_generator()
    
    start_time = datetime.now()
    
    try:
        # Generate documentation
        doc_path, from_cache = gen.generate(
            year=request.year,
            make=request.make,
            model=request.model,
            service=request.service,
            engine=request.engine,
            transmission=request.transmission,
            body_style=request.body_style,
            force_regenerate=request.force_regenerate
        )
        
        generation_time = (datetime.now() - start_time).total_seconds()
        
        # Generate doc_id (hash of request params)
        doc_id = gen._generate_cache_key(
            request.year, request.make, request.model, request.service,
            request.engine, request.transmission, request.body_style
        )
        
        # Get file size
        file_size = Path(doc_path).stat().st_size
        
        # Build response
        return GenerateDocResponse(
            status="success",
            doc_id=doc_id,
            from_cache=from_cache,
            generation_time=generation_time,
            html_url=f"/api/v1/documentation/{doc_id}/html",
            metadata={
                "vehicle": {
                    "year": request.year,
                    "make": request.make,
                    "model": request.model,
                    "engine": request.engine,
                    "transmission": request.transmission,
                    "body_style": request.body_style
                },
                "service": request.service,
                "generated_at": datetime.now().isoformat(),
                "file_size": file_size
            }
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate documentation: {str(e)}"
        )

@app.get("/api/v1/documentation/{doc_id}/html", response_class=HTMLResponse, tags=["Documentation"])
async def get_documentation_html(
    doc_id: str = PathParam(..., description="Document ID from generation response"),
    api_key: str = Depends(verify_api_key)
):
    """
    Retrieve HTML documentation by document ID
    
    Returns the formatted HTML document for display in WebView or browser.
    Documents are cached and can be retrieved instantly.
    
    ### Display in Mobile App:
    Simply load this URL in a WebView with the API key header:
    ```java
    // Android WebView
    WebView webView = findViewById(R.id.webview);
    Map<String, String> headers = new HashMap<>();
    headers.put("X-API-Key", "your-api-key");
    webView.loadUrl("https://api.swoopservice.com/api/v1/documentation/{doc_id}/html", headers);
    ```
    """
    gen = get_generator()
    
    # Find document in cache
    if doc_id not in gen.cache_index:
        raise HTTPException(
            status_code=404,
            detail=f"Document not found: {doc_id}. Generate it first using /api/v1/documentation/generate"
        )
    
    # Get file path
    cache_entry = gen.cache_index[doc_id]
    doc_path = gen.cache_dir / cache_entry["filename"]
    
    if not doc_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Document file not found. It may have been deleted."
        )
    
    # Read and return HTML
    with open(doc_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    return HTMLResponse(content=html_content)

@app.get("/api/v1/documentation/{doc_id}/metadata", response_model=DocumentMetadata, tags=["Documentation"])
async def get_documentation_metadata(
    doc_id: str = PathParam(..., description="Document ID"),
    api_key: str = Depends(verify_api_key)
):
    """
    Get metadata for a cached document
    
    Returns information about a document without retrieving the full HTML.
    """
    gen = get_generator()
    
    if doc_id not in gen.cache_index:
        raise HTTPException(status_code=404, detail="Document not found")
    
    cache_entry = gen.cache_index[doc_id]
    doc_path = gen.cache_dir / cache_entry["filename"]
    
    file_size = doc_path.stat().st_size if doc_path.exists() else 0
    
    return DocumentMetadata(
        doc_id=doc_id,
        vehicle=Vehicle(
            year=cache_entry["year"],
            make=cache_entry["make"],
            model=cache_entry["model"],
            engine=cache_entry.get("engine"),
            transmission=cache_entry.get("transmission"),
            body_style=cache_entry.get("body_style")
        ),
        service=cache_entry["service"],
        generated_at=cache_entry["generated_at"],
        file_size=file_size,
        cached=True
    )

@app.get("/api/v1/documentation", response_model=List[DocumentMetadata], tags=["Documentation"])
async def list_cached_documents(
    limit: int = Query(100, description="Maximum results", ge=1, le=1000),
    api_key: str = Depends(verify_api_key)
):
    """
    List all cached documents
    
    Returns metadata for all documents in the cache.
    Useful for browsing available documentation.
    """
    gen = get_generator()
    
    results = []
    for doc_id, cache_entry in list(gen.cache_index.items())[:limit]:
        doc_path = gen.cache_dir / cache_entry["filename"]
        file_size = doc_path.stat().st_size if doc_path.exists() else 0
        
        results.append(DocumentMetadata(
            doc_id=doc_id,
            vehicle=Vehicle(
                year=cache_entry["year"],
                make=cache_entry["make"],
                model=cache_entry["model"],
                engine=cache_entry.get("engine"),
                transmission=cache_entry.get("transmission"),
                body_style=cache_entry.get("body_style")
            ),
            service=cache_entry["service"],
            generated_at=cache_entry["generated_at"],
            file_size=file_size,
            cached=True
        ))
    
    return results

@app.delete("/api/v1/documentation/{doc_id}", tags=["Documentation"])
async def delete_documentation(
    doc_id: str = PathParam(..., description="Document ID to delete"),
    api_key: str = Depends(verify_api_key)
):
    """
    Delete a cached document
    
    Removes the document from cache. It can be regenerated if needed.
    """
    gen = get_generator()
    
    if doc_id not in gen.cache_index:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Get file path
    cache_entry = gen.cache_index[doc_id]
    doc_path = gen.cache_dir / cache_entry["filename"]
    
    # Delete file
    if doc_path.exists():
        doc_path.unlink()
    
    # Remove from index
    del gen.cache_index[doc_id]
    gen._save_cache_index()
    
    return {"status": "deleted", "doc_id": doc_id}

# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "status_code": exc.status_code}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """General exception handler"""
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

# ============================================================================
# Run Server
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("API_PORT", "8000"))
    host = os.getenv("API_HOST", "0.0.0.0")
    
    print(f"""
    ╔═══════════════════════════════════════════════════════════════╗
    ║          Swoop Service Auto API v{API_VERSION}                    ║
    ╠═══════════════════════════════════════════════════════════════╣
    ║  📡 Server: http://{host}:{port}                          ║
    ║  📚 Docs:   http://{host}:{port}/docs                     ║
    ║  🔒 Auth:   X-API-Key header required                        ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        "api:app",
        host=host,
        port=port,
        reload=True,  # Set to False in production
        log_level="info"
    )
