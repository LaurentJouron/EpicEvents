from click import prompt
from ..utils.bases.controllers import BaseController
from ..models import EventManager, ClientManager, EmployeeManager
from ..models.contract import ContractManager
from ..views import EventView
from ..views.client_views import ClientView
from ..views.employee_views import EmployeeView
from ..views.contract_views import ContractView
from ..controllers.employee_controllers import EmployeeLoginController
from ..controllers import home_controllers
import logging

from sqlalchemy.exc import IntegrityError

view = EventView()
manager = EventManager()


class EventController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                return EventCreateController()

            elif choice == "2":
                return EventReadController()

            elif choice == "3":
                return EventUpdateController()

            elif choice == "4":
                return EventDeleteController()

            elif choice == "5":
                return home_controllers.HomeController()

    def get_data(self):
        view.display_title("Create events")
        name = view.get_name()
        start_date, end_date = view.get_valid_date_range()
        address = view.get_address()
        view.display_title("Attendees")
        attendees = view.get_number()
        notes = view.get_notes()
        client_id = self.get_client_id()
        contract_id = self.get_contract_id()
        return {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "address": address,
            "attendees": attendees,
            "notes": notes,
            "client_id": client_id,
            # "support_id": support_id,
            "contract_id": contract_id,
        }

    def get_client_id(self):
        client_manager = ClientManager()
        client_view = ClientView()
        clients = client_manager.read()
        client_view.display_table(clients=clients)
        return client_view.select_id()

    def get_employee_id(self):
        employee_manager = EmployeeManager()
        employee_view = EmployeeView()
        employees = employee_manager.read()
        employee_view.display_table(employees=employees)
        return employee_view.select_id()

    def get_contract_id(self):
        contract_manager = ContractManager()
        contract_view = ContractView()
        contracts = contract_manager.read()
        contract_view.display_table(contracts=contracts)
        return contract_view.select_id()


class EventCreateController(EventController):
    def run(self):
        data = self.get_data()
        try:
            manager.create(**data)
            view.success_creating()
            return EventController()

        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            return EventController()

        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            raise

        finally:
            EventController()


class EventReadController(EventController):
    def run(self):
        events = manager.read()
        view.display_table(events=events)
        return EventController()


class EventUpdateController(EventController):
    def run(self):
        employee = EmployeeLoginController()
        employee = employee.read_login_file()
        # Modification uniquement si rôle = Commercial
        if employee["role_id"] == 1:
            contract_id = self.get_contract_id()
            try:
                contract = manager.get_status_by_id(contract_id)
                print(contract)

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
                logging.exception(
                    f"Unexpected error during client update: {e}"
                )
                view.error_not_found()
                raise
            finally:
                EventController()
        else:
            view.error_not_have_right()
            return EventController()


class EventDeleteController(EventController):
    def run(self):
        login_role = EmployeeLoginController()
        role = login_role.read_login_file()

        # Suppression impossible
        if role["role_id"] == 0:
            events = manager.read()
            view.display_table(events=events)

            client_id = view.select_id()
            deleted = manager.delete(client_id=client_id)
            if deleted:
                view.success_delete()
            else:
                view.error_not_found()
            return EventController()
        else:
            view.error_not_have_right()
            return EventController()
