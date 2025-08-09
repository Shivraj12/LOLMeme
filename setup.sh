#!/bin/bash

echo "🚀 Setting up LOLMeme project..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

# Create virtual environment
echo "📦 Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install backend dependencies
echo "📥 Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..

# Install frontend dependencies
echo "📥 Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Set your HF_TOKEN environment variable:"
echo "   export HF_TOKEN=your_huggingface_token_here"
echo ""
echo "2. Start the backend:"
echo "   cd backend && python app.py"
echo ""
echo "3. Start the frontend (in a new terminal):"
echo "   cd frontend && npm run dev"
echo ""
echo "4. Open http://localhost:3000 in your browser"
echo ""
echo "🤖 Happy meme generating!"
