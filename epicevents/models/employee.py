from ..database import Model, Session
from ..models.client import Client

from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, joinedload
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
                    department_id=kwargs["department_id"],
                )
                session.add(new_employee)

    def read(self):
        with Session() as session:
            with session.begin():
                employees = session.query(Employee).all()
                for employee in employees:
                    session.expunge(employee)
                    make_transient(employee)
                return employees

    def update(self, employee_id, **kwargs):
        with Session() as session:
            with session.begin():
                if employee := session.query(Employee).get(employee_id):
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
                    if kwargs["department_id"] != employee.department_id:
                        employee.department_id = kwargs["department_id"]

    def delete(self, employee_id):
        with Session() as session:
            with session.begin():
                if employee := session.query(Employee).get(employee_id):
                    session.delete(employee)
                    return True
                else:
                    return False

    # REQUESTS

    def get_by_id(self, employee_id):
        with Session() as session:
            with session.begin():
                if employee := (
                    session.query(Employee)
                    .options(joinedload(Employee.department))
                    .filter(Employee.id == employee_id)
                    .first()
                ):
                    session.enable_relationship_loading(employee)
                    session.expunge(employee)
                    make_transient(employee)
                return employee

    def get_by_username(self, username):
        with Session() as session:
            with session.begin():
                if employee := (
                    session.query(Employee)
                    .filter(Employee.username == username)
                    .first()
                ):
                    session.expunge(employee)
                    make_transient(employee)
                return employee


# MODELS
employee_event = Table(
    "employee_event",
    Model.metadata,
    Column("employee_id", ForeignKey("event.id")),
    Column("event_id", ForeignKey("employee.id")),
)


class Employee(Model):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(300), unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(500))

    department_id: Mapped[int] = mapped_column(
        ForeignKey("department.id"), nullable=True
    )
    department: Mapped["Department"] = relationship(back_populates="employee")

    client: Mapped[List["Client"]] = relationship(back_populates="employee")

    event: Mapped[List["Event"]] = relationship(secondary=employee_event)

    gestion: Mapped[List["Contract"]] = relationship(back_populates="employee")
