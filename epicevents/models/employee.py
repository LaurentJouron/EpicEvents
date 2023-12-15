from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model, Session
from models import Role, Client, Event, Contract


class EmployeeManager:
    def add_employee(self):
        with Session() as session:
            with session.begin():
                ...

    def get_employee_by_name(self):
        with Session() as session:
            with session.begin():
                ...

    def get_employee_by_id(self):
        with Session() as session:
            with session.begin():
                ...

    def get_employee_by_function(self):
        with Session() as session:
            with session.begin():
                ...

    def get_all_employee(self):
        with Session() as session:
            with session.begin():
                ...

    def login(self):
        with Session() as session:
            with session.begin():
                ...


class Employee(Model):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    fullname: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(300), unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(500))

    role_id: Mapped[int] = mapped_column(
        ForeignKey("role.id", ondelete="CASCADE")
    )
    role: Mapped[list["Role"]] = relationship(
        "Role", back_populates="employee"
    )

    client: Mapped[list["Client"]] = relationship(
        "Client", back_populates="employee"
    )

    contract: Mapped[list["Contract"]] = relationship(
        "Contract", back_populates="employee"
    )

    event_technician: Mapped[list["Event"]] = relationship(
        "Event", back_populates="employee"
    )

    event_commercial: Mapped[list["Event"]] = relationship(
        "Event", back_populates="employee"
    )

    def __repr__(self):
        return (
            f"Employee(id:{self.id}"
            f"last_name: {self.last_name}"
            f"first_name: {self.first_name}"
            f"fullname: {self.fullname}"
            f"email: {self.email}"
            f"phone: {self.phone}"
            f"password: {self.password}"
            f"role: {self.role}"
            f"client: {self.client.compagny_name!r}"
            f"event_technician: {self.event_technician!r}"
            f"event_commercial: {self.event_commercial!r}"
        )
