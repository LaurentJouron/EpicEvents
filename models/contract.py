from typing import Optional
from click import DateTime
from sqlalchemy import String, Text, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from EpicEvents.database import Model
from .event import Event


class Contract(Model):
    _tablename_ = "contract"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    total_amount: Mapped[str] = mapped_column(String(50))
    outstanding_amount: Mapped[str] = mapped_column(String(50))
    date_creation: Mapped[Date] = mapped_column(DateTime)
    status: Mapped[bool] = mapped_column(defaut=False)

    # event: Mapped["Event"] = relationship(back_populates="contract")

    # def __repr__(self) -> str:
    #     return f"Contract(id={self.id!r}, client.fullname={self.client.fullname!r}), event={self.event!r})"
