from ..utils.bases.controllers import BaseController
from ..views import HomeView, ReceptionView, ExitView
from ..controllers.role_controllers import RoleController
from ..controllers.client_controllers import ClientController
from ..controllers.event_controllers import EventController
from ..controllers.contract_controllers import ContractController
from ..controllers.employee_controllers import (
    EmployeeController,
    EmployeeLoginController,
    EmployeeLogoutController,
)


class ReceptionController(BaseController):
    def run(self):
        reception_view = ReceptionView()
        reception_view.welcome()
        reception_view.follow_instructions()
        return EmployeeLoginController()


class HomeController(BaseController):
    def run(self):
        while True:
            home_view = HomeView()
            choice = home_view.choice_menu()

            if choice == "1":
                return EmployeeController()

            elif choice == "2":
                return ClientController()

            elif choice == "3":
                return EventController()

            elif choice == "4":
                return ContractController()

            elif choice == "5":
                return RoleController()

            elif choice == "6":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        exit_view = ExitView()
        exit_view.exit_program()
        choice = exit_view.choice_menu()

        if choice == "1":
            logout = EmployeeLogoutController()
            logout.run()
            return None
        else:
            return HomeController()
