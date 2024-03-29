from ..utils.bases.controllers import BaseController
from ..models import DepartmentManager
from ..views import DepartmentView
from ..controllers import home_controllers
import sentry_sdk

from sqlalchemy.exc import IntegrityError
from rich.table import Table
from rich.console import Console

console = Console()
view = DepartmentView()
manager = DepartmentManager()


class DepartmentController(BaseController):
    """
    Represents the department controller of the application.

    Controls the flow of department-related operations.
    Displays a menu to the user and returns the corresponding controller based
    on the user's choice.

    Returns:
        The corresponding controller instance based on the user's choice
    """

    def run(self):
        """
        Runs the department controller.

        Displays a menu to the user and returns the corresponding controller
        based on the user's choice.

        Returns:
            The corresponding controller instance based on the user's choice
        """
        while True:
            choice = view.choice_menu()
            if choice == "1":
                return DepartmentCreateController()

            elif choice == "2":
                return DepartmentReadController()

            elif choice == "3":
                return DepartmentUpdateController()

            elif choice == "4":
                return DepartmentDeleteController()

            elif choice == "5":
                return home_controllers.HomeController()

    def get_department_id(self):
        departments = manager.read()
        view.display_table(departments)
        return view.select_id()

    def get_table(self, departments):
        """
        Displays a table of departments.

        Args:
            departments (List[Department]): A list of department objects to
            display.
        """
        table = Table(
            title="Departments", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("Name", style="bold")
        for department in departments:
            table.add_row(str(department.id), department.name)
        console.print(table)


class DepartmentCreateController(DepartmentController):
    """
    Represents the department create controller of the application.

    Controls the flow of creating a department.
    Prompts the user to enter the department name.
    Creates the department using the manager.
    Returns the DepartmentController instance.

    Returns:
        The DepartmentController instance
    """

    def run(self):
        """
        Runs the department create controller.

        Prompts the user to enter the department name.
        Creates the department using the manager.
        Returns the DepartmentController instance.

        Returns:
            The DepartmentController instance
        """
        name = view.get_name()
        try:
            manager.create(name=name)
            view.success_creating()
            return DepartmentController()

        except IntegrityError as e:
            sentry_sdk.capture_message(f"IntegrityError: {e}")
            sentry_sdk.capture_exception(e)
            return DepartmentController()

        except Exception as e:
            sentry_sdk.capture_exception(e)
            sentry_sdk.capture_message(f"Unexpected error: {e}")
            raise

        finally:
            DepartmentController()


class DepartmentReadController(DepartmentController):
    """
    Represents the department read controller of the application.

    Controls the flow of reading departments.
    Reads the departments from the manager and displays them in a table.
    Returns the DepartmentController instance.

    Returns:
        The DepartmentController instance
    """

    def run(self):
        """
        Runs the department read controller.

        Reads the departments from the manager and displays them in a table.
        Returns the DepartmentController instance.

        Returns:
            The DepartmentController instance
        """
        while True:
            departments = manager.read()
            self.get_table(departments=departments)
            continu = view.select_one_to_continue()
            if continu == "1":
                return DepartmentController()


class DepartmentUpdateController(DepartmentController):
    def run(self):
        """
        Runs the department controller.

        Reads the departments from the manager and displays them in a table.
        Prompts the user to select a department ID.
        Updates the department name based on the selected ID.
        Returns the DepartmentController instance.

        Returns:
            The DepartmentController instance
        """
        department_id = self.get_department_id()
        try:
            if manager.get_by_id(department_id=department_id):
                new_name = view.get_name()
                manager.update(department_id=department_id, new_name=new_name)
                view.success_update()
            else:
                view.error_not_found()

        except Exception as e:
            sentry_sdk.capture_message(
                f"Unexpected error during role update: {e}"
            )
            sentry_sdk.capture_exception(e)
        finally:
            return DepartmentController()


class DepartmentDeleteController(DepartmentController):
    """
    Represents the department delete controller of the application.

    Controls the flow of deleting a department.
    Displays the list of departments and prompts the user to select a
    department ID to delete.
    Deletes the department based on the selected ID and returns the
    DepartmentController instance.

    Returns:
        The DepartmentController instance
    """

    def run(self):
        """
        Runs the department delete controller.

        Reads the departments from the manager and displays them in a table.
        Prompts the user to select a department ID to delete.
        Deletes the department based on the selected ID.
        Returns the DepartmentController instance.

        Returns:
            The DepartmentController instance
        """
        department_id = self.get_department_id()
        if manager.delete(department_id=department_id):
            view.success_delete()
        else:
            view.error_not_found()
        return DepartmentController()
