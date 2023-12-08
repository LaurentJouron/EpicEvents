from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from EpicEvents import controllers as home
from models.employee import Employee
from views.employee_views import EmployeeView

view = EmployeeView()


class EmployeeController:
    def __init__(self):
        # Configuration la base de données et la session
        engine = create_engine("sqlite:///db.sqlite")
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def run(self):
        while True:
            choice = view.display_menu(view.employee_menu)
            if choice == "1":
                return EmployeeCreationController()
            elif choice == "2":
                return EmployeeModifyController()
            elif choice == "3":
                return EmployeeDeleteController()
            elif choice == "4":
                return EmployeeDisplayAll()
            elif choice == "5":
                return home.HomeController()


class EmployeeCreationController:
    def __init__(self):
        self.model = Employee

    def run(self):
        employee_data = view.get_employee_data()
        new_employee = Employee(**employee_data)
        new_employee.register(self.session)
        return EmployeeController()


class EmployeeModifyController:
    def __init__(self):
        self.model = Employee

    def run(self):
        username = view.get_one_employee()
        employee = (
            self.session.query(Employee).filter_by(username=username).first()
        )

        if employee:
            new_data = view.get_employee_data()
            for key, value in new_data.items():
                setattr(employee, key, value)
            self.session.commit()
            self.updated_succefully()
        else:
            self.not_found()
        return EmployeeController()


class EmployeeDeleteController:
    def __init__(self):
        self.model = Employee

    def run(self):
        username = view.get_one_employee()
        employee = (
            self.session.query(Employee).filter_by(username=username).first()
        )

        if employee:
            self.session.delete(employee)
            self.session.commit()
            self.delete_succefully()
        else:
            self.not_found()
        return EmployeeController()


class EmployeeDisplayAll:
    def __init__(self):
        self.model = Employee

    def run(self):
        employees = self.session.query(Employee).all()
        self.view.display_employees(employees)
        return EmployeeController()
