import pyautogui as pag
import keyboard as kb
import pyperclip
import re
import constants
import platform_credentials
from time import sleep, time
from typing import Tuple, Dict


def copy_text_and_return_as_variable(location_left: Tuple[int,int], location_right: Tuple[int,int,]):
    pag.moveTo(location_left)
    pag.mouseDown()
    pag.moveTo(location_right)
    pag.mouseUp()
    pag.hotkey("ctrl", "c")

    copied_text = pyperclip.paste()

    return copied_text.encode('utf-8').decode('utf-8').replace("\n", "").replace("\r", "").replace("\t", "")


def get_tournament_data() -> Dict:
    def get_tournament_location() -> Dict[str, str]:
        pag.scroll(-10000) # get to bottom of the page
        sleep(0.5)
        pag.scroll(constants.TOURNAMENT_INFO_OFFSET)
        sleep(0.5)
        pag.click(constants.COURT_FACILITY_BUTTON)
        sleep(1)
        tournament_plz = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_PLZ, constants.RIGHT_TOURNAMENT_PLZ)
        tournament_street = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_STREET, constants.RIGHT_TOURNAMENT_STREET)

        return {"tournament_plz": tournament_plz, "tournament_street": tournament_street}


    def get_tournament_dates():
        registration_start_existing = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_START_EXISTING, constants.RIGHT_TOURNAMENT_REGISTRATION_START_EXISTING)
        if registration_start_existing == "Meldeschluss":
            tournament_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DATE, constants.RIGHT_TOURNAMENT_DATE)
            tournament_registration_start = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_START_RSP, constants.RIGHT_TOURNAMENT_REGISTRATION_START_RSP)
            tournament_registration_end = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_END_RSP, constants.RIGHT_TOURNAMENT_REGISTRATION_END_RSP)
            tournament_draw_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DRAW_DATE_RSP, constants.RIGHT_TOURNAMENT_DRAW_DATE_RSP)
            return {"tournament_date": tournament_date, "tournament_registration_start": tournament_registration_start,"tournament_registration_end": tournament_registration_end, "tournament_draw_date": tournament_draw_date}
        else:
            tournament_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DATE, constants.RIGHT_TOURNAMENT_DATE)
            tournament_registration_end = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_REGISTRATION_END, constants.RIGHT_TOURNAMENT_REGISTRATION_END)
            tournament_draw_date = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_DRAW_DATE, constants.RIGHT_TOURNAMENT_DRAW_DATE)

            return {"tournament_date": tournament_date, "tournament_registration_start": "Nicht angegeben","tournament_registration_end": tournament_registration_end, "tournament_draw_date": tournament_draw_date}


    def get_tournament_title() -> Dict[str, str]:
        tournament_title = copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_TITLE, constants.RIGHT_TOURNAMENT_TITLE)
        return {"tournament_title": tournament_title}


    def get_tournament_link() -> Dict[str, str]:
        pag.moveTo(constants.TOURNAMENT_LINK)
        pag.click()
        pag.hotkey("ctrl", "c")
        return {"tournament_link": str(pyperclip.paste())}


    def scroll_to_top_of_page():
        kb.press_and_release("home")
        sleep(0.5)

    
    def execute_fail_safe():
        pag.scroll(-100)
        sleep(1)
        kb.press_and_release("home")
        sleep(1.5)


    for _ in range(5):
        pag.hotkey("ctrl", "-")

    scroll_to_top_of_page()
    execute_fail_safe()

    return get_tournament_title() | get_tournament_dates() | get_tournament_location() | get_tournament_link()

all_tournaments_with_data = {
    "M18": [],
    "M16": [],
    "M14": [],
    "M13": [],
    "M12": [],
    "M11": [],

    "W18": [],
    "W16": [],
    "W14": [],
    "W13": [],
    "W12": [],
    "W11": []
}

def scroll_through_tournaments():
    def execute_fail_safe():
        pag.scroll(-100)
        sleep(1)
        kb.press_and_release("home")
        sleep(1.5)


    def reset_zoom():
        pag.hotkey("ctrl", "0")
        pag.hotkey("ctrl", "-")


    def scroll_to_top_of_page():
        pag.click(constants.LEFT_SCREEN_EDGE)
        sleep(0.5)
        kb.press_and_release("home")


    def print_scrolling_progress():
        print(f"Progess: {round((tournament_number / tournament_amount) * 100)}%")
        print(f"Scrolled through {tournament_number} tournaments.")
        print(f"{tournament_amount - tournament_number} left.")
        print(f"Elapsed time: {round((time() - start_time) / 60, 2)} minutes")
        print()


    start_time = time()
    reset_zoom()
    sleep(1)
    pag.click(constants.AGE_CLASS_BUTTON)
    sleep(1)
    pag.click(constants.RESET_SEARCH_OPTIONS_BUTTON)
    kb.press_and_release("home")
    sleep(constants.SLEEP_TIME_FOR_LOADING)

    age_classes_list = list(constants.AGE_CLASSES)
    for age_class_index in range(len(age_classes_list)): 
        # pick an age class
        pag.click(constants.AGE_CLASS_BUTTON)
        sleep(0.5)
        pag.moveTo(constants.AGE_CLASSES_SELECTOR)
        sleep(0.5)
        pag.scroll(-500)
        sleep(0.5)
        pag.click(constants.AGE_CLASSES[age_classes_list[age_class_index]])
        sleep(0.5)
        if age_class_index > 0:
            pag.click(constants.AGE_CLASSES[age_classes_list[age_class_index - 1]])
            sleep(0.5)

        pag.click(constants.SEARCH_TOURNAMENTS_BUTTON)
        sleep(3)
        tournament_amount = int(re.sub(r'\D', '', copy_text_and_return_as_variable(constants.LEFT_TOURNAMENT_AMOUNT, constants.RIGHT_TOURNAMENT_AMOUNT))) # only get the numbers out of the string

        amount_show_more_tournaments_button = round(tournament_amount / 10)

        if tournament_amount == 0:
            continue
        else:
            if tournament_amount > 10:
                pag.click(constants.MAP_VIEW_BUTTON)
                sleep(0.5)
                pag.press("tab", presses=23)
                pag.press("enter")
                for _ in range(amount_show_more_tournaments_button):
                    pag.press("enter")
                    sleep(0.5)

            for tournament_number in range(1, tournament_amount + 1):
                reset_zoom()
                sleep(0.5)
                scroll_to_top_of_page()
                sleep(1)
                execute_fail_safe()
                pag.click(constants.MAP_VIEW_BUTTON)
                sleep(0.5)
                pag.press("tab", presses=tournament_number*2+2)
                sleep(1)
                pag.press("enter")
                sleep(constants.SLEEP_TIME_FOR_LOADING)
                all_tournaments_with_data[age_classes_list[age_class_index]].append(get_tournament_data())
                sleep(0.5)
                pag.click(constants.PAGE_BACK_BUTTON)
                sleep(constants.SLEEP_TIME_FOR_LOADING)

                print_scrolling_progress()

            reset_zoom()
            sleep(2)
            scroll_to_top_of_page()
            sleep(0.5)
            execute_fail_safe()

    pag.hotkey("ctrl", "w")


def open_chrome_browser():
    pag.press("super")
    sleep(0.5)
    kb.write("chrome")
    sleep(0.5)
    pag.press("enter")


def open_tournament_platform():
    open_chrome_browser()
    sleep(constants.SLEEP_TIME_FOR_LOADING)
    pyperclip.copy("https://www.tennis.de/spielen/turniersuche.html#search")
    pag.hotkey("ctrl", "v")
    pag.press("enter")
    sleep(constants.SLEEP_TIME_FOR_LOADING + 3)


def log_out_of_the_platform():
    open_tournament_platform()
    pag.click(constants.ACCOUNT_BUTTON)
    sleep(2)
    pag.click(constants.LOG_OUT_BUTTON)
    sleep(4)

    pag.hotkey("ctrl", "w")


def log_into_the_platform():
    open_tournament_platform()
    pyperclip.copy("https://www.tennis.de/spielen/turniersuche.html#search")
    pag.hotkey("ctrl", "v")
    pag.press("enter")
    sleep(constants.SLEEP_TIME_FOR_LOADING + 3)

    pag.click(constants.ACCOUNT_BUTTON)
    sleep(constants.SLEEP_TIME_FOR_LOADING)
    pag.click(constants.ACCOUNT_BUTTON)
    sleep(constants.SLEEP_TIME_FOR_LOADING + 2)

    pag.click(constants.EMAIL_INPUT_FIELD)
    sleep(1.1)
    pyperclip.copy(platform_credentials.E_MAIL)
    pag.hotkey("ctrl", "v")
    pag.press("esc")
    sleep(1.1)
    pag.click(constants.PASSWORD_INPUT_FIELD)
    pag.press("esc")
    sleep(1.1)
    pyperclip.copy(platform_credentials.PASSWORD)
    pag.hotkey("ctrl", "v")
    sleep(1.1)
    pag.click(constants.LOGIN_BUTTON)
    sleep(5)

    pag.hotkey("ctrl", "w")


def return_tournaments_with_data():
    log_into_the_platform()
    open_tournament_platform()
    scroll_through_tournaments()
    log_out_of_the_platform()
    return all_tournaments_with_data


def main():
    while True:
        if kb.is_pressed("a"):
            tournament_data = get_tournament_data()
            print(tournament_data)
            sleep(0.5)       
        elif kb.is_pressed("b"):
            open_tournament_platform()
            scroll_through_tournaments()
            sleep(0.5)

