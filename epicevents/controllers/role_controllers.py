from ..utils.bases.controllers import BaseController
from ..models import RoleManager
from ..views import RoleView
from ..controllers import home_controllers
from ..controllers.employee_controllers import EmployeeLoginController

import logging

from sqlalchemy.exc import IntegrityError

view = RoleView()
manager = RoleManager()


class RoleController(BaseController):
    def run(self):
        while True:
            choice = view.choice_menu()
            if choice == "1":
                return RoleCreateController()

            elif choice == "2":
                return RoleReadController()

            elif choice == "3":
                return RoleUpdateController()

            elif choice == "4":
                return RoleDeleteController()

            elif choice == "5":
                return home_controllers.HomeController()


class RoleCreateController(RoleController):
    def run(self):
        login_role = EmployeeLoginController()
        role = login_role.read_login_file()

        # Suppression impossible
        if role["role_id"] == 0:
            name = view.get_name()
            try:
                manager.create(name=name)
                view.success_creating()
                return RoleController()

            except IntegrityError as e:
                logging.error(f"IntegrityError: {e}")
                return RoleController()

            except Exception as e:
                logging.exception(f"Unexpected error: {e}")
                raise

            finally:
                RoleController()
        else:
            view.error_not_have_right()
            return RoleController()


class RoleReadController(RoleController):
    def run(self):
        roles = manager.read()
        view.display_table(roles)
        return RoleController()


class RoleUpdateController(RoleController):
    def run(self):
        roles = manager.read()
        view.display_table(roles)
        role_id = view.select_id()
        try:
            role_name = manager.get_name_by_id(role_id)

            if role_name:
                new_name = view.get_name()
                manager.update(role_id, new_name)
                view.success_update()
            else:
                view.error_not_found()

        except Exception as e:
            logging.exception(f"Unexpected error during role update: {e}")
        finally:
            return RoleController()


class RoleDeleteController(RoleController):
    def run(self):
        roles = manager.read()
        view.display_table(roles)

        role_id = view.select_id()
        deleted = manager.delete(role_id=role_id)

        if deleted:
            view.success_delete()
        else:
            view.error_not_found()
        return RoleController()
