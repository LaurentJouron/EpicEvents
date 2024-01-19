from epicevents.views import employee_views
from ..utils.bases.controllers import BaseController
from ..models import EventManager, ClientManager, EmployeeManager
from ..views import EventView, client_views
from ..controllers import home_controllers, employee_controllers

view = EventView()
manager = EventManager()


class EventController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                return EventCreateController()

            elif choice == "2":
                return EventUpdateController()

            elif choice == "3":
                return EventDeleteController()

            elif choice == "4":
                return EventDisplayAllController()

            elif choice == "5":
                return home_controllers.HomeController()


class EventCreateController(BaseController):
    def run(self):
        view.display_title()
        name = view.get_name()
        start_date = view.get_date(type="start")
        end_date = view.get_date(type="end")
        address = view.get_address()
        attendees = view.get_number()
        notes = view.get_notes()
        client_id = self.get_client_id()
        commercial_id = self.get_employee_id()
        support_id = self.get_employee_id()
        # contract_id = contract.contract_id
        return {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "address": address,
            "attendees": attendees,
            "notes": notes,
            "client_id": client_id,
            # "contract_id": contract_id,
            "commercial_id": commercial_id,
            "support_id": support_id,
        }

    def get_client_id(self):
        client_manager = ClientManager()
        client_view = client_views.ClientView()
        clients = client_manager.get_all_client()
        client_view.display_client_table(clients)
        return view.select_id()

    def get_employee_id(self):
        employee_manager = EmployeeManager()
        employee_view = employee_views.EmployeeView()
        employees = employee_manager.get_all_employee()
        employee_view.display_employee_table(employees=employees)
        return view.select_id()


class EventUpdateController(BaseController):
    def run(self):
        ...


class EventDeleteController(BaseController):
    def run(self):
        ...


class EventDisplayAllController(BaseController):
    def run(self):
        ...
