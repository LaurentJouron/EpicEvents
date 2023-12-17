from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model, Session

class ContractManager:
    def add_contract(self):
        with Session() as session:
            with session.begin():
                ...

    def get_contract_by_creation_date(self):
        with Session() as session:
            with session.begin():
                ...

    def get_contract_by_id(self):
        with Session() as session:
            with session.begin():
                ...

    def get_all_contract(self):
        with Session() as session:
            with session.begin():
                ...


class Contract(Model):
    __tablename__ = "contract"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    total_amount: Mapped[str] = mapped_column(String(50))
    outstanding_amount: Mapped[str] = mapped_column(String(50))
    date_creation: Mapped[Date] = mapped_column(Date)
    status: Mapped[bool] = mapped_column(default=False)

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
