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

employee_login = EmployeeLoginController()
employee = employee_login.read_login_file()


class ClientController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                # Création uniquement si rôle = Commercial
                if employee["role_id"] == COMMERCIAL:
                    return ClientCreateController()
                else:
                    view.error_not_have_right()
                    return ClientController()

            elif choice == "2":
                return ClientReadController()

            elif choice == "3":
                # Modification uniquement si rôle = Commercial
                if employee["role_id"] == COMMERCIAL:
                    return ClientUpdateController()
                else:
                    view.error_not_have_right()
                    return ClientController()

            elif choice == "4":
                # Suppression impossible
                if employee["role_id"] == ADMIN:
                    return ClientDeleteController()
                else:
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
            return ClientController()

        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
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
            commercial = manager.get_commercial_by_id(client_id)
            if commercial:
                # Modification uniquement si le commercial a créé le client
                if employee["employee_id"] == commercial:
                    data = self.get_data()
                    manager.update(client_id, **data)
                    view.success_update()
                    return ClientController()
                else:
                    view.error_not_have_right()
                    return ClientController()
            else:
                view.error_not_found()
                return ClientController()

        except Exception as e:
            logging.exception(f"Unexpected error during client update: {e}")
            view.error_not_found()
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
            view.error_not_found()
        return ClientController()
