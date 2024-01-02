from epicevents.utils.bases.menus import BaseMenu
from epicevents.utils.bases.views import BaseView
from epicevents.utils.contants import CONFIRMATION_MENU

epic_events = "EPIC EVENTS"


class ReceptionView(BaseView):
    def welcome(self):
        self.clean_console()
        welcome = f" Welcome on {epic_events} "
        self._display_centered_title(welcome)

    def follow_instructions(self):
        instructions = "Follow the instructions below"
        self._display_centered_title(instructions, stars=False)


class HomeView(BaseMenu):
    home_menu: dict = {
        "1": "Employee",
        "2": "Client",
        "3": "Event",
        "4": "Contract",
        "5": "Role",
        "6": "Exit",
    }

    def choice_menu(self):
        self._display_menu("Home menu", menu_dict=self.home_menu)
        return self._response_menu(menu_dict=self.home_menu)


class ExitView(BaseMenu):
    def exit_program(self):
        exiting = f" EXIT {epic_events} "
        self._display_centered_title(title=exiting, stars=False)

    def good_by(self):
        phrase = "Good day and see you soon..."
        self._display_centered_title(title=phrase, stars=False)

    def choice_menu(self):
        self._display_menu("Confirm exiting", menu_dict=CONFIRMATION_MENU)
        return self._response_menu(menu_dict=CONFIRMATION_MENU)
