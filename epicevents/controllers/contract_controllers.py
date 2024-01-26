from ..utils.bases.controllers import BaseController
from ..utils.contants import GESTION, SUPPORT, ADMIN
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
        employee_login = EmployeeLoginController()
        employee = employee_login.read_login_file()
        while True:
            choice = view.menu_choice()
            if choice == "1":
                # Création uniquement si department = Gestion
                if employee["department_id"] == GESTION:
                    return ContractCreateController()
                else:
                    view.error_not_have_right()
                    return ContractController()

            elif choice == "2":
                return ContractReadController()

            elif choice == "3":
                # Modification posswible uniquement si différent de Support
                if employee["department_id"] != SUPPORT:
                    return ContractUpdateController()
                else:
                    view.error_not_have_right()
                    return ContractController()

            elif choice == "4":
                # Suppression uniquement si department = Admin
                if employee["department_id"] == ADMIN:
                    return ContractDeleteController()
                else:
                    view.error_not_have_right()
                    return ContractController()

            elif choice == "5":
                return home_controllers.HomeController()

    def get_data(self):
        name = view.get_name()
        total_amount = view.get_amount("total")
        pending_amount = view.get_amount("pending")
        status = True
        employee = EmployeeLoginController()
        employee_id = employee.login_file()
        return {
            "name": name,
            "total_amount": total_amount,
            "pending_amount": pending_amount,
            "status": status,
            "employee_id": employee_id,
        }


class ContractCreateController(ContractController):
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


class ContractReadController(ContractController):
    def run(self):
        contracts = manager.read()
        view.display_table(contracts=contracts)
        return ContractController()


class ContractUpdateController(ContractController):
    def run(self):
        contracts = manager.read()
        view.display_table(contracts=contracts)
        contract_id = view.select_id()
        try:
            name = manager.get_by_id(contract_id=contract_id)

            # Droits à rajouter sur commercial et gestion
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


class ContractDeleteController(ContractController):
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
