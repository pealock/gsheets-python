@echo off

REM set window size
MODE 50,10

REM connect to wifi
netsh wlan connect ssid="RHX8-Q4AM#CEDD61" name="RHX8-Q4AM#CEDD61"

REM cd to git repo directory and launch script
cd %HOMEPATH%\Desktop\pealock\pySheets\py
python ./number.py
