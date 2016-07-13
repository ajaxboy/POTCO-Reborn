@echo off
title POTCO - Reborn

set /P PPYTHON_PATH=<PPYTHON_PATH
REM set GAME_SERVER=127.0.0.1
REM ^ Will be used later when networking is introduced
set LOGIN_COOKIE=Pirate
set /P LOGIN_COOKIE="Username: "

echo ==============================
echo Starting POTCO - Reborn...
echo Username: %LOGIN_COOKIE%
echo ==============================

%PPYTHON_PATH% -m PiratesStart %LOGIN_COOKIE%
pause