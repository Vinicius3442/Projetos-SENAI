import pyautogui
import time


print("Mova o mouse para o local desejado. A posição será mostrada em 5 segundos...")
time.sleep(5)
print("Posição do mouse:", pyautogui.position())