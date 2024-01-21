from ..database import Model, Session

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient
from typing import List


class RoleManager:
    """
    Manager class for handling database operations related to roles.

    Methods:
    - add_new(name: str): Add a new role with the given name to the database.
    - update(role_id: int, new_name: str): Update the name of a role with the given ID in the database.
    - delete(role_id: int) -> bool: Delete the role with the given ID from the database and return True if successful, False otherwise.
    - get_all() -> List[Role]: Get a list of all roles from the database.
    - get_name_by_id(role_id: int) -> str or None: Get the name of the role with the given ID from the database.
    """

    # CRUD
    def create(self, name):
        """
        Create role with the given name to the database.

        Args:
        - name (str): The name of the new role.
        """
        with Session() as session:
            with session.begin():
                new_role = Role(name=name)
                session.add(new_role)

    def read(self):
        """
        Get a list of all roles from the database.

        Returns:
        - List[Role]: A list of all roles.
        """
        with Session() as session:
            with session.begin():
                roles = session.query(Role).all()
                for role in roles:
                    session.expunge(role)
                    make_transient(role)
                return roles

    def update(self, role_id, new_name):
        """
        Update the name of a role with the given ID in the database.

        Args:
        - role_id (int): The ID of the role to update.
        - new_name (str): The new name for the role.
        """
        with Session() as session:
            with session.begin():
                role = session.query(Role).get(role_id)
                if role:
                    role.name = new_name

    def delete(self, role_id):
        """
        Delete the role with the given ID from the database.

        Args:
        - role_id (int): The ID of the role to delete.

        Returns:
        - bool: True if the role was deleted successfully, False otherwise.
        """
        with Session() as session:
            with session.begin():
                role = session.query(Role).get(role_id)
                if role:
                    session.delete(role)
                    return True
                else:
                    return False

    # REQUESTS
    def get_name_by_id(self, role_id):
        """
        Get the name of the role with the given ID from the database.

        Args:
        - role_id (int): The ID of the role.

        Returns:
        - str or None: The name of the role if found, None otherwise.
        """
        with Session() as session:
            with session.begin():
                role = session.query(Role).get(role_id)
                if role:
                    return role.name
                return None


# MODELS
class Role(Model):
    """
    Database model class representing a role.

    Attributes:
    - id (int): The unique identifier for the role.
    - name (str): The name of the role.
    - employee (List[Employee]): The list of employees associated with the role.
    """

    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    employee: Mapped[List["Employee"]] = relationship(back_populates="role")
