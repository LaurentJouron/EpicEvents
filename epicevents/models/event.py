from ..database import Model, Session

from sqlalchemy import ForeignKey, Date, Text, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient


class EventManager:
    # CRUD
    def create(self, **kwargs):
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
                    contract_id=kwargs["contract_id"],
                )
                session.add(new_event)
            return new_event.id

    def read(self):
        with Session() as session:
            with session.begin():
                events = session.query(Event).all()
                for event in events:
                    session.expunge(event)
                    make_transient(event)
                return events

    def update(self, event_id, **kwargs):
        with Session() as session:
            with session.begin():
                if event := session.query(Event).get(event_id):
                    if kwargs["name"] != event.name and kwargs["name"] != "":
                        event.name = kwargs["name"]
                    if (
                        kwargs["start_date"] != event.start_date
                        and kwargs["start_date"] != ""
                    ):
                        event.start_date = kwargs["start_date"]
                    if (
                        kwargs["end_date"] != event.end_date
                        and kwargs["end_date"] != ""
                    ):
                        event.end_date = kwargs["end_date"]
                    if (
                        kwargs["address"] != event.address
                        and kwargs["address"] != ""
                    ):
                        event.address = kwargs["address"]
                    if (
                        kwargs["attendees"] != event.attendees
                        and kwargs["attendees"] != ""
                    ):
                        event.attendees = kwargs["attendees"]
                    if (
                        kwargs["notes"] != event.notes
                        and kwargs["notes"] != ""
                    ):
                        event.notes = kwargs["notes"]
                    if (
                        kwargs["client_id"] != event.client_id
                        and kwargs["client_id"] != ""
                    ):
                        event.notes = kwargs["client_id"]
                    if (
                        kwargs["contract_id"] != event.notes
                        and kwargs["contract_id"] != ""
                    ):
                        event.notes = kwargs["contract_id"]

    def delete(self, event_id):
        with Session() as session:
            with session.begin():
                if event := session.query(Event).get(event_id):
                    session.delete(event)
                    return True
                else:
                    return False

    # REQUESTS
    def get_by_id(self, event_id):
        with Session() as session:
            with session.begin():
                event = (
                    session.query(Event).filter(Event.id == event_id).first()
                )
                if event:
                    session.expunge(event)
                    make_transient(event)
                return event


# MODELS
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
