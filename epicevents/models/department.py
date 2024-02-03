from ..database import Model, Session

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient
from typing import List


class DepartmentManager:
    """
    Manages the operations related to departments.

    Provides methods for creating, reading, updating, and deleting departments.
    Also provides methods for retrieving department names based on department
    IDs.
    """

    # CRUD
    def create(self, name):
        """
        Creates a new department with the given name.

        Args:
            name: The name of the department.
        """

        with Session() as session:
            with session.begin():
                new_name = Department(name=name)
                session.add(new_name)

    def read(self):
        """
        Retrieves all departments.

        Returns:
            List[Department]: A list of all departments.
        """

        with Session() as session:
            with session.begin():
                departments = session.query(Department).all()
                for department in departments:
                    session.expunge(department)
                    make_transient(department)
                return departments

    def update(self, department_id, new_name):
        """
        Updates the name of a department with the given department ID.

        Args:
            department_id: The ID of the department to update.
            new_name: The new name for the department.
        """
        with Session() as session:
            with session.begin():
                if department := session.query(Department).get(department_id):
                    if department.name != new_name != "":
                        department.name = new_name

    def delete(self, department_id):
        """
        Updates the name of a department with the given department ID.

        Args:
            department_id: The ID of the department to update.
            new_name: The new name for the department.
        """

        with Session() as session:
            with session.begin():
                if department := session.query(Department).get(department_id):
                    session.delete(department)
                    return True
                else:
                    return False

    # REQUESTS
    def get_by_id(self, department_id):
        """
        Retrieves a department by its ID.

        Args:
            department_id: The ID of the department.

        Returns:
            The department with the specified ID, or None if not found.
        """
        with Session() as session:
            with session.begin():
                if department := (
                    session.query(Department)
                    .filter(Department.id == department_id)
                    .first()
                ):
                    session.expunge(department)
                    make_transient(department)
                return department


# MODELS
class Department(Model):
    """
    Represents a department.

    This model class defines the structure and attributes of a department,
    including its ID, name, and associated employees.
    """

    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    employee: Mapped[List["Employee"]] = relationship(
        back_populates="department"
    )
