from epicevents.database import Session
from click import DateTime
from sqlalchemy import String, ForeignKey, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model
from .event import Event
from .employee import Employee


class ClientManager:
    def create_client(self):
        with Session() as session:
            with session.begin():
                ...

    def update_client(self):
        with Session() as session:
            with session.begin():
                ...

    def get_client_by_id(self, id):
        with Session() as session:
            with session.begin():
                ...

    def get_client_by_compagny_name(self, compagny_name):
        with Session() as session:
            with session.begin():
                ...

    def get_client_by_fullname(self, fullname):
        with Session() as session:
            with session.begin():
                ...

    def get_client_by_email(self, email):
        with Session() as session:
            with session.begin():
                ...

    def get_client_by_phone(self, phone):
        with Session() as session:
            with session.begin():
                ...

    def get_all_client(self):
        with Session() as session:
            with session.begin():
                ...

    def get_by_specific_client(self):
        with Session() as session:
            with session.begin():
                ...


class Client(Model):
    _tablename_ = "client"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    compagny_name: Mapped[str] = mapped_column(String(300))
    information: Mapped[str] = mapped_column(Text)
    last_name: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(300), unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    creation_date: Mapped[Date] = mapped_column(DateTime)
    updating_date: Mapped[Date] = mapped_column(DateTime)
    address: Mapped[Text] = mapped_column(Text)

    commercial_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    commercial: Mapped[list["Employee"]] = relationship(
        "Employee", back_populates="client"
    )

    events: Mapped[list["Event"]] = relationship(
        "Event",
        back_populates="event",
        cascade="all, delete",
        passive_deletes=True,
    )

    def __repr__(self):
        return (
            f"Client(id:{self.id}"
            f"fullname: {self.fullname}"
            f"email: {self.email}"
            f"phone: {self.phone}"
            f"compagny_name : {self.compagny_name!r}"
            f"creation_date : {self.creation_date!r}"
            f"updating_date : {self.updating_date!r}"
            f"commercial : {self.commercial.fullname!r})"
        )
