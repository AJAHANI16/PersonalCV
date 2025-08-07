#!/bin/bash

# PersonalCV Development Script
# Quick commands for development workflow

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

show_help() {
    echo "PersonalCV Development Script"
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  serve     Start development server (default port 8000)"
    echo "  build     Build optimized version for production"
    echo "  deploy    Build and prepare for deployment"
    echo "  clean     Clean build artifacts"
    echo "  help      Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 serve"
    echo "  $0 build"
    echo "  $0 deploy"
    echo ""
}

serve() {
    echo "🚀 Starting PersonalCV development server..."
    echo "📂 Project directory: $PROJECT_DIR"
    
    # Check if Python 3 is available
    if command -v python3 &> /dev/null; then
        echo "🐍 Using Python 3"
        python3 scripts/dev-server.py
    elif command -v python &> /dev/null; then
        echo "🐍 Using Python"
        python scripts/dev-server.py  
    else
        echo "❌ Python not found. Please install Python to run the development server."
        echo "💡 Alternative: Open index.html directly in your browser (some features may not work)"
        exit 1
    fi
}

build() {
    echo "🏗️  Building PersonalCV for production..."
    
    if command -v python3 &> /dev/null; then
        python3 scripts/build.py
    elif command -v python &> /dev/null; then
        python scripts/build.py
    else
        echo "❌ Python not found. Please install Python to build the project."
        exit 1
    fi
    
    echo "✅ Build complete!"
}

deploy() {
    echo "🚀 Preparing PersonalCV for deployment..."
    
    if command -v python3 &> /dev/null; then
        python3 scripts/build.py deploy
    elif command -v python &> /dev/null; then
        python scripts/build.py deploy
    else
        echo "❌ Python not found. Please install Python to prepare deployment."
        exit 1
    fi
    
    echo "✅ Deployment preparation complete!"
}

clean() {
    echo "🧹 Cleaning build artifacts..."
    
    if [ -d "build" ]; then
        rm -rf build
        echo "✅ Removed build directory"
    else
        echo "ℹ️  No build directory found"
    fi
    
    # Remove any temporary files
    find . -name "*.pyc" -delete 2>/dev/null || true
    find . -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    
    echo "✅ Cleanup complete!"
}

# Main script logic
case "${1:-serve}" in
    "serve")
        serve
        ;;
    "build")
        build
        ;;
    "deploy")
        deploy
        ;;
    "clean")
        clean
        ;;
    "help"|"-h"|"--help")
        show_help
        ;;
    *)
        echo "❌ Unknown command: $1"
        echo ""
        show_help
        exit 1
        ;;
esac