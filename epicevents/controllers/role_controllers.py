from epicevents.utils.bases.controllers import BaseController
from ..models import RoleManager
from ..views import RoleView

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
                ...
                # return HomeController()


class AddRoleController(BaseController):
    def run(self):
        name = view.role_name()
        role_manager.add_role(name=name)
        return RoleController()


class UpdateRoleController(BaseController):
    def run(self, name):
        ...
        return RoleController()


class GetRoleByIdController(BaseController):
    def run(self, role_id):
        ...
        return RoleController()


class GetRoleByNameController(BaseController):
    def run(self, name):
        ...
        return RoleController()


class GetAllRoleController(BaseController):
    def run(self):
        ...
        return RoleController()
