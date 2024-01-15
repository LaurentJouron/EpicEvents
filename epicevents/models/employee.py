from sqlalchemy import String, ForeignKey
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient
from typing import List

from ..database import Model, Session
from ..models.client import Client


class EmployeeManager:
    def create_employee(self, **kwargs):
        with Session() as session:
            with session.begin():
                new_employee = Employee(
                    username=kwargs["username"],
                    last_name=kwargs["last_name"],
                    email=kwargs["email"],
                    phone=kwargs["phone"],
                    password=kwargs["password"],
                    role_id=kwargs["role_id"],
                )
                session.add(new_employee)

    def get_employee_by_username(self, username):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Employee)
                    .filter(Employee.username == username)
                    .first()
                )

    def update_employee(self, employee_id, **kwargs):
        with Session() as session:
            with session.begin():
                employee = session.query(Employee).get(employee_id)
                if employee:
                    if kwargs["username"] != employee.username:
                        employee.username = kwargs["username"]
                    if kwargs["last_name"] != employee.last_name:
                        employee.last_name = kwargs["last_name"]
                    if kwargs["email"] != employee.email:
                        employee.email = kwargs["email"]
                    if kwargs["phone"] != employee.phone:
                        employee.phone = kwargs["phone"]
                    if kwargs["password"] != employee.password:
                        employee.password = kwargs["password"]
                    if kwargs["role_id"] != employee.role_id:
                        employee.role_id = kwargs["role_id"]

    def get_employee_by_id(self, employee_id):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Employee)
                    .filter(Employee.id == employee_id)
                    .first()
                )

    def get_employee_password_by_username(self, username):
        with Session() as session:
            with session.begin():
                employee = (
                    session.query(Employee)
                    .filter(Employee.username == username)
                    .first()
                )
                if employee:
                    return employee.password
                return None

    def get_employee_by_email(self, email):
        with Session() as session:
            with session.begin():
                session.query(Employee).filter_by(email=email)

    def get_all_employee(self):
        with Session() as session:
            with session.begin():
                employees = session.query(Employee).all()
                for employee in employees:
                    session.expunge(employee)
                    make_transient(employee)
                return employees

    def delete_employee(self, employee_id):
        with Session() as session:
            with session.begin():
                employee = session.query(Employee).get(employee_id)
                if employee:
                    session.delete(employee)
                    return True
                else:
                    return False


employee_event = Table(
    "employee_event",
    Model.metadata,
    Column("employee_id", ForeignKey("event.id")),
    Column("event_id", ForeignKey("employee.id")),
)


class Employee(Model):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(300), unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(500))

    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"), nullable=True)
    role: Mapped["Role"] = relationship(back_populates="employee")

    client: Mapped[List["Client"]] = relationship(back_populates="commercial")

    event: Mapped[List["Event"]] = relationship(secondary=employee_event)

    gestion: Mapped[List["Contract"]] = relationship(back_populates="gestion")
