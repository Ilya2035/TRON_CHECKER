from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class RequestsToTron(Base):
    __tablename__ = "requests_to_tron"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tron_address: Mapped[str] = mapped_column(String(300), nullable=False)
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
            f"request_time={self.request_time}"
            f")>"
        )
