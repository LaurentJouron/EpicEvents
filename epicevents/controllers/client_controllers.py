from ..utils.bases.controllers import BaseController
from ..utils.contants import COMMERCIAL, ADMIN
from ..models.employee import EmployeeManager
from ..models import ClientManager
from ..views import ClientView
from ..controllers import home_controllers
from ..controllers.employee_controllers import (
    EmployeeLoginController,
    EmployeeController,
)
import logging
import sentry_sdk

from rich.table import Table
from rich.console import Console
from sqlalchemy.exc import IntegrityError

view = ClientView()
manager = ClientManager()
console = Console()


class ClientController(BaseController):
    """
    Controls the flow of client-related operations.

    Provides methods to create, read, update, and delete client records.
    Also handles the navigation between different client-related controllers.

    Args:
        self

    """

    def run(self):
        """
        Runs the client controller.

        Displays a menu to the user and returns the corresponding controller
        based on the user's choice.

        Args:
            self

        Returns:
            The corresponding controller instance based on the user's choice
        """
        employee_controllers = EmployeeController()
        department = employee_controllers.get_user_login_department()
        while True:
            choice = view.menu_choice()
            if choice == "1":
                if department == COMMERCIAL:
                    return ClientCreateController()
                view.error_not_have_right()
                return ClientController()

            elif choice == "2":
                return ClientReadController()

            elif choice == "3":
                if department == COMMERCIAL:
                    return ClientUpdateController()
                view.error_not_have_right()
                return ClientController()

            elif choice == "4":
                if department == ADMIN:
                    return ClientDeleteController()
                view.error_not_have_right()
                return ClientController()

            elif choice == "5":
                return home_controllers.HomeController()

    def get_data(self):
        """
        Retrieves client data from the user.

        Returns:
            dict: A dictionary containing the client data.
        """
        view.display_title()
        compagny_name = view.get_compagny_name()
        username = view.get_username()
        last_name = view.get_lastname()
        email = view.get_email()
        phone = view.get_phone()
        address = view.get_address()
        information = view.get_information()
        employee = EmployeeLoginController()
        employee_id = employee.login_file()
        return {
            "compagny_name": compagny_name,
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "address": address,
            "information": information,
            "employee_id": employee_id,
        }

    def get_table(self, clients):
        """
        Displays a table of clients.

        Args:
            clients (List[Clients]): A list of client objects to display.

        Returns:
            None
        """
        table = Table(
            title="Client", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("Compagny", style="bold")
        table.add_column("Owner", style="bold")
        table.add_column("Email", style="bold")
        table.add_column("Phone", style="bold")
        table.add_column("Address", style="bold")
        table.add_column("Information", style="bold")
        table.add_column("Creation", style="bold")
        table.add_column("Update", style="bold")
        table.add_column("Sales", style="bold")
        for client in clients:
            manager_employee = EmployeeManager()
            employee = manager_employee.get_by_id(
                employee_id=client.employee_id
            )
            table.add_row(
                str(client.id),
                client.compagny_name,
                f"{client.username} {client.last_name}",
                client.email,
                client.phone,
                client.address,
                client.information,
                str(client.creation_date),
                str(client.updating_date),
                f"{employee.username} {employee.last_name}",
            )
        console.print(table)


class ClientCreateController(ClientController):
    """
    Controls the flow of creating a client.

    Prompts the user to enter client information.
    Creates the client using the manager.

    Args:
        self

    Returns:
        The ClientController instance
    """

    def run(self):
        """
        Runs the client create controller.

        Prompts the user to enter client information.
        Creates the client using the manager.

        Args:
            self

        Returns:
            The ClientController instance
        """
        data = self.get_data()
        try:
            manager.create(**data)
            view.success_creating()
            return ClientController()

        except IntegrityError as e:
            sentry_sdk.capture_message(f"IntegrityError: {e}")
            sentry_sdk.capture_exception(e)
            return ClientController()

        except Exception as e:
            sentry_sdk.capture_message(f"Unexpected error: {e}")
            sentry_sdk.capture_exception(e)
            raise

        finally:
            ClientController()


class ClientReadController(ClientController):
    """
    Controls the flow of reading clients.

    Retrieves all client records from the manager and displays them in a table.

    Args:
        self

    Returns:
        The ClientController instance
    """

    def run(self):
        """
        Runs the client read controller.

        Retrieves all client records from the manager and displays them in a
        table.

        Args:
            self

        Returns:
            The ClientController instance
        """
        while True:
            clients = manager.read()
            self.get_table(clients=clients)
            continu = view.select_one_to_continue()
            if continu == "1":
                return ClientController()


class ClientUpdateController(ClientController):
    """
    Controls the flow of updating a client.

    Retrieves client records from the manager and displays them in a table.
    Prompts the user to select a client ID to update.
    Updates the client information based on the selected ID.

    Args:
        self

    Returns:
        The ClientController instance
    """

    def run(self):
        """
        Runs the client update controller.

        Retrieves client records from the manager and displays them in a table.
        Prompts the user to select a client ID to update.
        Updates the client information based on the selected ID.

        Args:
            self

        Returns:
            The ClientController instance
        """
        clients = manager.read()
        self.get_table(clients)
        client_id = view.select_id()
        try:
            if client := manager.get_by_id(client_id=client_id):
                if commercial := client.employee_id:
                    employee_login = EmployeeLoginController()
                    employee = employee_login.read_login_file()
                    if employee["employee_id"] == commercial:
                        data = self.get_data()
                        manager.update(client_id, **data)
                        view.success_update()
                    else:
                        view.error_not_have_right()
                else:
                    view.error_not_found()
                return ClientController()
        except Exception as e:
            sentry_sdk.capture_message(
                f"Unexpected error during client update: {e}"
            )
            sentry_sdk.capture_exception(e)
            view.error_not_found()
            raise
        finally:
            return ClientController()


class ClientDeleteController(ClientController):
    """
    Controls the flow of deleting a client.

    Retrieves client records from the manager and displays them in a table.
    Prompts the user to select a client ID to delete.
    Deletes the client based on the selected ID.

    Args:
        self

    Returns:
        The ClientController instance
    """

    def run(self):
        """
        Runs the client delete controller.

        Retrieves client records from the manager and displays them in a table.
        Prompts the user to select a client ID to delete.
        Deletes the client based on the selected ID.

        Args:
            self

        Returns:
            The ClientController instance
        """
        clients = manager.read()
        self.get_table(clients=clients)

        client_id = view.select_id()
        if manager.delete(client_id=client_id):
            view.success_delete()
        else:
            view.error_not_found()
        return ClientController()
