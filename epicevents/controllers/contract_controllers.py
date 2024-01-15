from ..utils.bases.controllers import BaseController
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
                return ContractCreateController()

            elif choice == "2":
                return ContractUpdateController()

            elif choice == "3":
                return ContractDeleteController()

            elif choice == "4":
                return ContractDisplayAllController()

            elif choice == "5":
                return home_controllers.HomeController()


class ContractCreateController(BaseController):
    def run(self):
        ...


class ContractUpdateController(BaseController):
    def run(self):
        ...


class ContractDeleteController(BaseController):
    def run(self):
        ...


class ContractDisplayAllController(BaseController):
    def run(self):
        ...
