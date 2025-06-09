import pyautogui as pag
import time

# pyautogui é uma biblioteca que permite controlar o mouse e o teclado do computador
# pag.press é usado para simular a pressão de uma tecla
# pag.write é usado para escrever um texto
# pag.click é usado para clicar em uma posição específica da tela
# pag.PAUSE é usado para definir um tempo de pausa entre as ações


pag.PAUSE = 0.5 
pag.press("win")
pag.write("chrome")
pag.press("enter")
time.sleep(2)
pag.press("enter")
pag.write("http://youtube.com/watch?v=E0ozmU9cJDg")
pag.press("enter")

# Conhecimentos adquiridos por meio da semana de Python da Hashtag Programação