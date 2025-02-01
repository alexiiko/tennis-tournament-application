import pyautogui as pag
import keyboard as kb
import pyperclip
import constants
from time import sleep
from typing import Dict, Tuple

'''
pag.hotkey("super", "shift", "2")

sleep(2)

pag.write("https://spieler.tennis.de/group/guest/turniere")
pag.press("enter")
'''

# helper function for saving code lines
def copy_text_and_return_as_variable(location_left: Tuple[int,int], location_right: Tuple[int,int,]):
    pag.moveTo(location_left)
    pag.mouseDown()
    pag.moveTo(location_right)
    pag.mouseUp()
    pag.hotkey("ctrl", "c")

    return str(pyperclip.paste()).replace("\n", "").replace("\r", "").replace("\t", "")


def get_tournament_location_and_organizer() -> Dict[str, str]:
    pag.scroll(constants.COURT_FACILITY_SITE_OFFSET)
    pag.moveTo(1060,1168)
    pag.scroll(constants.GET_TO_COURT_FACILITY)
    pag.click()

    sleep(1)
    
    tournament_plz = copy_text_and_return_as_variable(constants.PLZ_LOCATION_LEFT, constants.PLZ_LOCATION_RIGHT)
    tournament_street = copy_text_and_return_as_variable(constants.STREET_LEFT, constants.STREET_RIGHT)
    tournament_organizer = copy_text_and_return_as_variable(constants.TOURNAMENT_ORGANIZER_LEFT, constants.TOURNAMENT_ORGANIZER_RIGHT)

    return {"tournament_plz": tournament_plz, "tournament_street": tournament_street, "tournament_organizer": tournament_organizer}


def get_tournament_name() -> Dict[str, str]:
    pag.scroll(constants.COURT_FACILITY_SITE_OFFSET)

    tournament_title = copy_text_and_return_as_variable(constants.TITLE_LEFT, constants.TITLE_RIGHT)

    return {"tournament_title": tournament_title}


def get_tournament_dates() -> Dict[str, str]:
    pag.scroll(constants.COURT_FACILITY_SITE_OFFSET)

    tournament_date = copy_text_and_return_as_variable(constants.DATE_LEFT, constants.DATE_RIGHT)
    tournament_registration_start = copy_text_and_return_as_variable(constants.REGISTRATION_START_LEFT, constants.REGISTRATION_START_RIGHT)
    tournament_registration_end = copy_text_and_return_as_variable(constants.REGISTRATION_DEADLINE_LEFT, constants.REGISTRATION_DEADLINE_RIGHT)
    tournament_draw = copy_text_and_return_as_variable(constants.DRAW_LEFT, constants.DRAW_RIGHT)

    return {"tournament_date": tournament_date, "tournament_registration_start": tournament_registration_start, "tournament_registration_end": tournament_registration_end, "tournament_draw": tournament_draw}


while True:
    if kb.is_pressed("a"):
        tournament_data = get_tournament_location_and_organizer() | get_tournament_dates() | get_tournament_name()
        print(tournament_data)
        sleep(0.5)
