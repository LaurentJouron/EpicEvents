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
                    creation_date=kwargs["creation_date"],
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
    name: Mapped[str] = mapped_column(String(50))
    total_amount: Mapped[str] = mapped_column(String(50))
    outstanding_amount: Mapped[str] = mapped_column(String(50))
    creation_date: Mapped[Date] = mapped_column(Date)
    status: Mapped[bool] = mapped_column(default=False)

    gestion_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    gestion: Mapped["Employee"] = relationship(back_populates="gestion")

    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    event: Mapped["Event"] = relationship(
        back_populates="contracts", single_parent=True
    )

    def __repr__(self):
        return (
            f"Contract(id:{self.id}"
            f"name: {self.name}"
            f"total_amount: {self.total_amount}"
            f"outstanding_amount: {self.outstanding_amount}"
            f"creation_date: {self.creation_date}"
            f"status : {self.status}"
            f"event_start_date : {self.event.start_date!r}"
        )
