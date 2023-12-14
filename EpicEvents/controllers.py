from utils.bases.controllers import BaseController
from utils.contants import CONFIRMATION_MENU

from .views import HomeView, AuthenticationView, ExitView

exit_view = ExitView()
auth_view = AuthenticationView()
home_view = HomeView()


class AuthenticationController(BaseController):
    def run(self):
        auth_view.welcome()
        auth_view.follow_instructions()
        while True:
            choice = auth_view.display_menu(auth_view.authentication_menu)
            if choice == "1":
                return ...

            elif choice == "2":
                return ...

            elif choice == "3":
                return ExitController()


class HomeController(BaseController):
    def run(self):
        while True:
            choice = home_view.display_menu(home_view.home_menu)
            if choice == "1":
                return ...

            elif choice == "2":
                return ...

            elif choice == "3":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        exit_view.exit_program()
        choice = home_view.display_menu(CONFIRMATION_MENU)
        if choice == "1":
            return None
        else:
            return HomeController()
