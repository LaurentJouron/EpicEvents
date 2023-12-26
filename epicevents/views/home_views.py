from epicevents.utils.bases.menus import BaseMenu
from epicevents.utils.bases.views import BaseView


class ReceptionView(BaseView):
    def welcome(self):
        welcome = " Welcome on << EPIC EVENTS >> "
        self._display_centered_title(welcome)

    def follow_instructions(self):
        instructions = "Follow the instructions below \n"
        self._display_centered_title(instructions, stars=False)


class HomeView(BaseMenu):
    home_menu: dict = {
        "1": "...",
        "2": "...",
        "3": "...",
    }


class ExitView(BaseView):
    def exit_program(self):
        self._display_centered_title(" EXIT EPIC EVENTS ")

    def good_by(self):
        self._space_presentation("Good day and see you soon...\n")
