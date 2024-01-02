from epicevents.utils.bases.controllers import BaseController
import time

from ..controllers import employee_controllers, role_controllers
from ..views import HomeView, ReceptionView, ExitView

view = HomeView()
reception_view = ReceptionView()
exit_view = ExitView()


class ReceptionController(BaseController):
    def run(self):
        reception_view.welcome()
        time.sleep(2)
        view.clean_console()
        reception_view.follow_instructions()
        time.sleep(1)
        view.clean_console()
        while True:
            choice = view.choice_menu()
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
        reception_view.welcome()
        time.sleep(2)
        view.clean_console()
        reception_view.follow_instructions()
        time.sleep(2)
        view.clean_console()
        while True:
            choice = view.choice_menu()
            if choice == "1":
                # Employee
                return employee_controllers.EmployeeController()
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
                return role_controllers.RoleController()
            elif choice == "6":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        exit_view.choice_menu()
        choice = exit_view.choice_menu()
        if choice == "1":
            return None
        else:
            return HomeController()
