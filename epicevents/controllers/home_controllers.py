from ..utils.bases.controllers import BaseController
from ..utils.contants import ADMIN
from ..views import HomeView, ReceptionView, ExitView
from ..controllers.department_controllers import DepartmentController
from ..controllers.client_controllers import ClientController
from ..controllers.event_controllers import EventController
from ..controllers.contract_controllers import ContractController
from ..controllers.employee_controllers import (
    EmployeeController,
    EmployeeLoginController,
    EmployeeLogoutController,
)

view = HomeView()


class ReceptionController(BaseController):
    """
    Represents the reception controller of the application.

    Controls the flow of the reception view.
    Displays a welcome message and instructions to the user.
    Returns the EmployeeLoginController to handle employee login.

    Args:
        self

    Returns:
        The EmployeeLoginController instance
    """

    def run(self):
        reception_view = ReceptionView()
        reception_view.welcome()
        reception_view.follow_instructions()
        return EmployeeLoginController()


class HomeController(BaseController):
    """
    Represents the home controller of the application.

    Controls the flow of the home view.
    Displays the home menu and handles user choices.
    Returns the corresponding controller based on the user's choice.

    Args:
        self

    Returns:
        The corresponding controller instance based on the user's choice
    """

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
                employee_controllers = EmployeeController()
                department = employee_controllers.get_user_login_department()
                if department == ADMIN:
                    return DepartmentController()
                view.error_not_have_right()
                return HomeController()

            elif choice == "6":
                return ExitController()


class ExitController(BaseController):
    """
    Represents the exit controller of the application.

    Controls the flow of the exit view.
    Displays an exit message and handles user choices.
    Returns the HomeController or None based on the user's choice.

    Args:
        self

    Returns:
        The HomeController instance or None
    """

    def run(self):
        exit_view = ExitView()
        exit_view.exit_program()
        choice = exit_view.choice_menu()

        if choice != "1":
            return HomeController()
        logout = EmployeeLogoutController()
        logout.run()
        return None
