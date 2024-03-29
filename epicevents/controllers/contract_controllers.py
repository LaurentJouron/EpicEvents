from ..utils.bases.controllers import BaseController
from ..utils.contants import GESTION, SUPPORT, ADMIN
from ..models import ContractManager
from ..models.employee import EmployeeManager
from ..views import ContractView
from ..controllers import home_controllers
from ..controllers.employee_controllers import (
    EmployeeLoginController,
    EmployeeController,
)
import sentry_sdk

from rich.table import Table
from rich.console import Console
from sqlalchemy.exc import IntegrityError


console = Console()
view = ContractView()
manager = ContractManager()


class ContractController(BaseController):
    """
    Controls the flow of contract-related operations.

    Provides methods to create, read, update, and delete contract records.
    Also handles the navigation between different contract-related controllers.
    """

    def run(self):
        """
        Runs the contract controller.

        Displays a menu to the user and returns the corresponding controller
        based on the user's choice.

        Returns:
            The corresponding controller instance based on the user's choice
        """
        employee_controllers = EmployeeController()
        department = employee_controllers.get_user_login_department()
        while True:
            choice = view.menu_choice()
            if choice == "1":
                if department == GESTION:
                    return ContractCreateController()
                view.error_not_have_right()
                return ContractController()

            elif choice == "2":
                return ContractReadController()

            elif choice == "3":
                if department != SUPPORT:
                    return ContractUpdateController()
                view.error_not_have_right()
                return ContractController()

            elif choice == "4":
                if department == ADMIN:
                    return ContractDeleteController()
                view.error_not_have_right()
                return ContractController()

            elif choice == "5":
                return home_controllers.HomeController()

    def get_data(self):
        """
        Retrieves contract data from the user.

        Returns:
            dict: A dictionary containing the contract data.
        """
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

    def get_table(self, contracts):
        """
        Displays a table of contracts.

        Args:
            contracts (List[Contracts]): A list of contract objects to display.
        """
        table = Table(
            title="Contract", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("Name", style="bold")
        table.add_column("Total amount", style="bold")
        table.add_column("Pending amount", style="bold")
        table.add_column("Creation date", style="bold")
        table.add_column("Status", style="bold")
        table.add_column("Gestion", style="bold")
        for contract in contracts:
            manager_employee = EmployeeManager()
            employee = manager_employee.get_by_id(
                employee_id=contract.employee_id
            )
            table.add_row(
                str(contract.id),
                contract.name,
                contract.total_amount,
                contract.pending_amount,
                str(contract.creation_date),
                str(contract.status),
                f"{employee.username} {employee.last_name}",
            )
        console.print(table)


class ContractCreateController(ContractController):
    """
    Controls the flow of creating a contract.

    Prompts the user to enter contract information.
    Creates the contract using the manager.

    Returns:
        The ContractController instance
    """

    def run(self):
        """
        Runs the contract create controller.

        Prompts the user to enter contract information.
        Creates the contract using the manager.

        Returns:
            The ContractController instance
        """
        view.display_title("Create contract")
        data = self.get_data()

        try:
            manager.create(**data)
            view.success_creating()
            return ContractController()

        except IntegrityError as e:
            sentry_sdk.capture_exception(e)
            return ContractController()

        except Exception as e:
            sentry_sdk.capture_exception(e)
            raise

        finally:
            return ContractController()


class ContractReadController(ContractController):
    """
    Controls the flow of reading contracts.

    Retrieves contract records from the manager and displays them in a table.

    Returns:
        The ContractController instance
    """

    def run(self):
        """
        Runs the contract update controller.

        Retrieves contract records from the manager and displays them in a
        table.
        Prompts the user to select a contract ID to update.
        Updates the contract information based on the selected ID.

        Returns:
            The ContractController instance
        """
        while True:
            contracts = manager.read()
            self.get_table(contracts=contracts)
            continu = view.select_one_to_continue()
            if continu == "1":
                return ContractController()


class ContractUpdateController(ContractController):
    """
    Controls the flow of updating a contract.

    Retrieves contract records from the manager and displays them in a table.
    Prompts the user to select a contract ID to update.
    Updates the contract information based on the selected ID.

    Returns:
        The ContractController instance
    """

    def run(self):
        """
        Runs the contract update controller.

        Retrieves contract records from the manager and displays them in a
        table.
        Prompts the user to select a contract ID to update.
        Updates the contract information based on the selected ID.

        Returns:
            The ContractController instance
        """
        contracts = manager.read()
        self.get_table(contracts=contracts)
        contract_id = view.select_id()
        try:
            if manager.get_by_id(contract_id=contract_id):
                data = self.get_data()
                manager.update(contract_id=contract_id, **data)
                view.success_update()
                return ContractController()
            else:
                view.not_found()
        except Exception as e:
            sentry_sdk.capture_message(
                f"Unexpected error during client update: {e}"
            )
            sentry_sdk.capture_exception(e)
            view.not_found()
            raise
        finally:
            ContractController()


class ContractDeleteController(ContractController):
    """
    Controls the flow of deleting a contract.

    Retrieves contract records from the manager and displays them in a table.
    Prompts the user to select a contract ID to delete.
    Deletes the contract based on the selected ID.

    Returns:
        The ContractController instance
    """

    def run(self):
        """
        Runs the contract delete controller.

        Retrieves contract records from the manager and displays them in a
        table.
        Prompts the user to select a contract ID to delete.
        Deletes the contract based on the selected ID.

        Returns:
            The ContractController instance
        """
        contracts = manager.read()
        self.get_table(contracts=contracts)
        contract_id = view.select_id()
        if manager.delete(contract_id=contract_id):
            view.success_delete()
        else:
            view.not_found()
        return ContractController()
