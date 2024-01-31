from ..utils.bases.controllers import BaseController
from ..utils.contants import COMMERCIAL, ADMIN
from ..models import EventManager, ClientManager, EmployeeManager
from ..models.contract import ContractManager
from ..views import EventView
from ..views.client_views import ClientView
from ..views.employee_views import EmployeeView
from ..views.contract_views import ContractView
from ..controllers.employee_controllers import (
    EmployeeLoginController,
    EmployeeController,
)
from ..controllers import home_controllers
import logging

from sqlalchemy.exc import IntegrityError

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
        client_view = ClientView()
        clients = client_manager.read()
        client_view.display_table(clients=clients)
        client_id = client_view.select_id()
        return client_manager.get_by_id(client_id=client_id)

    def get_employee(self):
        employee_manager = EmployeeManager()
        employee_view = EmployeeView()
        employees = employee_manager.read()
        employee_view.display_table(employees=employees)
        employee_id = employee_view.select_id()
        return employee_manager.get_by_id(employee_id=employee_id)

    def get_contract(self):
        contract_manager = ContractManager()
        contract_view = ContractView()
        contracts = contract_manager.read()
        contract_view.display_table(contracts=contracts)
        contract_id = contract_view.select_id()
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


class EventCreateController(EventController):
    def run(self):
        data = self.get_data()
        try:
            event_id = manager.create(**data)
            print(event_id)
            input("rien")
            view.success_creating()
            return EventController()

        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            return EventController()

        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            raise

        finally:
            return EventController()


class EventReadController(EventController):
    def run(self):
        while True:
            events = manager.read()
            view.display_table(events=events)
            continu = view.select_one_to_continue()
            if continu == "1":
                return EventController()


class EventUpdateController(EventController):
    def run(self):
        contract_id = self.get_contract_id()
        try:
            contract = manager.get_status_by_id(contract_id)

            # Modification possible uniquement pour le commercial
            if contract["status"] is True:
                if contract:
                    data = self.get_data()
                    manager.update(contract_id, **data)
                    view.success_update()
                    return EventController()
                else:
                    view.error_not_found()
            else:
                view.error_not_have_right()
                return EventController()

        except Exception as e:
            logging.exception(f"Unexpected error during client update: {e}")
            view.error_not_found()
            raise
        finally:
            return EventController()


class EventDeleteController(EventController):
    def run(self):
        events = manager.read()
        view.display_table(events=events)

        event_id = view.select_id()
        if manager.delete(event_id=event_id):
            view.success_delete()
        else:
            view.error_not_found()
        return EventController()
