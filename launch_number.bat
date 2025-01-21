REM set window size
MODE 50,10

REM connect to wifi
REM netsh wlan connect ssid="" name="My Name"

REM Launch LED control app
start "C:\Users\BA Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ÈðºÏÐÅPlus V8.0°æ\ÈðºÏÐÅPlus.lnk"

REM cd to git repo directory and launch script
cd %HOMEPATH%\Desktop\pealock\gsheets-python
python ./number.py