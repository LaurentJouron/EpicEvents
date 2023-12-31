from sqlalchemy import ForeignKey, Date, Text, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Model, Session


class EventManager:
    def add_event(self, **kwargs):
        with Session() as session:
            with session.begin():
                new_event = Event(
                    name=kwargs["name"],
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
                    .filter(Event.start_date == start_date)
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
    name: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[Date] = mapped_column(Date)
    end_date: Mapped[Date] = mapped_column(Date)
    address: Mapped[str] = mapped_column(Text)
    attendees: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str] = mapped_column(Text)

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    client: Mapped["Client"] = relationship(back_populates="event")

    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id"))
    contract: Mapped["Contract"] = relationship(back_populates="event")
