import sqlite3
from flask import g
import os
DATABASE = os.path.join('database', 'cards.db') # My database

def get_db(): # Database connection
    if not hasattr(g, "db"):
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row # to access columns by name
    return g.db

def get_table_name(): # getting the table names
    connection = get_db() # Open the database
    result = connection.execute( # Get all table names in the database
        "SELECT name FROM sqlite_master WHERE type='table';"
    ).fetchall()

    if len(result) == 0: # If there are no tables, give an error
        raise Exception("Your database has no tables.")
    
    first_table_name = result[0][0]# Return the name of the first table
    return first_table_name
