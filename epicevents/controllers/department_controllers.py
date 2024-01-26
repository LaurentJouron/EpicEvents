from ..utils.bases.controllers import BaseController
from ..models import DepartmentManager
from ..views import DepartmentView
from ..controllers import home_controllers
import logging

from sqlalchemy.exc import IntegrityError

view = DepartmentView()
manager = DepartmentManager()


class DepartmentController(BaseController):
    def run(self):
        while True:
            choice = view.choice_menu()
            if choice == "1":
                return DepartmentCreateController()

            elif choice == "2":
                return DepartmentReadController()

            elif choice == "3":
                return DepartmentUpdateController()

            elif choice == "4":
                return DepartmentDeleteController()

            elif choice == "5":
                return home_controllers.HomeController()


class DepartmentCreateController(DepartmentController):
    def run(self):
        name = view.get_name()
        try:
            manager.create(name=name)
            view.success_creating()
            return DepartmentController()

        except IntegrityError as e:
            logging.error(f"IntegrityError: {e}")
            return DepartmentController()

        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            raise

        finally:
            DepartmentController()


class DepartmentReadController(DepartmentController):
    def run(self):
        departments = manager.read()
        view.display_table(departments=departments)
        return DepartmentController()


class DepartmentUpdateController(DepartmentController):
    def run(self):
        departments = manager.read()
        view.display_table(departments)
        department_id = view.select_id()
        try:
            department_name = manager.get_name_by_id(department_id)

            if department_name:
                new_name = view.get_name()
                manager.update(department_id, new_name)
                view.success_update()
            else:
                view.error_not_found()

        except Exception as e:
            logging.exception(f"Unexpected error during role update: {e}")
        finally:
            return DepartmentController()


class DepartmentDeleteController(DepartmentController):
    def run(self):
        departments = manager.read()
        view.display_table(departments)

        department_id = view.select_id()
        deleted = manager.delete(department_id=department_id)

        if deleted:
            view.success_delete()
        else:
            view.error_not_found()
        return DepartmentController()
