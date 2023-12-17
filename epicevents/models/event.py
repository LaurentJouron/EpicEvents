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
    start_date_start: Mapped[Date] = mapped_column(Date)
    end_date: Mapped[Date] = mapped_column(Date)
    address: Mapped[str] = mapped_column(Text)
    attendees: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str] = mapped_column(Text)

    client_id: Mapped[int] = mapped_column(
        ForeignKey("client.id", ondelete="CASCADE")
    )
    client: Mapped["Client"] = relationship("Client", back_populates="events")

    commercial_id: Mapped[int] = mapped_column(
        ForeignKey("employee.id", ondelete="CASCADE")
    )
    commercial: Mapped["Employee"] = relationship(
        "Employee", back_populates="events"
    )

    technician_id: Mapped[int] = mapped_column(
        ForeignKey("employee.id", ondelete="CASCADE")
    )
    technician: Mapped["Employee"] = relationship(
        "Employee", back_populates="events"
    )

    contract: Mapped["Event"] = relationship(
        "Contract",
        back_populates="events",
        cascade="all, delete",
        passive_deletes=True,
    )

    def __repr__(self):
        return (
            f"Event(id:{self.id}"
            f"start_date_start: {self.start_date_start}"
            f"end_date: {self.end_date}"
            f"address: {self.address}"
            f"attendees : {self.attendees!r}"
            f"notes : {self.notes!r}"
            f"client : {self.client!r}"
            f"commercial : {self.commercial.fullname!r})"
            f"technician : {self.technician.fullname!r})"
            f"contract : {self.contract.date_creation!r})"
        )
