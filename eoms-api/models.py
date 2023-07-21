from datetime import datetime
from sqlalchemy import Integer, Numeric, Text, Time, ForeignKey
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
        return f"Item(id={self.id!r}, sku={self.sku!r}, reference={self.reference!r}, description={self.description!r}, unit_price={self.unit_price!r}, stock_quantity={self.stock_quantity!r}, updated_on={self.updated_on!r}, created_on={self.created_on!r})"

class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    reference: Mapped[str] = mapped_column(Text())
    name: Mapped[str] = mapped_column(Text())
    email_address: Mapped[str] = mapped_column(Text())
    updated_on: Mapped[datetime] = mapped_column(Time())
    created_on: Mapped[datetime] = mapped_column(Time())

    def __repr__(self):
        return f"Customer(id={self.id!r}, reference={self.reference!r}, name={self.name!r}, email_address={self.email_address!r}, updated_on={self.updated_on!r}, created_on={self.updated_on!r})"

class OrderItem(Base):
    __tablename__ = "order_item"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"))
    updated_on: Mapped[datetime] = mapped_column(Time())
    created_on: Mapped[datetime] = mapped_column(Time())

    def __repr__(self):
        return f"OrderItem(id={self.id!r}, order_id={self.order_id!r}, item_id={self.item_id!r}, updated_on={self.updated_on!r}, created_on={self.created_on!r})"

class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    reference: Mapped[str] = mapped_column(Text())
    status: Mapped[str] = mapped_column(Text())
    updated_on: Mapped[datetime] = mapped_column(Time())
    created_on: Mapped[datetime] = mapped_column(Time())

    def __repr__(self):
        return f"Order(id={self.id!r}, customer_id={self.item_id!r}, reference={self.updated_on!r}, status={self.created_on!r}, updated_on={self.updated_on!r}, created_on={self.created_on!r})"
