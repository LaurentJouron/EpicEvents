from ..database import Model, Session

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient
from typing import List


class RoleManager:
    # CRUD
    def create(self, name):
        with Session() as session:
            with session.begin():
                new_role = Role(name=name)
                session.add(new_role)

    def read(self):
        with Session() as session:
            with session.begin():
                roles = session.query(Role).all()
                for role in roles:
                    session.expunge(role)
                    make_transient(role)
                return roles

    def update(self, role_id, new_name):
        with Session() as session:
            with session.begin():
                role = session.query(Role).get(role_id)
                if role:
                    role.name = new_name

    def delete(self, role_id):
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
        with Session() as session:
            with session.begin():
                role = session.query(Role).get(role_id)
                if role:
                    return role.name
                return None


# MODELS
class Role(Model):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    employee: Mapped[List["Employee"]] = relationship(back_populates="role")
