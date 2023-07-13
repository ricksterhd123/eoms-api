import os
import psycopg2
from models.customer import list_customers
from fastapi import FastAPI

DATABASE_NAME = "eoms"
DATABASE_USER = os.environ.get("DATABASE_USER", "postgres")
DATABASE_PASS = os.environ.get("DATABASE_PASS", "example")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "127.0.0.1")

app = FastAPI()
db_connection = psycopg2.connect(
    database=DATABASE_NAME, 
    user=DATABASE_USER, 
    password=DATABASE_PASS, 
    host=DATABASE_HOST
)

@app.get("/customers")
def get_customers():
    return list_customers(db_connection)

# @app.get("/orders")
# def get_orders():
#     return [{"test": True}]
