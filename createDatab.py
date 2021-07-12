import sqlite3
import datetime
from pprint import pprint


def _createDatabase():
    conn = sqlite3.connect("customers.db")
    c = conn.cursor()
    c.execute(
        """ CREATE TABLE IF NOT EXISTS customer (
    first text,
    last text,
    sex text,
    age integer,
    vaccine text,
    state text,
    dateT date,
    time text
    )
    """
    )
    conn.commit()
    conn.close()


def insertData(first, last, gender, age, vaccine, state, date, time):
    _createDatabase()
    conn = sqlite3.connect("customers.db")

    c = conn.cursor()
    c.execute(
        "INSERT INTO customer VALUES(?,?,?,?,?,?,?,?)",
        (first, last, gender, age, vaccine, state, date, time),
    )
    conn.commit()
    conn.close()


def updateData(first, last, gender, age, vaccine, state, date, time):
    _createDatabase()
    conn = sqlite3.connect("customers.db")

    c = conn.cursor()
    q = "UPDATE customer SET  last = ?, sex = ?, age = ?, vaccine = ?, state = ?, dateT = ?, time = ? WHERE first = ?"
    c.execute(q, (last, gender, age, vaccine, state, date, time, first))
    conn.commit()
    conn.close()


def showTable(name):
    conn = sqlite3.connect("customers.db")
    c = conn.cursor()
    c.execute("SELECT * FROM customer where first=?", (name,))
    data = c.fetchone()
    conn.commit()
    conn.close()
    if data:
        return data



