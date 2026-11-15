@echo off
where py >nul 2>nul && (py -3.11 "%~dp0install.py" --os windows & goto end)
where python >nul 2>nul && (python "%~dp0install.py" --os windows & goto end)
echo Instale Python 3.11 64-bit antes de prosseguir.
:end
pause
