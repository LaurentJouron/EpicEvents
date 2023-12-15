from epicevents.database import Session
from click import DateTime
from sqlalchemy import String, ForeignKey, Date, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model
from .contract import Contract


class EventManager:
    def add_event(self):
        with Session() as session:
            with session.begin():
                ...

    def get_event_by_name(self):
        with Session() as session:
            with session.begin():
                ...

    def get_event_by_id(self):
        with Session() as session:
            with session.begin():
                ...

    def get_all_event(self):
        with Session() as session:
            with session.begin():
                ...


class Event(Model):
    __tablename__ = "event"
    id: Mapped[int] = mapped_column(primary_key=True)
    start_date_start: Mapped[Date] = mapped_column(DateTime)
    end_date: Mapped[Date] = mapped_column(DateTime)
    address: Mapped[str] = mapped_column(Text)
    attendees: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str] = mapped_column(Text)

    contract_id: Mapped[int] = mapped_column(
        ForeignKey("contract.id", ondelete="CASCADE")
    )
    contract: Mapped[list["Contract"]] = relationship(
        "Contract",
        back_populates="commercial",
        cascade="all, delete",
        passive_deletes=True,
    )

    # client_id = mapped_column(ForeignKey("client.id"))
    # client = relationship("Client", back_populates="events")

    # support_contact_id = mapped_column(
    #     ForeignKey("employee.id"), nullable=True, default=None
    # )
    # support_contact = relationship("employee", back_populates="events")

    # def __repr__(self) -> str:
    #     return f"Event(id={self.id!r}, name={self.name!r})"
