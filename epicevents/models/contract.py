from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from epicevents.database import Model, Session


class ContractManager:
    def add_contract(self, **kwargs):
        with Session() as session:
            with session.begin():
                new_contract = Contract(
                    total_amount=kwargs["total_amount"],
                    outstanding_amount=kwargs["outstanding_amount"],
                    date_creation=kwargs["date_creation"],
                    status=kwargs["status"],
                    gestion_id=kwargs["gestion_id"],
                    event_id=kwargs["event_id"],
                )
                session.add(new_contract)

    def get_contract_by_id(self, contract_id):
        with Session() as session:
            with session.begin():
                return (
                    session.query(Contract)
                    .filter(Contract.id == contract_id)
                    .first()
                )

    def get_all_contract(self):
        with Session() as session:
            with session.begin():
                return session.query(Contract).all()


class Contract(Model):
    __tablename__ = "contract"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    total_amount: Mapped[str] = mapped_column(String(50))
    outstanding_amount: Mapped[str] = mapped_column(String(50))
    date_creation: Mapped[Date] = mapped_column(Date)
    status: Mapped[bool] = mapped_column(default=False)

    gestion_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    gestion: Mapped[list["Employee"]] = relationship(
        "Employee", back_populates="contract"
    )

    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    event: Mapped["Contract"] = relationship(
        "Contract", back_populates="event"
    )

    def __repr__(self):
        return (
            f"Contract(id:{self.id}"
            f"total_amount: {self.total_amount}"
            f"outstanding_amount: {self.outstanding_amount}"
            f"date_creation: {self.date_creation}"
            f"status : {self.status}"
            f"event_start_date : {self.event.start_date!r}"
        )
