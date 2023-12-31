import time

from ..utils.contants import SHORT_SLEEP, LONG_SLEEP
from ..utils.bases.controllers import BaseController
from ..views import HomeView, ReceptionView, ExitView
from ..controllers import (
    employee_controllers,
    role_controllers,
    client_controllers,
)

view = HomeView()
reception_view = ReceptionView()
exit_view = ExitView()


class ReceptionController(BaseController):
    def run(self):
        reception_view.welcome()
        time.sleep(LONG_SLEEP)
        reception_view.clean_console()
        reception_view.follow_instructions()
        time.sleep(SHORT_SLEEP)
        reception_view.clean_console()
        return employee_controllers.EmployeeLoginController()


class HomeController(BaseController):
    def run(self):
        while True:
            choice = view.choice_menu()
            if choice == "1":
                # Employee
                return employee_controllers.EmployeeController()
            elif choice == "2":
                # Client
                return client_controllers.ClientController()
            elif choice == "3":
                # Event
                view.clean_console()
                return ...
            elif choice == "4":
                # Contract
                view.clean_console()
                return ...
            elif choice == "5":
                # Role
                view.clean_console()
                return role_controllers.RoleController()
            elif choice == "6":
                view.clean_console()
                return ExitController()


class ExitController(BaseController):
    def run(self):
        exit_view.choice_menu()
        choice = exit_view.choice_menu()
        if choice == "1":
            return None
        else:
            view.clean_console()
            return HomeController()
