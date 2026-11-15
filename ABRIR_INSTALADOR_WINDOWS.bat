@echo off
cd /d "%~dp0"
py -3.11 -c "import tkinter" >nul 2>nul
if not errorlevel 1 (py -3.11 "%~dp0INSTALADOR_GRAFICO.py" & goto end)
echo Python 3.11 64 bits com Tkinter e necessario.
echo https://www.python.org/downloads/
:end
pause
