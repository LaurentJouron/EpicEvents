from ..utils.bases.controllers import BaseController
from ..models import ContractManager
from ..views import ContractView
from ..controllers.employee_controllers import EmployeeLoginController
from ..controllers import home_controllers
import logging

from sqlalchemy.exc import IntegrityError

view = ContractView()
manager = ContractManager()


class ContractController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                return ContractCreateController()
            elif choice == "2":
                return ContractReadController()
            elif choice == "3":
                return ContractUpdateController()
            elif choice == "4":
                return ContractDeleteController()
            elif choice == "5":
                return home_controllers.HomeController()


class ContractCreateController(BaseController):
    def run(self):
        view.display_title("Create contract")
        data = self.get_data()
        try:
            manager.create(**data)
            view.success_creating()
            return ContractController()
        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            return ContractController()
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            raise
        finally:
            ContractController()

    def get_data(self):
        name = view.get_name()
        total_amount = view.get_amount("total")
        outstanding_amount = view.get_amount("outstanding")
        status = True
        employee = EmployeeLoginController()
        gestion_id = employee.login_file()
        return {
            "name": name,
            "total_amount": total_amount,
            "outstanding_amount": outstanding_amount,
            "status": status,
            "gestion_id": gestion_id,
            # "event_id": event_id,
        }


class ContractUpdateController(ContractCreateController):
    def run(self):
        contracts = manager.read()
        view.display_table(contracts=contracts)
        contract_id = view.select_id()
        try:
            name = manager.get_by_id(contract_id=contract_id)
            if name:
                data = self.get_data()
                manager.update(contract_id=contract_id, **data)
                view.success_update()
                return ContractController()
            else:
                view.not_found()
        except Exception as e:
            logging.exception(f"Unexpected error during contract update: {e}")
            view.not_found()
            raise
        finally:
            ContractController()


class ContractDeleteController(BaseController):
    def run(self):
        contracts = manager.read()
        view.display_table(contracts=contracts)

        contract_id = view.select_id()
        deleted = manager.delete(contract_id=contract_id)
        if deleted:
            view.success_delete()
        else:
            view.not_found()
        return ContractController()


class ContractReadController(BaseController):
    def run(self):
        contracts = manager.read()
        view.display_table(contracts=contracts)
        return ContractController()
