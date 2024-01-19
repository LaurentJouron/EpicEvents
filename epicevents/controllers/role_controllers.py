from ..utils.bases.controllers import BaseController
from ..models import RoleManager
from ..views import RoleView
from ..controllers import home_controllers
import logging

from sqlalchemy.exc import IntegrityError

view = RoleView()
manager = RoleManager()


class RoleController(BaseController):
    def run(self):
        while True:
            choice = view.choice_menu()
            if choice == "1":
                return RoleCreationController()

            elif choice == "2":
                return RoleUpdateController()

            elif choice == "3":
                return RoleDeleteController()

            elif choice == "4":
                return RoleDisplayAllController()

            elif choice == "5":
                return home_controllers.HomeController()


class RoleCreationController(BaseController):
    def run(self):
        role_name = view.get_role_name()
        try:
            manager.add_role(name=role_name)
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


class RoleUpdateController(BaseController):
    def run(self):
        roles = manager.get_all_roles()
        view.display_roles_table(roles)
        role_id = view.get_role_id()
        try:
            role_name = manager.get_role_name_by_id(role_id)
            if role_name:
                new_name = view.get_role_name()
                manager.update_role(role_id, new_name)
                view.success_update()
            else:
                view.not_found()
        except Exception as e:
            logging.exception(f"Unexpected error during role update: {e}")
        finally:
            return RoleController()


class RoleDeleteController(BaseController):
    def run(self):
        roles = manager.get_all_roles()
        view.display_roles_table(roles)

        role_id = view.get_role_id()
        deleted = manager.delete_role(role_id=role_id)
        if deleted:
            view.success_delete()
        else:
            view.not_found()
        return RoleController()


class RoleDisplayAllController(BaseController):
    def run(self):
        roles = manager.get_all_roles()
        view.display_roles_table(roles)
        return RoleController()
