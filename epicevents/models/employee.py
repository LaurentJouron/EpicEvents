from ..database import Model, Session
from ..models.client import Client

from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient
from typing import List


class EmployeeManager:
    # CRUD
    def create(self, **kwargs):
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

    def read(self):
        with Session() as session:
            with session.begin():
                employees = session.query(Employee).all()
                for employee in employees:
                    print(employee.id)
                    if employee.id == 7:
                        print(employee.username)
                    session.expunge(employee)
                    make_transient(employee)
                return employees

    def update(self, employee_id, **kwargs):
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

    def delete(self, employee_id):
        with Session() as session:
            with session.begin():
                employee = session.query(Employee).get(employee_id)
                if employee:
                    session.delete(employee)
                    return True
                else:
                    return False

    # REQUESTS
    def get_by_username(self, username):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Employee)
                    .filter(Employee.username == username)
                    .first()
                )

    def get_by_id(self, employee_id):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Employee)
                    .filter(Employee.id == employee_id)
                    .first()
                )

    def get_password(self, username):
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

    def get_role_id_by_username(self, username):
        with Session() as session:
            with session.begin():
                employee = (
                    session.query(Employee)
                    .filter_by(username=username)
                    .first()
                )
                if employee:
                    return employee.role_id
                return None

    def get_id_by_username(self, username):
        with Session() as session:
            with session.begin():
                employee = (
                    session.query(Employee)
                    .filter_by(username=username)
                    .first()
                )
                if employee:
                    return employee.id
                return None

    def get_username_and_lastname_by_id(self, employee_id):
        with Session() as session:
            with session.begin():
                employee = (
                    session.query(Employee)
                    .filter_by(employee_id=employee_id)
                    .first()
                )
                if employee:
                    return f"{employee.username} {employee.last_name}"
                return None


# MODELS
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
