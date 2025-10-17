@echo off
echo ========================================
echo Smart Resume Screener - Starting...
echo ========================================
echo.

cd /d "%~dp0"

echo [1/2] Starting Backend API...
start "Backend API" cmd /k "venv\Scripts\python.exe app.py"
timeout /t 3 /nobreak > nul

echo [2/2] Starting Frontend Server...
start "Frontend Server" cmd /k "cd frontend && ..\venv\Scripts\python.exe -m http.server 8000"
timeout /t 2 /nobreak > nul

echo.
echo ========================================
echo    READY TO USE!
echo ========================================
echo.
echo Backend API:  http://localhost:5000
echo Frontend:     http://localhost:8000
echo.
echo Opening frontend in browser...
start http://localhost:8000
echo.
echo Press any key to stop all servers...
pause > nul

echo.
echo Stopping servers...
taskkill /FI "WINDOWTITLE eq Backend API*" /T /F > nul 2>&1
taskkill /FI "WINDOWTITLE eq Frontend Server*" /T /F > nul 2>&1
echo Done!
