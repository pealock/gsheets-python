@echo off

REM set window size
MODE 50,10

REM connect to wifi
netsh wlan connect ssid="RHX8-Q4AM#CF02BF" name="RHX8-Q4AM#CF02BF"

REM cd to git repo directory and launch script
cd %HOMEPATH%\Desktop\pealock\pySheets\py
python ./number.py