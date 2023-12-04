from controllers.person_controller import PersonController
from utils.bases.controllers import BaseController
from utils.contants import CONFIRMATION_MENU

from .views import HomeView

view = HomeView()


class HomeController(BaseController):
    def run(self):
        while True:
            choice = view.display_menu(view.home_menu)
            if choice == "1":
                return PersonController()

            elif choice == "2":
                return ...

            elif choice == "5":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        view.exit_game()
        choice = view.display_menu(CONFIRMATION_MENU)
        if choice == "1":
            return None
        else:
            return HomeController()
