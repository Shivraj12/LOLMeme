@echo off
echo Starting LOLMeme servers...

echo.
echo Starting Backend...
start "LOLMeme Backend" cmd /k "cd /d %~dp0 && venv\Scripts\activate && cd backend && python app.py"

echo.
echo Starting Frontend...
start "LOLMeme Frontend" cmd /k "cd /d %~dp0 && cd frontend && npm run dev"

echo.
echo Both servers are starting...
echo Backend will be available at: http://localhost:5000
echo Frontend will be available at: http://localhost:3000
echo.
echo Press any key to exit this window...
pause
