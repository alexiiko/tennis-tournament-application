import pyautogui as pag
import keyboard as kb
import constants
from time import sleep

context = input()

scroll_down_ten = -10
scroll_down_one = -1

scroll_up_ten = 10
scroll_up_one = 1

scroll_count_down_ten = 0
scroll_count_down_one = 0

scroll_count_up_ten = 0
scroll_count_up_one = 0

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
        pag.scroll(scroll_down_ten)
        scroll_count_down_ten += 1 
        sleep(0.5)

    elif kb.is_pressed("d"):
        print(scroll_count_down_ten)
        print()
        scroll_count = 0
        sleep(0.5)

    elif kb.is_pressed("e"):
        pag.scroll(scroll_up_ten)
        scroll_count_up_ten += 1 
        sleep(0.5)

    elif kb.is_pressed("f"):
        print(scroll_count_up_ten)
        print()
        scroll_count_up_ten = 0
        sleep(0.5)

    elif kb.is_pressed("g"):
        pag.scroll(constants.SEE_TOURNAMENTS_OFFSET)
        sleep(0.5)
    
    elif kb.is_pressed("h"):
        pag.scroll(scroll_down_one)
        scroll_count_down_one += 1 
        sleep(0.5)

    elif kb.is_pressed("i"):
        print(scroll_count_down_one)
        print()
        scroll_count_down_one = 0
        sleep(0.5)

    elif kb.is_pressed("j"):
        pag.scroll(scroll_up_one)
        scroll_count_up_one += 1 
        sleep(0.5)

    elif kb.is_pressed("k"):
        print(scroll_count_up_one)
        print()
        scroll_count_up_one = 0
        sleep(0.5)
