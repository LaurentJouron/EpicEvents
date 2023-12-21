from sqlalchemy import String, ForeignKey, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model, Session


class ClientManager:
    def create_client(self, **kwargs):
        with Session() as session:
            with session.begin():
                new_client = Client(
                    compagny_name=kwargs["compagny_name"],
                    information=kwargs["information"],
                    username=kwargs["username"],
                    last_name=kwargs["last_name"],
                    email=kwargs["email"],
                    phone=kwargs["phone"],
                    creation_date=kwargs["creation_date"],
                    updating_date=kwargs["updating_date"],
                    address=kwargs["address"],
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
                session.query(Client).filter_by(username=username).first()

    def get_client_by_email(self, email):
        with Session() as session:
            with session.begin():
                session.query(Client).filter_by(email=email).first()

    def get_client_by_phone(self, phone):
        with Session() as session:
            with session.begin():
                session.query(Client).filter_by(phone=phone).first()

    def get_all_client(self):
        with Session() as session:
            return session.query(Client).all()


class Client(Model):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    compagny_name: Mapped[str] = mapped_column(String(300))
    information: Mapped[str] = mapped_column(Text)
    username: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(300), unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    creation_date: Mapped[Date] = mapped_column(Date)
    updating_date: Mapped[Date] = mapped_column(Date)
    address: Mapped[Text] = mapped_column(Text)

    commercial_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    commercial: Mapped[list["Employee"]] = relationship(
        "Employee", back_populates="client"
    )

    event: Mapped[list["Event"]] = relationship(
        "Event", back_populates="client"
    )

    def __repr__(self):
        return (
            f"Client(id:{self.id}"
            f"username: {self.username}"
            f"email: {self.email}"
            f"phone: {self.phone}"
            f"compagny_name : {self.compagny_name!r}"
            f"creation_date : {self.creation_date!r}"
            f"updating_date : {self.updating_date!r}"
            f"commercial : {self.commercial.username!r})"
        )
