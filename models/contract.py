from epicevents.database import Session
from click import DateTime
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model
from .event import Event


class EmployeeManager:
    def add_employee(self):
        with Session() as session:
            with session.begin():
                ...

    def get_employee_by_name(self):
        with Session() as session:
            with session.begin():
                ...

    def get_employee_by_id(self):
        with Session() as session:
            with session.begin():
                ...

    def get_all_employee(self):
        with Session() as session:
            with session.begin():
                ...


class Contract(Model):
    __tablename__ = "contract"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    total_amount: Mapped[str] = mapped_column(String(50))
    outstanding_amount: Mapped[str] = mapped_column(String(50))
    date_creation: Mapped[Date] = mapped_column(DateTime)
    status: Mapped[bool] = mapped_column(defaut=False)

    event: Mapped["Event"] = relationship(back_populates="contract")

    def __repr__(self):
        return (
            f"Contract(id:{self.id}"
            f"total_amount: {self.total_amount}"
            f"outstanding_amount: {self.outstanding_amount}"
            f"date_creation: {self.date_creation}"
            f"status : {self.status}"
            f"event : {self.event!r}"
        )
