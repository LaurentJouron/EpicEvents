from epicevents.utils.bases.controllers import BaseController
from ..models import EventManager
from ..views import EventView
from ..controllers import home_controllers

view = EventView()
manager = EventManager()


class EventController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                return CreateEventController()

            elif choice == "2":
                return UpdateEventController()

            elif choice == "3":
                return GetEventByIdController()

            elif choice == "4":
                return GetEventByNameController()

            elif choice == "5":
                return DeleteEventController()

            elif choice == "6":
                return GetAllEventController()

            elif choice == "7":
                return home_controllers.HomeController()


class CreateEventController(BaseController):
    def run(self):
        ...


class UpdateEventController(BaseController):
    def run(self):
        ...


class GetEventByIdController(BaseController):
    def run(self):
        ...


class GetEventByNameController(BaseController):
    def run(self):
        ...


class DeleteEventController(BaseController):
    def run(self):
        ...


class GetAllEventController(BaseController):
    def run(self):
        ...
