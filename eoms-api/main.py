import os
from models import Base, Customer, Item
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from fastapi import FastAPI

DATABASE_NAME = "eoms"
DATABASE_USER = os.environ.get("DATABASE_USER", "postgres")
DATABASE_PASS = os.environ.get("DATABASE_PASS", "example")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "127.0.0.1")

engine = create_engine(f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}")
Base.metadata.create_all(engine)
conn = engine.connect()
app = FastAPI()

@app.get("/customers")
def get_customers(limit: int = 10, offset: int = 0):
    stmt = select(Customer).limit(limit).offset(offset)
    session = Session(conn)
    result = session.execute(stmt)
    return { "customers": result.scalars().all() }

@app.get("/items")
def get_items(limit: int = 10, offset: int = 0):
    stmt = select(Item).limit(limit).offset(offset)
    session = Session(conn)
    result = session.execute(stmt)
    return { "items": result.scalars().all() }
