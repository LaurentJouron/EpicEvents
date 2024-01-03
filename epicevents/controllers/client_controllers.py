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
                return CreateClientController()

            elif choice == "2":
                return UpdateClientController()

            elif choice == "3":
                return GetClientByIdController()

            elif choice == "4":
                return GetClientByNameController()

            elif choice == "5":
                return DeleteClientController()

            elif choice == "6":
                return GetAllClientController()

            elif choice == "7":
                return home_controllers.HomeController()


class CreateClientController(BaseController):
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


class UpdateClientController(BaseController):
    def run(self):
        ...


class GetClientByIdController(BaseController):
    def run(self):
        all_client = GetAllClientController()
        all_client.run()
        client_id = view.get_id()
        client_name = manager.get_client_by_id(client_id)
        if client_name:
            view.client_information(client_name)
        else:
            view.invalid_id()
        return ClientController()


class GetClientByNameController(BaseController):
    def run(self):
        all_client = GetAllClientController()
        all_client.run()
        name = view.get_name()
        client = manager.get_client_by_compagny_name(name)
        if client:
            view.display_name(name)
        else:
            view.not_found(name)
        time.sleep(SHORT_SLEEP)
        view.clean_console()
        return ClientController()


class DeleteClientController(BaseController):
    def run(self):
        all_client = GetAllClientController()
        all_client.run()
        client_id = view.get_id()
        deleted = manager.delete_client(client_id)
        if deleted:
            view.success_delete()
        else:
            view.not_found()
        time.sleep(SHORT_SLEEP)
        view.clean_console()
        return ClientController()


class GetAllClientController(BaseController):
    def run(self):
        clients = manager.get_all_client()
        view.display_client_table(clients)
        return ClientController()
