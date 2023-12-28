from sqlalchemy import String, ForeignKey, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from epicevents.database import Model, Session


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
                    creation_date=kwargs["creation_date"],
                    updating_date=kwargs["updating_date"],
                )
                session.add(new_client)

    def update_client(self, client_id, **kwargs):
        with Session() as session:
            with session.begin():
                client_to_update = session.query(Client).get(client_id)
                if client_to_update:
                    for key, value in kwargs.items():
                        setattr(client_to_update, key, value)

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
    commercial: Mapped["Employee"] = relationship(back_populates="commercial")
    event: Mapped[List["Event"]] = relationship(back_populates="client")

    def __repr__(self):
        return (
            f"Client(id:{self.id}"
            f"compagny_name : {self.compagny_name!r}"
            f"username: {self.username} {self.last_name}"
            f"email: {self.email}"
            f"phone: {self.phone}"
            f"address: {self.address}"
            f"information: {self.information}"
            f"creation_date : {self.creation_date!r}"
            f"updating_date : {self.updating_date!r}"
            f"commercial : {self.commercial.username!r})"
        )
