from ..utils.bases.controllers import BaseController
from ..utils.contants import COMMERCIAL, ADMIN, GESTION, SUPPORT
from ..models.event import EventManager
from ..models.client import ClientManager
from ..models.employee import EmployeeManager
from ..models.contract import ContractManager
from ..views import EventView
from ..controllers import home_controllers
from ..controllers.employee_controllers import EmployeeController
from ..controllers.client_controllers import ClientController
from ..controllers.contract_controllers import ContractController
import logging
import sentry_sdk

from rich.table import Table
from rich.console import Console
from sqlalchemy.exc import IntegrityError

console = Console()
view = EventView()
manager = EventManager()


class EventController(BaseController):
    def run(self):
        employee_controllers = EmployeeController()
        department = employee_controllers.get_user_login_department()
        while True:
            choice = view.menu_choice()
            if choice == "1":
                if department == COMMERCIAL:
                    return EventCreateController()
                view.error_not_have_right()
                return EventController()

            elif choice == "2":
                return EventReadController()

            elif choice == "3":
                if department != COMMERCIAL:
                    return EventUpdateController()
                view.error_not_have_right()
                return EventController()

            elif choice == "4":
                if department == ADMIN:
                    return EventDeleteController()
                view.error_not_have_right()
                return EventController()

            elif choice == "5":
                return home_controllers.HomeController()

    def get_client(self):
        client_manager = ClientManager()
        client_controller = ClientController()
        clients = client_manager.read()
        client_controller.get_table(clients=clients)
        client_id = view.select_id()
        return client_manager.get_by_id(client_id=client_id)

    def get_employee(self):
        employee_manager = EmployeeManager()
        employee_controller = EmployeeController()
        employees = employee_manager.read()
        employee_controller.get_table(employees=employees)
        employee_id = view.select_id()
        return employee_manager.get_by_id(employee_id=employee_id)

    def get_contract(self):
        contract_manager = ContractManager()
        contract_controller = ContractController()
        contracts = contract_manager.read()
        contract_controller.get_table(contracts=contracts)
        contract_id = view.select_id()
        return contract_manager.get_by_id(contract_id=contract_id)

    def get_data(self):
        employee_controllers = EmployeeController()
        department_id = employee_controllers.get_user_login_department()
        employee_id = employee_controllers.get_user_id_login()
        contract = self.get_contract()
        client = self.get_client()
        if (
            department_id == COMMERCIAL
            and employee_id == client.employee_id
            and contract.status is True
        ):
            return self._extracted_data(contract, client)
        view.error_not_have_right()
        return EventController()

    def _extracted_data(self, contract, client):
        view.display_title("Create events")
        name = contract.name
        start_date, end_date = view.get_valid_date_range()
        address = client.address
        view.display_title("Attendees")
        attendees = view.get_number()
        notes = view.get_notes()
        client_id = client.id
        contract_id = contract.id
        employee_controllers = EmployeeController()
        employee_id = employee_controllers.get_user_id_login()
        return {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "address": address,
            "attendees": attendees,
            "notes": notes,
            "client_id": client_id,
            "contract_id": contract_id,
            "employee_id": employee_id,
        }

    def get_table(self, events):
        table = Table(
            title="Events", show_header=True, header_style="bold blue"
        )
        table.add_column("ID", style="dim")
        table.add_column("Name", style="bold")
        table.add_column("Start date", style="bold")
        table.add_column("End date", style="bold")
        table.add_column("Address", style="bold")
        table.add_column("Attendees", style="bold")
        table.add_column("Notes", style="bold")
        table.add_column("Client", style="bold")
        for event in events:
            manager_client = ClientManager()
            client = manager_client.get_by_id(client_id=event.client_id)
            table.add_row(
                str(event.id),
                event.name,
                str(event.start_date),
                str(event.end_date),
                event.address,
                str(event.attendees),
                event.notes,
                client.compagny_name,
            )
        console.print(table)

    def _extracted_employee_event(self, data):
        event_id = manager.create(**data)
        employee_controllers = EmployeeController()
        employee_controllers.get_employee_event(event_id=event_id)
        view.success_creating()
        return EventController()


class EventCreateController(EventController):
    def run(self):
        employee_controllers = EmployeeController()
        department = employee_controllers.get_user_login_department()
        if department == COMMERCIAL:
            data = self.get_data()
            try:
                return self._extracted_employee_event(data)
            except IntegrityError as e:
                sentry_sdk.capture_message(f"IntegrityError: {e}")
                sentry_sdk.capture_exception(e)
                return EventController()

            except Exception as e:
                sentry_sdk.capture_message(f"Unexpected error: {e}")
                sentry_sdk.capture_exception(e)
                raise

            finally:
                return EventController()
        view.error_not_have_right()
        return EventController()


class EventReadController(EventController):
    def run(self):
        while True:
            events = manager.read()
            self.get_table(events=events)
            continu = view.select_one_to_continue()
            if continu == "1":
                return EventController()


class EventUpdateController(EventController):
    def run(self):
        employee_controllers = EmployeeController()
        manager_employee = EmployeeManager()
        department = employee_controllers.get_user_login_department()
        if department == SUPPORT:
            events = manager.read()
            self.get_table(events=events)
            event_id = view.select_id()
            employee_id = employee_controllers.get_user_id_login()
            if manager_employee.get_relation_by_id(
                employee_id=employee_id, event_id=event_id
            ):
                try:
                    data = self.get_support_modify_data()
                    manager.update(event_id=event_id, **data)
                    view.success_update()
                except Exception as e:
                    sentry_sdk.capture_message(
                        f"Unexpected error during client update: {e}"
                    )
                    sentry_sdk.capture_exception(e)
                    view.error_not_found()
                    raise
                finally:
                    return EventController()
            else:
                view.error_not_have_right()
                return EventController()
        elif department == GESTION:
            return self._employee_event_relation(employee_controllers)
        else:
            view.error_not_have_right()
            return EventController()

    def _employee_event_relation(self, employee_controllers):
        event_id = self._extracted_event_table()
        employee_manager = EmployeeManager()
        employees = employee_manager.read()
        employees = employee_controllers.get_table(employees)
        employee_id = view.select_id()
        employee_manager.create_user_event_relation(
            employee_id=employee_id, event_id=event_id
        )
        view.success_update()
        return EventController()

    def _extracted_event_table(self):
        events = manager.read()
        self.get_table(events)
        return view.select_id()

    def get_support_modify_data(self):
        employee_controllers = EmployeeController()
        department_id = employee_controllers.get_user_login_department()
        contract = self.get_contract()
        client = self.get_client()
        if department_id == SUPPORT:
            return self._extracted_support_modify_data(contract, client)
        view.error_not_have_right()
        return EventController()

    def _extracted_support_modify_data(self, contract, client):
        view.display_title("Modify events")
        name = contract.name
        start_date, end_date = view.get_valid_date_range()
        address = client.address
        view.display_title("Attendees")
        attendees = view.get_number()
        notes = view.get_notes()
        client_id = client.id
        contract_id = contract.id
        employee_controllers = EmployeeController()
        employee_id = employee_controllers.get_user_id_login()
        return {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "address": address,
            "attendees": attendees,
            "notes": notes,
            "client_id": client_id,
            "contract_id": contract_id,
            "employee_id": employee_id,
        }


class EventDeleteController(EventController):
    def run(self):
        employee_controllers = EmployeeController()
        department = employee_controllers.get_user_login_department()
        if department != ADMIN:
            events = manager.read()
            self.get_table(events=events)
            event_id = view.select_id()
            if manager.delete(event_id=event_id):
                view.success_delete()
            else:
                view.error_not_found()
            return EventController()
        view.error_not_have_right()
        return EventController()
