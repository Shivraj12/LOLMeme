@echo off
echo 🚀 Setting up LOLMeme project...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed. Please install Node.js 16+ first.
    pause
    exit /b 1
)

REM Create virtual environment
echo 📦 Creating Python virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install backend dependencies
echo 📥 Installing backend dependencies...
cd backend
pip install -r requirements.txt
cd ..

REM Install frontend dependencies
echo 📥 Installing frontend dependencies...
cd frontend
npm install
cd ..

echo ✅ Setup complete!
echo.
echo 🎯 Next steps:
echo 1. Set your HF_TOKEN environment variable:
echo    set HF_TOKEN=your_huggingface_token_here
echo.
echo 2. Start the backend:
echo    cd backend ^&^& python app.py
echo.
echo 3. Start the frontend (in a new terminal):
echo    cd frontend ^&^& npm run dev
echo.
echo 4. Open http://localhost:3000 in your browser
echo.
echo 🤖 Happy meme generating!
pause
