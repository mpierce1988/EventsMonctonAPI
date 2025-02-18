from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Event(Base):
    __tablename__ = "event"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    datetime: Mapped[DateTime] = mapped_column(DateTime)
    type: Mapped[str] = mapped_column(String(128))
    information: Mapped[str] = mapped_column(String)
    venue: Mapped[str] = mapped_column(String)
    cost: Mapped[Optional[str]]
    link_type: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)
