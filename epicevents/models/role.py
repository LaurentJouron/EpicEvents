from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Model, Session
from models import Employee


class RoleManager:
    def add_role(self, name):
        with Session() as session:
            with session.begin():
                new_role = Role(name=name)
                session.add(new_role)

    def update_role(self, name):
        with Session() as session:
            with session.begin():
                ...

    def get_role_by_id(self):
        with Session() as session:
            with session.begin():
                ...

    def get_role_by_name(self, name):
        with Session() as session:
            with session.begin():
                ...

    def get_all_role(self):
        with Session() as session:
            with session.begin():
                ...


class Role(Model):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    employees: Mapped[list["Employee"]] = relationship(
        "Role",
        back_populates="role",
        cascade="all, delete",
        passive_deletes=True,
    )

    def __repr__(self):
        return f"Role(id={self.id}, name='{self.name}')"
