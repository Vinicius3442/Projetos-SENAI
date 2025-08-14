import pyautogui
import time

xreset, yreset = 744, 242
x, y = 40, 737

# Deadzone (área segura para parar o script)
deadzone_x, deadzone_y = 50, 50  # se o mouse estiver dentro de (0–50, 0–50)

print("Iniciando em 5 segundos... Mova o mouse para (0,0) para parar o script.")
time.sleep(5)

while True:
    # Verifica se o mouse está na deadzone
    mouse_x, mouse_y = pyautogui.position()
    if mouse_x <= deadzone_x and mouse_y <= deadzone_y:
        print("Script encerrado (mouse na deadzone).")
        break

    # Pressiona 'e' 50 vezes
    for _ in range(50):
        pyautogui.press('e')
        time.sleep(0.05)

        # Verifica a deadzone durante a repetição
        mouse_x, mouse_y = pyautogui.position()
        if mouse_x <= deadzone_x and mouse_y <= deadzone_y:
            print("Script eencerrado (mouse na deadzone).")
            exit()

    # Clique no ponto definido
    pyautogui.click(x, y)
    time.sleep(0.5)
    
    # move pro reset
    pyautogui.click(xreset, yreset)



