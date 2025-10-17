#!/bin/bash
# Start the Swoop Service Auto REST API

echo "🚀 Starting Swoop Service Auto API..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import fastapi" 2>/dev/null; then
    echo "📦 Installing API dependencies..."
    pip install -r requirements.txt
fi

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Copying from .env.example..."
    cp .env.example .env
    echo "⚠️  Please edit .env with your API keys before continuing."
    exit 1
fi

# Get port from .env or use default
PORT=$(grep "^API_PORT=" .env | cut -d '=' -f2 | tr -d ' ' || echo "8000")

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║          Swoop Service Auto REST API                         ║"
echo "╠═══════════════════════════════════════════════════════════════╣"
echo "║  📡 API Server: http://localhost:$PORT                        ║"
echo "║  📚 Docs:       http://localhost:$PORT/docs                   ║"
echo "║  📖 ReDoc:      http://localhost:$PORT/redoc                  ║"
echo "║  🔒 Auth:       X-API-Key header required                    ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Start the API server
python api.py
