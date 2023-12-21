from sqlalchemy import ForeignKey, Date, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model, Session


class EventManager:
    def add_event(self, **kwargs):
        with Session() as session:
            with session.begin():
                new_event = Event(
                    start_date=kwargs["start_date"],
                    end_date=kwargs["end_date"],
                    address=kwargs["address"],
                    attendees=kwargs["attendees"],
                    notes=kwargs["notes"],
                    client_id=kwargs["client_id"],
                    commercial_id=kwargs["commercial_id"],
                    support_id=kwargs["support_id"],
                    contract_id=kwargs["contract_id"],
                )
                session.add(new_event)

    def get_event_by_start_date(self, start_date):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Event)
                    .filter_by(start_date=start_date)
                    .first()
                )

    def get_event_by_id(self, event_id):
        with Session() as session:
            with session.begin():
                return session.query(Event).get(event_id)

    def get_all_event(self):
        with Session() as session:
            return session.query(Event).all()


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
