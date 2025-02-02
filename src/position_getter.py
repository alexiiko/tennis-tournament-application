import pyautogui as pag
import keyboard as kb
import constants
from time import sleep

context = input()

scroll_count = 0
scroll_count_einer = 0

scroll_count_up = 0

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
        scroll_count = 0
        sleep(0.5)

    elif kb.is_pressed("e"):
        pag.scroll(10)
        scroll_count_up += 1 
        sleep(0.5)

    elif kb.is_pressed("f"):
        print(scroll_count_up)
        print()
        scroll_count_up = 0
        sleep(0.5)

    elif kb.is_pressed("g"):
        pag.scroll(constants.SEE_TOURNAMENTS_OFFSET)
        sleep(0.5)
    
    elif kb.is_pressed("h"):
        pag.scroll(-1)
        scroll_count_einer += 1 
        sleep(0.5)

    elif kb.is_pressed("i"):
        print(scroll_count_einer)
        print()
        scroll_count_einer = 0
        sleep(0.5)

    elif kb.is_pressed("j"):
        pag.scroll(2190)
        sleep(0.5)
