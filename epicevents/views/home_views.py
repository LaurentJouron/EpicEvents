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
        return self._choice_menu("Home menu", menu=self.home_menu)


class ExitView(BaseView):
    def exit_program(self):
        exiting = f" EXIT {epic_events} "
        self.console.print(exiting, style="bold blue", justify="center")

    def good_by(self):
        phrase = "Good day and see you soon..."
        self._display_centered_title(title=phrase, stars=False)

    def choice_menu(self):
        return self._choice_menu("Confirm exiting", menu=CONFIRMATION_MENU)
