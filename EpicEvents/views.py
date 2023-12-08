from utils.bases.menus import BaseMenu


class HomeView(BaseMenu):
    home_menu: dict = {
        "1": "Employee",
        "2": "Signup",
    }

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def welcome(self):
        self._space_presentation(" Welcome on << EPIC EVENTS>> ")

    def follow_instructions(self):
        self._space_presentation("Please follow the instructions below")

    def exit_program(self):
        self._space_presentation(" EXIT EPIC EVENTS ")

    def good_by(self):
        self._space_presentation("Good day and see you soon...\n")
