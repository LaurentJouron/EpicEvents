from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from epicevents.database import Model, Session


class EmployeeManager:
    def add_employee(self, **kwargs):
        with Session() as session:
            with session.begin():
                new_employee = Employee(
                    username=kwargs["username"],
                    last_name=kwargs["last_name"],
                    email=kwargs["email"],
                    phone=kwargs["phone"],
                    password=kwargs["password"],
                )
                session.add(new_employee)

    def get_employee_by_username(self, username):
        with Session() as session:
            with session.begin():
                session.query(Employee).filter_by(username=username)

    def get_employee_by_id(self, id):
        with Session() as session:
            with session.begin():
                session.query(Employee).filter_by(id=id)

    def get_employee_by_email(self, email):
        with Session() as session:
            with session.begin():
                session.query(Employee).filter_by(email=email)

    def get_all_employee(self):
        with Session() as session:
            with session.begin():
                return session.query(Employee).all()

    def delete_employee(self, username, email):
        with Session() as session:
            with session.begin():
                session.delete(username=username, email=email)

    def login(self, username, password):
        with Session() as session:
            with session.begin():
                session.query(Employee).filter_by(
                    username=username, password=password
                )


class Employee(Model):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(300), unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(500))

    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))
    role: Mapped[list["Role"]] = relationship(
        "Role", back_populates="employee"
    )

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    client: Mapped[list["Client"]] = relationship(
        "Client", back_populates="employee"
    )

    commercial_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    commercial: Mapped[list["Event"]] = relationship(
        "Event", back_populates="employee"
    )

    support_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    support: Mapped[list["Event"]] = relationship(
        "Event", back_populates="employee"
    )

    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id"))
    contract: Mapped[list["Contract"]] = relationship(
        "Contract", back_populates="employee"
    )

    @hybrid_property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return (
            f"Employee(id:{self.id}, "
            f"username: {self.username}, "
            f"last_name: {self.last_name}, "
            f"email: {self.email}, "
            f"phone: {self.phone}, "
            f"password: {self.password}, "
            f"role: {self.role}, "
            f"client: {self.client.compagny_name!r}, "
            f"support: {self.support!r}, "
            f"commercial: {self.commercial!r})"
        )
