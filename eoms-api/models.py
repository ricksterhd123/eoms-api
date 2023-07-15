from datetime import datetime
from sqlalchemy import Integer, Numeric, Text, Time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    sku: Mapped[str] = mapped_column(Text())
    reference: Mapped[str] = mapped_column(Text())
    description: Mapped[str] = mapped_column(Text())
    unit_price: Mapped[float] = mapped_column(Numeric())
    stock_quantity: Mapped[int] = mapped_column(Integer())
    updated_on: Mapped[datetime] = mapped_column(Time())
    created_on: Mapped[datetime] = mapped_column(Time())

    def __repr__(self):
        return f"Item(id={self.id!r}, sku={self.sku!r}, description={self.description!r})"

class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    reference: Mapped[str] = mapped_column(Text())
    name: Mapped[str] = mapped_column(Text())
    email_address: Mapped[str] = mapped_column(Text())
    updated_on: Mapped[datetime] = mapped_column(Time())
    created_on: Mapped[datetime] = mapped_column(Time())

    def __repr__(self):
        return f"Customer(id={self.id!r}, name={self.name!r}, email_address={self.email_address!r})"
