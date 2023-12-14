from click import DateTime
from sqlalchemy import String, ForeignKey, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from EpicEvents.database import Model
from .contract import Contract
from .event import Event


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

    # commercial_id = mapped_column(ForeignKey("employee.id"))
    # commercial = relationship("employee", back_populates="clients")

    # contracts: Mapped[list["Contract"]] = relationship(back_populates="client")
    # events: Mapped[list["Event"]] = relationship(back_populates="client")

    # def __repr__(self):
    #     return (
    #         f"Client(id:{self.id}, fullname: {self.fullname}, email: {self.email}, phone: {self.phone},"
    #         f"compagny_name : {self.compagny_name!r}, creation_date : {self.creation_date!r},"
    #         f"updating_date : {self.updating_date!r},"
    #         f"commercial : {self.commercial.fullname!r})"
    #     )
