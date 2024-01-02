import time
import logging
from sqlalchemy.exc import IntegrityError
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
        try:
            manager.add_role(name=role_name)
            view.success_creating()
            time.sleep(1)
            view.clean_console()
            return RoleController()
        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            view.exist_error(role_name)
            time.sleep(1)
            view.clean_console()
            return RoleController()
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            time.sleep(1)
            view.clean_console()
            raise
        finally:
            RoleController()


class UpdateRoleController(BaseController):
    def run(self):
        all_role = GetAllRoleController()
        all_role.run()
        role_id = view.get_id()
        existing_role = manager.get_role_by_id(role_id)
        if not existing_role:
            view.invalid_id()
            return RoleController()
        view.display_name(existing_role)
        new_name = view.get_name()
        manager.update_role(existing_role, new_name)
        view._success_update()
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
    def run(self):
        all_role = GetAllRoleController()
        all_role.run()
        name = view.get_name()
        role = manager.get_role_by_name(name)
        if role:
            view.display_name(name)
        else:
            view.not_found(name)
        return RoleController()


class DeleteRoleController(BaseController):
    def run(self):
        all_role = GetAllRoleController()
        all_role.run()
        role_id = view.get_id()
        deleted = manager.delete_role(role_id)
        if deleted:
            view.success_delete()
        else:
            view.not_found()
        time.sleep(1)
        view.clean_console()
        return RoleController()


class GetAllRoleController(BaseController):
    def run(self):
        roles = manager.get_all_roles()
        view.display_roles_table(roles)
        return RoleController()
