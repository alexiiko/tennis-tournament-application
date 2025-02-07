import pyautogui as pag
import keyboard as kb
import pyperclip
import constants
import json
import re
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
    pag.hotkey("ctrl", "-")
    pag.hotkey("ctrl", "-")

    sleep(1)

    def get_tournament_location() -> Dict[str, Dict[str, str]]:
        pag.scroll(-10000) # get to bottom of the page
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        pag.scroll(constants.TOURNAMENT_INFO_OFFSET)
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        pag.click(constants.COURT_FACILITY_BUTTON)
        tournament_plz = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_PLZ, constants.RIGHT_TOURNAMENT_PLZ)
        tournament_street = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_STREET, constants.RIGHT_TOURNAMENT_STREET)

        return {"tournament_location": {"tournament_plz": tournament_plz, "tournament_street": tournament_street}}


    def get_tournament_dates() -> Dict[str, Dict[str, str]]:
        registration_start_existing = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_START_EXISTING, constants.RIGHT_TOURNAMENT_REGISTRATION_START_EXISTING)
        sleep(2)
        if registration_start_existing == "Meldeschluss":
            tournament_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DATE, constants.RIGHT_TOURNAMENT_DATE)
            tournament_registration_start = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_START_RSP, constants.RIGHT_TOURNAMENT_REGISTRATION_START_RSP)
            tournament_registration_end = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_END_RSP, constants.RIGHT_TOURNAMENT_REGISTRATION_END_RSP)
            tournament_draw_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DRAW_DATE_RSP, constants.RIGHT_TOURNAMENT_DRAW_DATE_RSP)
            return {"tournament_dates": {"tournament_date": tournament_date, "tournament_registration_start": tournament_registration_start,"tournament_registration_end": tournament_registration_end, "tournament_draw_date": tournament_draw_date}}
        else:
            tournament_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DATE, constants.RIGHT_TOURNAMENT_DATE)
            tournament_registration_end = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_END, constants.RIGHT_TOURNAMENT_REGISTRATION_END)
            tournament_draw_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DRAW_DATE, constants.RIGHT_TOURNAMENT_DRAW_DATE)

            return {"tournament_dates": {"tournament_date": tournament_date, "tournament_registration_start": "Nicht angegeben","tournament_registration_end": tournament_registration_end, "tournament_draw_date": tournament_draw_date}}


    def get_tournament_title() -> Dict[str, str]:
        pag.scroll(constants.SCROLL_AMOUNT_TO_TOP)
        sleep(constants.SLEEP_TIME_FOR_LOADING)
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
    sleep(constants.SLEEP_TIME_FOR_LOADING)
    tournament_amount = int(re.sub(r'\D', '', copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_AMOUNT, constants.RIGHT_TOURNAMENT_AMOUNT))) # only get the numbers out of the string
    pag.scroll(constants.SEE_TOURNAMENTS_OFFSET)
    sleep(constants.SLEEP_TIME_FOR_LOADING)

    amount_show_more_tournaments_button = round(tournament_amount / 10)

    for tournament_number in range(9, tournament_amount):
        pag.click(constants.SHOW_TOURNAMENT_BUTTON)
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        get_tournament_data()
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        pag.click(constants.PAGE_BACK_BUTTON)
        pag.moveTo(constants.SEARCH_TOURNAMENTS_BUTTON)
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        pag.hotkey("ctrl", "0")
        pag.hotkey("ctrl", "-")
        pag.hotkey("ctrl", "-")
        pag.hotkey("ctrl", "-")
        pag.hotkey("ctrl", "-")
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        pag.scroll(constants.SCROLL_AMOUNT_TO_TOP)
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        pag.scroll(constants.SEE_TOURNAMENTS_OFFSET)
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        pag.scroll(constants.NEXT_TOURNAMENT_OFFSET * tournament_number)
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        if tournament_number % 10 == 0 and amount_show_more_tournaments_button > 0:
            print(tournament_number - 1)
            pag.click(constants.SHOW_MORE_TOURNAMENTS_BUTTON)
            amount_show_more_tournaments_button -= 1 
            sleep(constants.SLEEP_TIME_FOR_LOADING)
            pag.scroll(constants.SCROLL_AMOUNT_TO_TOP)
            sleep(constants.SLEEP_TIME_FOR_LOADING)
            pag.scroll(constants.SEE_TOURNAMENTS_OFFSET)
            sleep(constants.SLEEP_TIME_FOR_LOADING)
            pag.scroll(constants.NEXT_TOURNAMENT_OFFSET * (tournament_number))
            sleep(constants.SLEEP_TIME_FOR_LOADING)
            pag.click(constants.SHOW_MORE_TOURNAMENTS_BUTTON)
            sleep(constants.SLEEP_TIME_FOR_LOADING)
        else:
            continue


while True:
    if kb.is_pressed("a"):
        tournament_data = get_tournament_data()
        print(tournament_data)
        sleep(0.5)
    elif kb.is_pressed("b"):
        # open the platform
        pag.hotkey("super", "shift", "2")
        sleep(constants.SLEEP_TIME_FOR_LOADING)
        pyperclip.copy("https://www.tennis.de/spielen/turniersuche.html#search")
        pag.hotkey("ctrl", "v")
        pag.press("enter")
        sleep(constants.SLEEP_TIME_FOR_LOADING + 3)
        pag.hotkey("ctrl", "0")
        pag.hotkey("ctrl", "-")
        pag.hotkey("ctrl", "-")
        pag.hotkey("ctrl", "-")
        pag.hotkey("ctrl", "-")

        scroll_through_tournaments()
        sleep(0.5)
