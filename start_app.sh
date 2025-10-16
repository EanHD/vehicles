#!/bin/bash
# Swoop Service Auto - Quick Start Script

cd "$(dirname "$0")"

echo "=============================================="
echo "  Swoop Service Auto"
echo "  Professional Service Documentation System"
echo "=============================================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "   Please run: python3 -m venv venv"
    exit 1
fi

# Activate venv
source venv/bin/activate

# Check dependencies
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -q -r requirements.txt
fi

echo "✅ Environment ready"
echo "✅ Starting web application..."
echo ""
echo "   URL: http://localhost:8501"
echo "   Press Ctrl+C to stop"
echo ""
echo "=============================================="
echo ""

# Start streamlit
streamlit run app.py --server.port 8501 --server.address 0.0.0.0

