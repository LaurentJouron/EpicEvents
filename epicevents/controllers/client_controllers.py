from ..utils.bases.controllers import BaseController
from ..utils.contants import COMMERCIAL, ADMIN
from ..models import ClientManager
from ..views import ClientView
from ..controllers.employee_controllers import EmployeeLoginController
from ..controllers import home_controllers
import logging

from sqlalchemy.exc import IntegrityError

view = ClientView()
manager = ClientManager()


class ClientController(BaseController):
    def run(self):
        employee_login = EmployeeLoginController()
        employee = employee_login.read_login_file()
        while True:
            choice = view.menu_choice()
            if choice == "1":
                if employee["department_id"] == COMMERCIAL:
                    return ClientCreateController()
                view.error_not_have_right()
                return ClientController()

            elif choice == "2":
                return ClientReadController()

            elif choice == "3":
                if employee["department_id"] == COMMERCIAL:
                    return ClientUpdateController()
                view.error_not_have_right()
                return ClientController()

            elif choice == "4":
                if employee["department_id"] == ADMIN:
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
            view.display_table(clients=clients)
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
