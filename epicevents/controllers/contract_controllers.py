from epicevents.utils.bases.controllers import BaseController
from ..models import ContractManager
from ..views import ContractView
from ..controllers import home_controllers

view = ContractView()
manager = ContractManager()


class ContractController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                return CreateContractController()

            elif choice == "2":
                return UpdateContractController()

            elif choice == "3":
                return GetContractByIdController()

            elif choice == "4":
                return GetContractByNameController()

            elif choice == "5":
                return DeleteContractController()

            elif choice == "6":
                return GetAllContractController()

            elif choice == "7":
                return home_controllers.HomeController()


class CreateContractController(BaseController):
    def run(self):
        ...


class UpdateContractController(BaseController):
    def run(self):
        ...


class GetContractByIdController(BaseController):
    def run(self):
        ...


class GetContractByNameController(BaseController):
    def run(self):
        ...


class DeleteContractController(BaseController):
    def run(self):
        ...


class GetAllContractController(BaseController):
    def run(self):
        ...
