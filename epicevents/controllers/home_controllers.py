from epicevents.utils.bases.controllers import BaseController
from epicevents.utils.contants import CONFIRMATION_MENU

from ..views import HomeView, ReceptionView, ExitView

reception_view = ReceptionView()
exit_view = ExitView()
home_view = HomeView()


class ReceptionController(BaseController):
    def run(self):
        reception_view.welcome()
        reception_view.follow_instructions()
        while True:
            choice = home_view.display_menu(home_view.home_menu)
            if choice == "1":
                return ...  # Login

            elif choice == "2":
                return ...  # Signup

            elif choice == "3":
                return ExitController()  # Exit
        return ExitController()  # Exit


class HomeController(BaseController):
    def run(self):
        while True:
            choice = home_view.display_menu(home_view.home_menu)
            if choice == "1":
                return ...  # Client for commercial

            elif choice == "2":
                return ...  # Support for technician

            elif choice == "3":
                return ...  # Gestion for manager
            elif choice == "4":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        exit_view.exit_program()
        choice = home_view.display_menu(CONFIRMATION_MENU)
        if choice == "1":
            return None
        else:
            return HomeController()
