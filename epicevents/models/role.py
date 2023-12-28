from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from epicevents.database import Model, Session


class RoleManager:
    def add_role(self, name):
        with Session() as session:
            with session.begin():
                new_role = Role(name=name)
                session.add(new_role)

    def update_role(self, role_id, new_name):
        with Session() as session:
            with session.begin():
                role = session.query(Role).get(role_id)
                if role:
                    role.name = new_name

    def get_role_by_id(self, role_id):
        with Session() as session:
            with session.begin():
                return session.query(Role).get(role_id)

    def get_role_by_name(self, name):
        with Session() as session:
            with session.begin():
                return session.query(Role).filter_by(name=name).first()

    def get_all_roles(self):
        with Session() as session:
            with session.begin():
                return session.query(Role).all()


class Role(Model):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    employee: Mapped[List["Employee"]] = relationship(back_populates="role")

    def __repr__(self):
        return f"Role(id={self.id}, name='{self.name}')"
