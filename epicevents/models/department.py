from ..database import Model, Session

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient
from typing import List


class DepartmentManager:
    # CRUD
    def create(self, name):
        with Session() as session:
            with session.begin():
                new_name = Department(name=name)
                session.add(new_name)

    def read(self):
        with Session() as session:
            with session.begin():
                departments = session.query(Department).all()
                for department in departments:
                    session.expunge(department)
                    make_transient(department)
                return departments

    def update(self, department_id, new_name):
        with Session() as session:
            with session.begin():
                department = session.query(Department).get(department_id)
                if department:
                    department.name = new_name

    def delete(self, department_id):
        with Session() as session:
            with session.begin():
                department = session.query(Department).get(department_id)
                if department:
                    session.delete(department)
                    return True
                else:
                    return False

    # REQUESTS
    def get_name_by_id(self, department_id):
        with Session() as session:
            with session.begin():
                department = session.query(Department).get(department_id)
                if department:
                    return department.name
                return None


# MODELS
class Department(Model):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    employee: Mapped[List["Employee"]] = relationship(
        back_populates="department"
    )
