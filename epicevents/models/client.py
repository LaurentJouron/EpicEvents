from ..database import Model, Session

from datetime import date
from typing import List
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.types import Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient


class ClientManager:
    # CRUD
    def create(self, **kwargs):
        with Session() as session:
            with session.begin():
                new_client = Client(
                    compagny_name=kwargs["compagny_name"],
                    username=kwargs["username"],
                    last_name=kwargs["last_name"],
                    email=kwargs["email"],
                    phone=kwargs["phone"],
                    address=kwargs["address"],
                    information=kwargs["information"],
                    creation_date=date.today(),
                    updating_date=date.today(),
                    employee_id=kwargs["employee_id"],
                )
                session.add(new_client)

    def read(self):
        with Session() as session:
            with session.begin():
                clients = session.query(Client).all()
                for client in clients:
                    session.expunge(client)
                    make_transient(client)
                return clients

    def update(self, client_id, **kwargs):
        with Session() as session:
            with session.begin():
                if client := session.query(Client).get(client_id):
                    if kwargs["compagny_name"] != client.compagny_name:
                        client.compagny_name = kwargs["compagny_name"]
                    if kwargs["username"] != client.compagny_name:
                        client.username = kwargs["username"]
                    if kwargs["last_name"] != client.last_name:
                        client.last_name = kwargs["last_name"]
                    if kwargs["email"] != client.email:
                        client.email = kwargs["email"]
                    if kwargs["phone"] != client.phone:
                        client.phone = kwargs["phone"]
                    if kwargs["address"] != client.address:
                        client.address = kwargs["address"]
                    if kwargs["information"] != client.information:
                        client.information = kwargs["information"]
                    client.updating_date = date.today()

    def delete(self, client_id):
        with Session() as session:
            with session.begin():
                if client := session.query(Client).get(client_id):
                    session.delete(client)
                    return True
                else:
                    return False

    # REQUESTS
    def get_by_id(self, client_id):
        with Session() as session:
            with session.begin():
                client = (
                    session.query(Client)
                    .filter(Client.id == client_id)
                    .first()
                )
                if client:
                    session.expunge(client)
                    make_transient(client)
                return client


# MODELS
class Client(Model):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    compagny_name: Mapped[str] = mapped_column(String(300), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(
        String(300), unique=True, nullable=False
    )
    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    address: Mapped[Text] = mapped_column(Text, nullable=False)
    information: Mapped[str] = mapped_column(Text)

    creation_date: Mapped[Date] = mapped_column(Date)
    updating_date: Mapped[Date] = mapped_column(Date, nullable=True)

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employee.id"), nullable=True
    )
    employee: Mapped["Employee"] = relationship(back_populates="client")

    event: Mapped[List["Event"]] = relationship(back_populates="client")
