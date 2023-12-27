from epicevents.views.utils.bases.controllers import BaseController
from epicevents.views.utils.contants import CONFIRMATION_MENU

from ..controllers import employee_controllers, role_controllers
from ..views import HomeView, ReceptionView, ExitView


class ReceptionController(BaseController):
    def run(self):
        reception_view = ReceptionView()
        home_view = HomeView()

        reception_view.welcome()
        reception_view.follow_instructions()

        while True:
            choice = home_view.display_menu()
            if choice == "1":
                # Login
                return ...
            elif choice == "2":
                # Signup
                return ...
            elif choice == "3":
                # Exit
                return ExitController()


class HomeController(BaseController):
    def run(self):
        home_view = HomeView()

        while True:
            choice = home_view.display_menu(home_view.home_menu)
            if choice == "1":
                # Employee
                return employee_controllers()
            elif choice == "2":
                # Client
                return ...
            elif choice == "3":
                # Event
                return ...
            elif choice == "4":
                # Contract
                return ...
            elif choice == "5":
                # Role
                return role_controllers()
            elif choice == "6":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        exit_view = ExitView()
        home_view = HomeView()

        exit_view.exit_program()
        choice = home_view.display_menu(CONFIRMATION_MENU)
        if choice == "1":
            return None
        else:
            return HomeController()
