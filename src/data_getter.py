import pyautogui as pag
import position_constants
from time import sleep


pag.hotkey("super", "shift", "2")

sleep(2)

pag.write("https://spieler.tennis.de/group/guest/turniere")
pag.press("enter")

