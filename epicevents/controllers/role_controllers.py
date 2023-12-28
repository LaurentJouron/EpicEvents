from epicevents.utils.bases.controllers import BaseController
from ..models import RoleManager
from ..views import RoleView
from ..controllers import home_controllers

view = RoleView()
manager = RoleManager()


class RoleController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                return CreateRoleController()

            elif choice == "2":
                return UpdateRoleController()

            elif choice == "3":
                return GetRoleByIdController()

            elif choice == "4":
                return GetRoleByNameController()

            elif choice == "5":
                return DeleteRoleController()

            elif choice == "6":
                return GetAllRoleController()

            elif choice == "7":
                return home_controllers.HomeController()


class CreateRoleController(BaseController):
    def run(self):
        role_name = view.get_name()
        existing_role = manager.add_role(role_name)
        if existing_role:
            view.exist_error(role_name)
            return RoleController()
        manager.add_role(name=role_name)
        view.success_message()
        return RoleController()


class UpdateRoleController(BaseController):
    def run(self):
        role_id = view.get_id()
        existing_role = manager.get_id(role_id)
        if not existing_role:
            view.invalid_id()
            return RoleController()
        view.role_information(existing_role)
        new_name = view.get_role_name()
        manager.update_role(existing_role, new_name)
        view.success_update(new_name)
        return RoleController()


class GetRoleByIdController(BaseController):
    def run(self):
        role_id = view.get_id()
        role = manager.get_by_id(role_id)
        if role:
            view.role_information(role)
        else:
            view.invalid_id()
        return RoleController()


class GetRoleByNameController(BaseController):
    def run(self, name):
        name = view.get_name()
        role = manager.get_by_name(name)
        if role:
            view.role_information(role)
        else:
            view.invalid_name(name)
        return RoleController()


class DeleteRoleController(BaseController):
    def run(self):
        ...


class GetAllRoleController(BaseController):
    def run(self):
        all_roles = manager.get_all_role()
        if all_roles:
            view.all_round()
            for role in all_roles:
                print(role)
        else:
            view.not_found()
        return RoleController()
