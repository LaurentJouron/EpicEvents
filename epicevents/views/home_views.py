from epicevents.utils.bases.menus import BaseMenu
from epicevents.utils.bases.views import BaseView


class ReceptionView(BaseView):
    def welcome(self):
        self.clean_console()
        welcome = " Welcome on EPIC EVENTS "
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

    def display_menu(self):
        self._display_menu("Home menu", menu_dict=self.home_menu)
        return self._response_menu(menu_dict=self.home_menu)


class ExitView(BaseView):
    def exit_program(self):
        exiting = " EXIT EPIC EVENTS "
        self._display_centered_title(exiting, stars=False)

    def good_by(self):
        self._space_presentation("Good day and see you soon...")
