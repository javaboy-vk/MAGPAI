@echo off
REM =============================================================================
REM Script Name: run-magpai-agent-demo-v1.1.cmd
REM Author: javaboy-vk
REM Date: 2026-06-04
REM Version: 1.1
REM Description: Starts the MAGPAI Agent Demo v1.1 local email-enabled server.
REM =============================================================================

cd /d "%~dp0..\.."
start "" /b cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:8088/"
python "src\magpai\agent\email_server.v1.1.py"
pause
