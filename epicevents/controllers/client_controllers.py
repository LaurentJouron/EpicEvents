from ..utils.contants import SHORT_SLEEP
from ..utils.bases.controllers import BaseController
from ..models import ClientManager
from ..views import ClientView
from ..controllers.employee_controllers import EmployeeLoginController
from ..controllers import home_controllers
import logging
import time

from sqlalchemy.exc import IntegrityError

view = ClientView()
manager = ClientManager()


class ClientController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                view.clean_console()
                return ClientCreateController()
            elif choice == "4":
                view.clean_console()
                return ClientReadController()
            elif choice == "2":
                return ClientUpdateController()
            elif choice == "3":
                return ClientDeleteController()
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
        commercial_id = employee.login_file()
        return {
            "compagny_name": compagny_name,
            "username": username,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "address": address,
            "information": information,
            "commercial_id": commercial_id,
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
            view.exist_error(data)
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            return ClientController()
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            raise
        finally:
            ClientController()


class ClientReadController(ClientController):
    def run(self):
        clients = manager.read()
        view.display_table(clients=clients)
        return ClientController()


class ClientUpdateController(ClientController):
    def run(self):
        clients = manager.read()
        view.display_table(clients)
        client_id = view.select_id()
        try:
            name = manager.get_compagny_name_by_id(client_id)
            if name:
                data = self.get_data()
                manager.update(client_id, **data)
                view.success_update()
                return ClientController()
            else:
                view.not_found()
        except Exception as e:
            logging.exception(f"Unexpected error during client update: {e}")
            view.not_found()
            raise
        finally:
            ClientController()


class ClientDeleteController(ClientController):
    def run(self):
        clients = manager.read()
        view.display_table(clients=clients)

        client_id = view.select_id()
        deleted = manager.delete(client_id=client_id)
        if deleted:
            view.success_delete()
        else:
            view.not_found()
        return ClientController()
