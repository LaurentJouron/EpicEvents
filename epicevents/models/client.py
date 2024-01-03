from datetime import datetime
from sqlalchemy import String, ForeignKey, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from ..database import Model, Session


class ClientManager:
    def create_client(self, **kwargs):
        with Session() as session:
            with session.begin():
                if "id" in kwargs:
                    client = session.query(Client).get(kwargs["id"])
                    if client:
                        for key, value in kwargs.items():
                            setattr(client, key, value)
                        client.updating_date = datetime.now()
                else:
                    new_client = Client(
                        compagny_name=kwargs["compagny_name"],
                        username=kwargs["username"],
                        last_name=kwargs["last_name"],
                        email=kwargs["email"],
                        phone=kwargs["phone"],
                        address=kwargs["address"],
                        information=kwargs["information"],
                    )
                    session.add(new_client)

    def get_client_by_id(self, client_id):
        with Session() as session:
            with session.begin():
                return session.query(Client).filter_by(id=client_id).first()

    def get_client_by_compagny_name(self, compagny_name):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Client)
                    .filter_by(compagny_name=compagny_name)
                    .first()
                )

    def get_client_by_username(self, username):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Client).filter_by(username=username).first()
                )

    def get_client_by_email(self, email):
        with Session() as session:
            with session.begin():
                return session.query(Client).filter_by(email=email).first()

    def get_client_by_phone(self, phone):
        with Session() as session:
            with session.begin():
                session.query(Client).filter_by(phone=phone).first()

    def get_all_client(self):
        with Session() as session:
            return session.query(Client).all()


class Client(Model):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    compagny_name: Mapped[str] = mapped_column(String(300))
    username: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(300), unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    address: Mapped[Text] = mapped_column(Text)
    information: Mapped[str] = mapped_column(Text)
    creation_date: Mapped[Date] = mapped_column(Date)
    updating_date: Mapped[Date] = mapped_column(Date)

    commercial_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    commercial: Mapped["Employee"] = relationship(back_populates="client")

    event: Mapped[List["Event"]] = relationship(back_populates="client")
