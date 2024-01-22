from ..utils.bases.controllers import BaseController
from ..models import EventManager, ClientManager, EmployeeManager
from ..views import EventView
from ..views.client_views import ClientView
from ..views.employee_views import EmployeeView
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
        start_date = view.get_date(type="start")
        end_date = view.get_date(type="end")
        address = view.get_address()
        view.display_title("Attendees")
        attendees = view.get_number()
        notes = view.get_notes()
        client_id = self.get_client_id()
        view.display_title("Commercial")
        commercial_id = self.get_employee_id()
        view.display_title("Gestion")
        support_id = self.get_employee_id()
        return {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "address": address,
            "attendees": attendees,
            "notes": notes,
            "client_id": client_id,
            "commercial_id": commercial_id,
            "support_id": support_id,
        }

    def get_client_id(self):
        client_manager = ClientManager()
        client_view = ClientView()
        clients = client_manager.read()
        client_view.display_table(clients)
        return view.select_id()

    def get_employee_id(self):
        employee_manager = EmployeeManager()
        employees = employee_manager.read()
        employee_view = EmployeeView()
        employee_view.display_table(employees=employees)
        return view.select_id()


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
        ...


class EventDeleteController(EventController):
    def run(self):
        ...
