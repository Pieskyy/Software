import sqlite3 as sql

def listExtension():
    con = sql.connect("database/cards.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM cards").fetchall()  # <-- change to your actual table name
    con.close()
    return data
