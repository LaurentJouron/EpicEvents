from sqlalchemy import select
from epicevents.controllers import HomeController
from epicevents.database import Session
from utils.bases.controllers import BaseController
from models.role import RoleManager
from views.role_views import RoleView

view = RoleView()
role_manager = RoleManager()


class RoleController(BaseController):
    def run(self):
        while True:
            choice = view.display_menu(view.role_menu)
            if choice == "1":
                return AddRoleController()

            elif choice == "2":
                return UpdateRoleController()

            elif choice == "3":
                return GetRoleByIdController()

            elif choice == "4":
                return GetRoleByNameController()

            elif choice == "5":
                return GetAllRoleController()

            elif choice == "6":
                return HomeController()


class AddRoleController(BaseController):
    def run(self):
        ...


class UpdateRoleController(BaseController):
    def run(self, name):
        ...


class GetRoleByIdController(BaseController):
    def run(self, role_id):
        ...


class GetRoleByNameController(BaseController):
    def run(self, name):
        ...


class GetAllRoleController(BaseController):
    def run(self):
        ...
