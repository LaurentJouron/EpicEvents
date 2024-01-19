from ..database import Model, Session

from datetime import date
from typing import List
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.types import Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.session import make_transient


class ClientManager:
    def create_client(self, **kwargs):
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
                    commercial_id=kwargs["commercial_id"],
                )
                session.add(new_client)

    def update_client(self, client_id, **kwargs):
        with Session() as session:
            with session.begin():
                client = session.query(Client).get(client_id)
                if client:
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

    def get_client_compagny_name_by_id(self, client_id):
        with Session() as session:
            with session.begin():
                client = session.query(Client).get(client_id)
                if client:
                    return client.username
                return None

    def get_client_id_by_compagny_name(self, compagny_name):
        with Session() as session:
            with session.begin():
                client = (
                    session.query(Client)
                    .filter_by(compagny_name=compagny_name)
                    .first()
                )
                if client:
                    return client.id
                return None

    def get_client_by_username(self, username):
        with Session() as session:
            with session.begin():
                return session.query(Client).filter_by(username=username)

    def get_client_by_email(self, email):
        with Session() as session:
            with session.begin():
                client = session.query(Client).get(email=email)
                if client:
                    return client.id
                return None

    def get_client_by_phone(self, phone):
        with Session() as session:
            with session.begin():
                client = session.query(Client).get(phone=phone)
                if client:
                    return client.id
                return None

    def get_all_client(self):
        with Session() as session:
            with session.begin():
                clients = session.query(Client).all()
                for client in clients:
                    session.expunge(client)
                    make_transient(client)
                return clients

    def delete_client(self, client_id):
        with Session() as session:
            with session.begin():
                client = session.query(Client).get(client_id)
                if client:
                    session.delete(client)
                    return True
                else:
                    return False


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

    commercial_id: Mapped[int] = mapped_column(
        ForeignKey("employee.id"), nullable=True
    )
    commercial: Mapped["Employee"] = relationship(back_populates="client")

    event: Mapped[List["Event"]] = relationship(back_populates="client")
