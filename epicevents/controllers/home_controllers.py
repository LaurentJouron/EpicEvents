from ..utils.bases.controllers import BaseController
from ..views import HomeView, ReceptionView, ExitView
from ..controllers import (
    employee_controllers,
    role_controllers,
    client_controllers,
    event_controllers,
    contract_controllers,
)

view = HomeView()
reception_view = ReceptionView()
exit_view = ExitView()


class ReceptionController(BaseController):
    def run(self):
        reception_view.welcome()
        reception_view.follow_instructions()
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
                # Events
                return event_controllers.EventController()
                ...
            elif choice == "4":
                # Contracts
                return contract_controllers.ContractController()
                ...
            elif choice == "5":
                # Roles
                return role_controllers.RoleController()
            elif choice == "6":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        exit_view.exit_program()
        choice = exit_view.choice_menu()
        if choice == "1":
            employee_controllers.EmployeeLogoutController()
            return None
        else:
            return HomeController()
