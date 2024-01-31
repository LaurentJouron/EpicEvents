from ..models.employee import EmployeeManager
from ..utils.bases.controllers import BaseController
from ..utils.contants import COMMERCIAL, ADMIN
from ..models import ClientManager
from ..views import ClientView
from ..controllers.employee_controllers import (
    EmployeeLoginController,
    EmployeeController,
)
from ..controllers import home_controllers
import logging

from rich.table import Table
from rich.console import Console
from sqlalchemy.exc import IntegrityError


view = ClientView()
manager = ClientManager()
console = Console()


class ClientController(BaseController):
    def run(self):
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
    def run(self):
        data = self.get_data()
        try:
            manager.create(**data)
            view.success_creating()
            return ClientController()

        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            return ClientController()

        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            raise

        finally:
            ClientController()


class ClientReadController(ClientController):
    def run(self):
        while True:
            clients = manager.read()
            self.get_table(clients=clients)
            continu = view.select_one_to_continue()
            if continu == "1":
                return ClientController()


class ClientUpdateController(ClientController):
    def run(self):
        clients = manager.read()
        view.display_table(clients)
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
            logging.exception(f"Unexpected error during client update: {e}")
            view.error_not_found()
            raise
        finally:
            return ClientController()


class ClientDeleteController(ClientController):
    def run(self):
        clients = manager.read()
        view.display_table(clients=clients)

        client_id = view.select_id()
        if manager.delete(client_id=client_id):
            view.success_delete()
        else:
            view.error_not_found()
        return ClientController()
