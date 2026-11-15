@echo off
setlocal
"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup\hall_d.ps1" -Acao VozCompleta
set "HALL_D_EXIT=%ERRORLEVEL%"
if not "%HALL_D_EXIT%"=="0" echo [ERRO] Codigo %HALL_D_EXIT%. Confira a mensagem acima.
echo.
pause
exit /b %HALL_D_EXIT%
