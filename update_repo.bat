@echo off

REM set window size
MODE 50,10

REM Move to working dir & update repo
cd %HOMEPATH%\Desktop\pealock\pySheets\
git pull

REM Require user to exit
pause