from ..utils.bases.controllers import BaseController
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
        ...


class EventUpdateController(BaseController):
    def run(self):
        ...


class EventDeleteController(BaseController):
    def run(self):
        ...


class EventDisplayAllController(BaseController):
    def run(self):
        ...
