from epicevents.utils.bases.controllers import BaseController
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
        ...


class UpdateClientController(BaseController):
    def run(self):
        ...


class GetClientByIdController(BaseController):
    def run(self):
        ...


class GetClientByNameController(BaseController):
    def run(self):
        ...


class DeleteClientController(BaseController):
    def run(self):
        ...


class GetAllClientController(BaseController):
    def run(self):
        ...
