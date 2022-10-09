# # Without using Async, await
# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
from datetime import *
# Code with Async,Await included, We will discuss this in some other article
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return None
#import os
#import requests

app = FastAPI()

conn = None

@app.on_event("startup")
async def startup_event():
    sql_create_depots_table = """CREATE TABLE IF NOT EXISTS depots (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        distance float,
                                        travel_time integer NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""

    sql_create_queues_table = """CREATE TABLE IF NOT EXISTS queues (
                                        id integer PRIMARY KEY,
                                        queue_time integer NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES depots (id)
                                    );"""

    conn = create_connection("sqlite\db\pythonsqlite.db")

    if conn is not None:
        create_table(conn, sql_create_depots_table)
        create_table(conn, sql_create_queues_table)
    else:
        print("Error! cannot create the database connection.")


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


class Queue(BaseModel):
    id:int
    queue_time:int


class Depo(BaseModel):
    id:int
    name:str
    distance:float
    travel_time:int
    queues:tuple


queue = Queue(id=0, queue_time=5)

depos = [Depo(
        id=0,
        name="g",
        distance=1.5,
        travel_time=6,
        queues=(Queue(id=0, queue_time=5),Queue(id=1, queue_time=9))),
        Depo(
        id=1,
        name="h",
        distance=2.5,
        travel_time=10,
        queues=(Queue(id=0, queue_time=5),Queue(id=1, queue_time=9)))
    ]


@app.get("/depos")
async def get_depos():
    cur = conn.cursor()
    cur.execute("SELECT * FROM depots")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    conn.close()
    return depos


class Flight(BaseModel):
    id:int
    date:date
    cost:float


class Flight_History(BaseModel):
    id:int
    flights:tuple


flight_hist = Flight_History(
    id='0',
    flights = [
        Flight(
            id='0',
            date='2022-09-10',
            cost=249.99
        ),
        Flight(
            id='0',
            date='2022-09-10',
            cost=125.99
        ),
        Flight(
            id='0',
            date='2022-09-10',
            cost=100.00
        )
    ]
)

@app.get("/flight_hist")
async def get_flight_hist():
    discount = 0.1
    total = 0
    for flight in flight_hist.flights:
        total += flight.cost
    return total * discount





