import time
import logging

from ..utils.bases.controllers import BaseController
from ..utils.contants import SHORT_SLEEP, NAME
from ..models import RoleManager
from ..views import RoleView
from ..controllers import home_controllers

from sqlalchemy.exc import IntegrityError

view = RoleView()
manager = RoleManager()


class RoleController(BaseController):
    def run(self):
        while True:
            choice = view.menu_choice()
            if choice == "1":
                view.clean_console()
                return CreateRoleController()

            elif choice == "2":
                view.clean_console()
                return UpdateRoleController()

            elif choice == "3":
                view.clean_console()
                return GetRoleByIdController()

            elif choice == "4":
                view.clean_console()
                return GetRoleByNameController()

            elif choice == "5":
                view.clean_console()
                return DeleteRoleController()

            elif choice == "6":
                view.clean_console()
                return GetAllRoleController()

            elif choice == "7":
                view.clean_console()
                return home_controllers.HomeController()


class CreateRoleController(BaseController):
    def run(self):
        role_name = view.get_name()
        try:
            manager.add_role(name=role_name)
            view.success_creating()
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            return RoleController()
        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            view.exist_error(role_name)
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            return RoleController()
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            time.sleep(SHORT_SLEEP)
            view.clean_console()
            raise
        finally:
            RoleController()


class UpdateRoleController(BaseController):
    def run(self):
        roles = manager.get_all_roles()
        view.display_roles_table(roles)
        role_id = view.get_id()
        try:
            role_name = manager.get_role_name_by_id(role_id)
            if role_name:
                view.role_information(NAME)
                new_name = view.get_name()
                manager.update_role(role_id, new_name)
                view.success_update()
            else:
                view.not_found()
        except Exception as e:
            logging.exception(f"Unexpected error during role update: {e}")
            view.message_error(str(e))
        finally:
            return RoleController()


class GetRoleByIdController(BaseController):
    def run(self):
        roles = manager.get_all_roles()
        view.display_roles_table(roles)
        role_id = view.get_id()
        role_name = manager.get_role_name_by_id(role_id)
        if role_name:
            view.role_information(role_name)
        else:
            view.invalid_id()
        return RoleController()


class GetRoleByNameController(BaseController):
    def run(self):
        roles = manager.get_all_roles()
        view.display_roles_table(roles)
        role_name = view.get_name()
        role_id = manager.get_role_id_by_name(role_name)
        if role_id:
            view.role_information(role_id)
        else:
            view.not_found()
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
        time.sleep(SHORT_SLEEP)
        view.clean_console()
        return RoleController()


class GetAllRoleController(BaseController):
    def run(self):
        roles = manager.get_all_roles()
        view.display_roles_table(roles)
        return RoleController()
