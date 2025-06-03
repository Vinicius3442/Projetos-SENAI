import pyautogui as pag
import time

mousepos = pag.position()

time.sleep(5)
print(f'Posição do mouse: {mousepos}')