from ..database import Model, Session

from sqlalchemy import ForeignKey, Date, Text, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient


class EventManager:
    # CRUD
    """Manager for handling events."""

    def create(self, **kwargs):
        """
        Create a new event.

        Args:
            **kwargs: Keyword arguments for the event attributes.

        Returns:
            The ID of the created event.
        """
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
        """
        Read all events.

        Returns:
            The list of events.
        """
        with Session() as session:
            with session.begin():
                events = session.query(Event).all()
                for event in events:
                    session.expunge(event)
                    make_transient(event)
                return events

    def update(self, event_id, **kwargs):
        """
        Update an event.

        Args:
            event_id: The ID of the event to update.
            **kwargs: Keyword arguments for the event attributes to update.
        """
        with Session() as session:
            with session.begin():
                if event := session.query(Event).get(event_id):
                    if kwargs["name"] not in [event.name, ""]:
                        event.name = kwargs["name"]
                    if kwargs["start_date"] not in [event.start_date, ""]:
                        event.start_date = kwargs["start_date"]
                    if kwargs["end_date"] not in [event.end_date, ""]:
                        event.end_date = kwargs["end_date"]
                    if kwargs["address"] not in [event.address, ""]:
                        event.address = kwargs["address"]
                    if kwargs["attendees"] not in [event.attendees, ""]:
                        event.attendees = kwargs["attendees"]
                    if kwargs["notes"] not in [event.notes, ""]:
                        event.notes = kwargs["notes"]
                    if kwargs["client_id"] not in [event.client_id, ""]:
                        event.notes = kwargs["client_id"]
                    if kwargs["contract_id"] not in [event.notes, ""]:
                        event.notes = kwargs["contract_id"]

    def delete(self, event_id):
        """
        Delete an event.

        Args:
            event_id: The ID of the event to delete.

        Returns:
            True if the event was deleted successfully, False otherwise.
        """
        with Session() as session:
            with session.begin():
                if event := session.query(Event).get(event_id):
                    session.delete(event)
                    return True
                else:
                    return False

    # REQUESTS
    def get_by_id(self, event_id):
        """
        Get an event by its ID.

        Args:
            event_id: The ID of the event to retrieve.

        Returns:
            The event object.
        """
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
    """
    Model representing an event.

    Args:
        id (int): The ID of the event.
        name (str): The name of the event.
        start_date (datetime.date): The start date of the event.
        end_date (datetime.date): The end date of the event.
        address (str): The address of the event.
        attendees (int): The number of attendees for the event.
        notes (str): Additional notes for the event.
        client_id (int): The ID of the client associated with the event.
        client (Client): The client object associated with the event.
        contract_id (int): The ID of the contract associated with the event.
        contract (Contract): The contract object associated with the event.
    """

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
