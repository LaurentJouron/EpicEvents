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


class RoleInitialiseController(BaseController):
    def run(self):
        for role in view.initialise_role():
            role_manager.add_role(role)


class AddRoleController(BaseController):
    def run(self):
        role_name = view.get_role_name()
        existing_role = role_manager.get_name(role_name)
        if existing_role:
            view.exist_error(role_name)
            return RoleController()
        role_manager.add_role(name=role_name)
        view.success_message(role_name)
        return RoleController()


class UpdateRoleController(BaseController):
    def run(self, role_id):
        existing_role = role_manager.get_by_id(role_id)
        if not existing_role:
            view.invalid_id()
            return RoleController()
        view.role_information(existing_role)
        new_name = view.get_role_name()
        role_manager.update_role(existing_role, new_name)
        view.success_update(new_name)
        return RoleController()


class GetRoleByIdController(BaseController):
    def run(self, role_id):
        role = role_manager.get_by_id(role_id)
        if role:
            view.role_information(role)
        else:
            view.invalid_id()
        return RoleController()


class GetRoleByNameController(BaseController):
    def run(self, name):
        role = role_manager.get_by_name(name)
        if role:
            view.role_information(role)
        else:
            view.invalid_name(name)
        return RoleController()


class GetAllRoleController(BaseController):
    def run(self):
        all_roles = role_manager.get_all_role()
        if all_roles:
            view.all_round()
            for role in all_roles:
                print(role)
        else:
            view.not_found()
        return RoleController()
