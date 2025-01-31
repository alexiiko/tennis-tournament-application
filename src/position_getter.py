import pyautogui as pag
import keyboard as kb
from time import sleep

context = input()

scroll_count = 0

while True:
    if kb.is_pressed("a"):
        mouse_x, mouse_y = pag.position()
        print(mouse_x, mouse_y)
        print()
        sleep(0.5)

        with open("pos_list.txt", "a") as file:
            file.write(context + ": " + str(mouse_x) + "|" + str(mouse_y) + "\n" + "\n")

        context = input()

    elif kb.is_pressed("b"):
        pag.moveTo(1060,1168)

    elif kb.is_pressed("c"):
        pag.scroll(-10)
        scroll_count += 1  
        sleep(0.5)

    elif kb.is_pressed("d"):
        print(scroll_count)
        print()
        sleep(0.5)
