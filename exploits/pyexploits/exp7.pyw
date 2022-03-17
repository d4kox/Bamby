import pyautogui as pg
try:
    def runCommand(comando):
        pg.press('win')
        pg.write('cmd')
        pg.press('right')
        pg.press('down')
        pg.press('enter')
        pg.press('left')
        pg.press('enter')
        pg.write(comando)

    comando = input("Command >>> ")
    runCommand(comando)
except KeyboardInterrupt:
    pg.hotkey('win','r')
    pg.write('cmd')
    pg.press('enter')
    pg.write('C:')
    pg.press('enter')
    pg.write('cd "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\exploits"')
    pg.press('enter')
    pg.write('python exp7.pyw')
    pg.press('enter')