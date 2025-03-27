from typing import Optional
from datetime import datetime

from sqlalchemy import String, Numeric, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class RequestsToTron(Base):
    __tablename__ = "requests_to_tron"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tron_address: Mapped[str] = mapped_column(String(300), nullable=False)
    balance_trx: Mapped[Optional[float]] = mapped_column(Numeric(18, 6), nullable=True)
    bandwidth: Mapped[Optional[int]] = mapped_column(Numeric(20, 0), nullable=True)
    energy: Mapped[Optional[int]] = mapped_column(Numeric(20, 0), nullable=True)
    request_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    def __repr__(self) -> str:
        return (
            f"<RequestsToTron("
            f"id={self.id}, "
            f"tron_address='{self.tron_address}', "
            f"balance_trx={self.balance_trx}, "
            f"bandwidth={self.bandwidth}, "
            f"energy={self.energy}, "
            f"request_time={self.request_time}"
            f")>"
        )
