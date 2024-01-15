import logging
import time

from sqlalchemy.exc import IntegrityError

from ..utils.contants import SHORT_SLEEP
from ..utils.bases.controllers import BaseController
from ..models import ClientManager
from ..views import ClientView
from ..controllers import home_controllers

view = ClientView()
manager = ClientManager()


class ClientController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                view.clean_console()
                return ClientCreationController()

            elif choice == "2":
                return ClientUpdateController()

            elif choice == "3":
                return ClientDeleteController()

            elif choice == "4":
                view.clean_console()
                return ClientDisplayAllController()

            elif choice == "5":
                return home_controllers.HomeController()


class ClientCreationController(BaseController):
    def run(self):
        client_data = view.get_client_data()
        try:
            manager.create_client(**client_data)
            view.success_creating()
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            return ClientController()
        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            view.exist_error(client_data)
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


class ClientUpdateController(BaseController):
    def run(self):
        clients = manager.get_all_client()
        view.display_client_table(clients)
        client_id = view.get_id()
        try:
            client_name = manager.get_client_compagny_name_by_id(client_id)
            if client_name:
                client_data = view.get_client_data()
                manager.update_client(client_id, **client_data)
                view.success_update()
                return ClientController()
            else:
                view.not_found()
        except Exception as e:
            logging.exception(f"Unexpected error during client update: {e}")
            view.message_error(str(e))
            raise
        finally:
            ClientController()


class ClientDeleteController(BaseController):
    def run(self):
        client_id = view.get_id()
        deleted = manager.delete_client(client_id=client_id)
        if deleted:
            view.success_delete()
        else:
            view.not_found()
        time.sleep(SHORT_SLEEP)
        view.clean_console()
        return ClientController()


class ClientDisplayAllController(BaseController):
    def run(self):
        clients = manager.get_all_client()
        view.display_client_table(clients=clients)
        return ClientController()
