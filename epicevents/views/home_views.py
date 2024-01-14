from ..utils.bases.views import BaseView
from ..utils.contants import CONFIRMATION_MENU

epic_events = "EPIC EVENTS"


class ReceptionView(BaseView):
    def welcome(self):
        self._clean_console()
        welcome = f" Welcome on {epic_events} "
        self._display_centered_title(welcome)

    def follow_instructions(self):
        instructions = "\nFollow the instructions below"
        self._display_centered_title(instructions, stars=False)

    def clean_console(self):
        self._clean_console()


class HomeView(BaseView):
    home_menu: dict = {
        "1": "Employee",
        "2": "Client",
        "3": "Event",
        "4": "Contract",
        "5": "Role",
        "6": "Exit",
    }

    def choice_menu(self):
        return self._choice_menu("Home menu", menu_dict=self.home_menu)

    def clean_console(self):
        self._clean_console()


class ExitView(BaseView):
    def exit_program(self):
        exiting = f" EXIT {epic_events} "
        self._display_centered_title(title=exiting, stars=False)

    def good_by(self):
        phrase = "Good day and see you soon..."
        self._display_centered_title(title=phrase, stars=False)

    def choice_menu(self):
        self._display_menu("Confirm exiting", menu_dict=CONFIRMATION_MENU)
        return self._response_menu(menu_dict=CONFIRMATION_MENU)

    def clean_console(self):
        self._clean_console()
