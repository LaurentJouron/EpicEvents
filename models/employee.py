from epicevents.database import Session
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model
from .role import Role
from .client import Client
from .event import Event
from .contract import Contract


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
        "Role",
        back_populates="list",
        cascade="all, delete",
        passive_deletes=True,
    )

    client_id: Mapped[int] = mapped_column(
        ForeignKey("client.id", ondelete="CASCADE")
    )
    client: Mapped[list["Client"]] = relationship(
        "Client",
        back_populates="commercial",
        cascade="all, delete",
        passive_deletes=True,
    )

    contract_id: Mapped[int] = mapped_column(
        ForeignKey("contract.id", ondelete="CASCADE")
    )
    contract: Mapped[list["Contract"]] = relationship(
        "Contract",
        back_populates="gestion",
        cascade="all, delete",
        passive_deletes=True,
    )

    event_id: Mapped[int] = mapped_column(
        ForeignKey("event.id", ondelete="CASCADE")
    )
    event: Mapped[list["Event"]] = relationship(
        back_populates="support",
        cascade="all, delete",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f"Employee(id={self.id}, fullname='{self.fullname}')"
