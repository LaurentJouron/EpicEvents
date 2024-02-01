from ..database import Model, Session

from sqlalchemy import String, ForeignKey, Table, Column, insert
from sqlalchemy.orm import Mapped, mapped_column, relationship, joinedload
from sqlalchemy.orm.session import make_transient
from typing import List


class EmployeeManager:
    """
    Manages the CRUD operations for employees.

    Provides methods to create, read, update, and delete employee records.
    Also provides methods to retrieve employees by ID or username.

    Args:
        self
    """

    # CRUD
    def create(self, **kwargs):
        """
        Creates a new employee record.

        Args:
            **kwargs: Keyword arguments for the employee attributes.

        Returns:
            None
        """
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
        """
        Retrieves all employee records.

        Returns:
            List[Employee]: A list of all employee records.
        """
        with Session() as session:
            with session.begin():
                employees = (
                    session.query(Employee)
                    .options(joinedload(Employee.department))
                    .all()
                )
                for employee in employees:
                    session.expunge(employee)
                    make_transient(employee)
                return employees

    def update(self, employee_id, **kwargs):
        """
        Updates an existing employee record.

        Args:
            employee_id: The ID of the employee to update.
            **kwargs: Keyword arguments for the employee attributes to update.

        Returns:
            None
        """
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
        """
        Deletes an employee record.

        Args:
            employee_id: The ID of the employee to delete.

        Returns:
            bool: True if the employee record was deleted, False otherwise.
        """
        with Session() as session:
            with session.begin():
                if employee := session.query(Employee).get(employee_id):
                    session.delete(employee)
                    return True
                else:
                    return False

    # REQUESTS

    def get_by_id(self, employee_id):
        """
        Retrieves an employee record by ID.

        Args:
            employee_id: The ID of the employee to retrieve.

        Returns:
            Employee: The employee record with the specified ID.
        """
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
        """
        Retrieves an employee record by username.

        Args:
            username: The username of the employee to retrieve.

        Returns:
            Employee: The employee record with the specified username.
        """
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

    # CRUD
    def create_user_event_relation(self, **kwargs):
        """
        Creates a new employee record.

        Args:
            **kwargs: Keyword arguments for the employee attributes.

        Returns:
            None
        """
        with Session() as session:
            with session.begin():
                new_relation = insert(employee_event).values(
                    employee_id=kwargs["employee_id"],
                    event_id=kwargs["event_id"],
                )
                session.execute(new_relation)

    def get_relation_by_id(self, employee_id, event_id):
        with Session() as session:
            with session.begin():
                relation = (
                    session.query(employee_event)
                    .filter(employee_event.employee_id == employee_id)
                    .filter(employee_event.event_id == event_id)
                    .first()
                )
                if relation:
                    return True


# MODELS
employee_event = Table(
    "employee_event",
    Model.metadata,
    Column("employee_id", ForeignKey("employee.id")),
    Column("event_id", ForeignKey("event.id")),
)


class Employee(Model):
    """
    Represents an employee.

    Attributes:
        id (int): The ID of the employee.
        username (str): The username of the employee.
        last_name (str): The last name of the employee.
        email (str): The email address of the employee.
        phone (str): The phone number of the employee.
        password (str): The password of the employee.
        department_id (int): The ID of the department the employee belongs to.
        department (Department): The department the employee belongs to.
        client (List[Client]): The clients associated with the employee.
        event (List[Event]): The events associated with the employee.
        gestion (List[Contract]): The contracts managed by the employee.
    """

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
    department: Mapped["Department"] = relationship(
        back_populates="employee", lazy="joined"
    )

    client: Mapped[List["Client"]] = relationship(back_populates="employee")

    event: Mapped[List["Event"]] = relationship(secondary=employee_event)

    gestion: Mapped[List["Contract"]] = relationship(back_populates="employee")
