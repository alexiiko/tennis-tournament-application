import pyautogui as pag
import keyboard as kb
import pyperclip
import constants
import json
import re
from time import sleep, time
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
        sleep(1)
        tournament_plz = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_PLZ, constants.RIGHT_TOURNAMENT_PLZ)
        tournament_street = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_STREET, constants.RIGHT_TOURNAMENT_STREET)

        return {"tournament_location": {"tournament_plz": tournament_plz, "tournament_street": tournament_street}}


    def get_tournament_dates() -> Dict[str, Dict[str, str]]:
        registration_start_existing = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_START_EXISTING, constants.RIGHT_TOURNAMENT_REGISTRATION_START_EXISTING)
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
        kb.press_and_release("home")
        sleep(0.5)
        pag.scroll(-100)
        sleep(1)
        kb.press_and_release("home")
        sleep(1)
        tournament_title = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_TITLE, constants.RIGHT_TOURNAMENT_TITLE)
        return {"tournament_title": tournament_title}


    def get_tournament_link() -> Dict[str, str]:
        pag.moveTo(constants.TOURNAMENT_LINK)
        pag.click()
        pag.hotkey("ctrl", "c")
        return {"tournament_link": str(pyperclip.paste())}

    sleep(2)

    pag.hotkey("ctrl", "-")
    pag.hotkey("ctrl", "-")
    pag.hotkey("ctrl", "-")
    pag.hotkey("ctrl", "-")
    pag.hotkey("ctrl", "-")

    sleep(3)

    return json.dumps(get_tournament_title() | get_tournament_dates() | get_tournament_location() | get_tournament_link())


def scroll_through_tournaments():
    start_time = time()
    pag.hotkey("ctrl", "0")
    pag.hotkey("ctrl", "-")
    sleep(1)
    pag.click(constants.AGE_CLASS_BUTTON)
    sleep(1)
    pag.click(constants.RESET_SEARCH_OPTIONS_BUTTON)
    kb.press_and_release("home")
    sleep(2)

    age_class_men_list = list(constants.MEN_CLASSES)
    for age_class_index in range(len(age_class_men_list)): 
        pag.click(constants.AGE_CLASS_BUTTON)
        sleep(0.5)
        pag.moveTo(constants.AGE_CLASSES_SELECTOR)
        sleep(0.5)
        pag.scroll(-500)
        sleep(0.5)
        pag.click(constants.MEN_CLASSES[age_class_men_list[age_class_index]])
        sleep(0.5)
        if age_class_index > 0:
            pag.click(constants.MEN_CLASSES[age_class_men_list[age_class_index - 1]])
            sleep(0.5)
        sleep(0.5)

    pag.click(constants.SEARCH_TOURNAMENTS_BUTTON)
    sleep(3)
    tournament_amount = int(re.sub(r'\D', '', copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_AMOUNT, constants.RIGHT_TOURNAMENT_AMOUNT))) # only get the numbers out of the string

    amount_show_more_tournaments_button = round(tournament_amount / 10)

    pag.click(constants.MAP_VIEW_BUTTON)
    sleep(0.5)
    pag.press("tab", presses=23)
    pag.press("enter")
    for _ in range(amount_show_more_tournaments_button):
        pag.press("enter")
        sleep(0.5)

    for tournament_number in range(1, tournament_amount + 1):
        pag.hotkey("ctrl", "0")
        pag.hotkey("ctrl", "-")
        sleep(0.5)
        pag.click(constants.LEFT_SCREEN_EDGE)
        sleep(0.5)
        kb.press_and_release("home")
        sleep(2)
        pag.scroll(-100)
        sleep(1)
        kb.press_and_release("home")
        sleep(2)
        pag.click(constants.MAP_VIEW_BUTTON)
        sleep(0.5)

        pag.press("tab", presses=tournament_number*2+2)

        sleep(1)

        pag.press("enter")
        sleep(2)
        get_tournament_data()
        sleep(0.5)
        pag.click(constants.PAGE_BACK_BUTTON)
        sleep(2)

        print(f"Progess:{(tournament_number / tournament_amount) * 100}%")
        print(f"Scrolled through {tournament_number} tournaments.")
        print(f"{tournament_amount - tournament_number} left.")
        print(f"Elapsed time: {round((time() - start_time) / 60, 2)} minutes")
        print()


def open_tournament_platform():
    pag.hotkey("super", "shift", "2")
    sleep(constants.SLEEP_TIME_FOR_LOADING)
    pyperclip.copy("https://www.tennis.de/spielen/turniersuche.html#search")
    pag.hotkey("ctrl", "v")
    pag.press("enter")
    sleep(constants.SLEEP_TIME_FOR_LOADING + 3)


while True:
    if kb.is_pressed("a"):
        tournament_data = get_tournament_data()
        print(tournament_data)
        sleep(0.5)
    elif kb.is_pressed("b"):
        open_tournament_platform()
        scroll_through_tournaments()
        sleep(0.5)
