import pyautogui as pag
import keyboard as kb
import pyperclip
import constants
import json
from time import sleep
from typing import Tuple, Dict


# helper function for saving code lines
def copy_text_and_return_as_variable(location_left: Tuple[int,int], location_right: Tuple[int,int,]):
    pag.moveTo(location_left)
    pag.mouseDown()
    pag.moveTo(location_right)
    pag.mouseUp()
    pag.hotkey("ctrl", "c")

    return str(pyperclip.paste()).replace("\n", "").replace("\r", "").replace("\t", "")


def get_tournament_data() -> str:
    def get_tournament_location() -> Dict[str, Dict[str, str]]:
        pag.scroll(-10000) # get to bottom of the page
        sleep(0.5)
        pag.scroll(constants.TOURNAMENT_INFO_OFFSET)
        sleep(0.5)
        pag.click(constants.COURT_FACILITY_BUTTON)
        tournament_plz = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_PLZ, constants.RIGHT_TOURNAMENT_PLZ)
        tournament_street = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_STREET, constants.RIGHT_TOURNAMENT_STREET)

        return {"tournament_location": {"tournament_plz": tournament_plz, "tournament_street": tournament_street}}


    def get_tournament_dates() -> Dict[str, Dict[str, str]]:
        tournament_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DATE, constants.RIGHT_TOURNAMENT_DATE)
        # if there is registration start button (check with screenshot) then add it into here 
        tournament_registration_end = copy_text_and_return_as_variable(constants.LEFT_REGISTRATION_END, constants.RIGHT_REGISTRATION_END)
        tournament_draw_date = copy_text_and_return_as_variable(constants.LEFT_DRAW_DATE, constants.RIGHT_DRAW_DATE)

        return {"tournament_dates": {"tournament_date": tournament_date, "tournament_registration_end": tournament_registration_end, "tournament_draw_date": tournament_draw_date}}


    def get_tournament_title() -> Dict[str, str]:
        pag.scroll(5000)
        sleep(0.5)
        tournament_title = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_TITLE, constants.RIGHT_TOURNAMENT_TITLE)
        return {"tournament_title": tournament_title}


    def get_tournament_link() -> Dict[str, str]:
        pag.moveTo(constants.TOURNAMENT_LINK)
        pag.click()
        pag.hotkey("ctrl", "c")
        return {"tournament_link": str(pyperclip.paste())}

    return json.dumps(get_tournament_title() | get_tournament_dates() | get_tournament_location() | get_tournament_link())


def scroll_through_tournaments():
    pag.click(constants.SEARCH_TOURNAMENTS_BUTTON)
    sleep(2)
    tournament_amount = int(copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_AMOUNT, constants.RIGHT_TOURNAMENT_AMOUNT))
    pag.scroll(constants.SEE_TOURNAMENTS_OFFSET)
    sleep(2)

    for tournament_number in range(1, tournament_amount):
        # if mehr turniere anzeigen on screen:
        # click the mehr turniere anzeigen button 
        # go to the top of the page 
        # go down via the offsets
        # else everything down below
        pag.click(constants.SHOW_TOURNAMENT_BUTTON)
        sleep(2)
        get_tournament_data()
        sleep(2)
        pag.click(constants.PAGE_BACK_BUTTON)
        sleep(2)
        pag.moveTo(constants.SEARCH_TOURNAMENTS_BUTTON)
        sleep(2)
        pag.scroll(5000)
        sleep(2)
        pag.scroll(constants.SEE_TOURNAMENTS_OFFSET)
        sleep(2)
        pag.scroll(constants.NEXT_TOURNAMENT_OFFSET * tournament_number)
        sleep(2)


while True:
    if kb.is_pressed("a"):
        tournament_data = get_tournament_data()
        print(tournament_data)
        sleep(0.5)
    elif kb.is_pressed("b"):
        # open the platform
        pag.hotkey("super", "shift", "2")
        sleep(2)
        pag.write("https://spieler.tennis.de/group/guest/turniere")
        pag.press("enter")

        scroll_through_tournaments()
        sleep(0.5)
