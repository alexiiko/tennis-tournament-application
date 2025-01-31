import pyautogui as pag
import keyboard as kb
from time import sleep

context = input()
while True:
    if kb.is_pressed("a"):
        mouse_x, mouse_y = pag.position()
        print(mouse_x, mouse_y)
        print()
        sleep(0.5)

        with open("pos_list.txt", "a") as file:
            file.write(context + ": " + str(mouse_x) + "|" + str(mouse_y) + "\n" + "\n")

        context = input()
