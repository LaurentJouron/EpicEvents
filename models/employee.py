from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from EpicEvents.database import Model
from .role import Role
from .client import Client
from .event import Event
from .contract import Contract

class EmployeeManager:
    def get_by_id


class Employee(Model):
    _tablename_ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    fullname: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(300), unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(500))

    # role: Mapped[list["Role"]] = relationship(
    #     "Role",
    #     back_populates="list",
    #     cascade="all, delete",
    #     passive_deletes=True,
    # )

    # client: Mapped[list["Client"]] = relationship(
    #     "Client",
    #     back_populates="commercial",
    #     cascade="all, delete",
    #     passive_deletes=True,
    # )

    # contract: Mapped[list["Contract"]] = relationship(
    #     "Contract",
    #     back_populates="gestion",
    #     cascade="all, delete",
    #     passive_deletes=True,
    # )

    # event: Mapped[list["Event"]] = relationship(
    #     back_populates="support",
    #     cascade="all, delete",
    #     passive_deletes=True,
    # )

    # def __repr__(self) -> str:
    #     return f"Employee(id={self.id}, fullname='{self.fullname}')"
