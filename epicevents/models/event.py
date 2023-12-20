from sqlalchemy import ForeignKey, Date, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model, Session


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
    start_date: Mapped[Date] = mapped_column(Date)
    end_date: Mapped[Date] = mapped_column(Date)
    address: Mapped[str] = mapped_column(Text)
    attendees: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str] = mapped_column(Text)

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    client: Mapped["Client"] = relationship("Client", back_populates="event")

    commercial_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    commercial: Mapped["Employee"] = relationship(
        "Employee", back_populates="event"
    )

    support_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    support: Mapped["Employee"] = relationship(
        "Employee", back_populates="event"
    )

    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id"))
    contract: Mapped["Event"] = relationship(
        "Event", back_populates="contract"
    )

    def __repr__(self):
        return (
            f"Event(id:{self.id}"
            f"start_date: {self.start_date}"
            f"end_date: {self.end_date}"
            f"address: {self.address}"
            f"attendees : {self.attendees!r}"
            f"notes : {self.notes!r}"
            f"client : {self.client!r}"
            f"commercial : {self.commercial.username!r})"
            f"technician : {self.technician.username!r})"
            f"contract : {self.contract.date_creation!r})"
        )
