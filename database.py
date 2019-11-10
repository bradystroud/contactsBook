#database stuff

import sqlite3


# CREATES SQL TABLE IF NOT ALREADY CREATED
def sql_table(con, cursorObj):
    cursorObj = con.cursor()
    cursorObj.execute(""" 
    CREATE TABLE if not exists contacts(
        cID INTEGER PRIMARY KEY,
        fname TEXT,
        lname TEXT,
        phone TEXT,
        email TEXT
    )
    """)
 
    con.commit()


# INITIALISES DATABASE VARIABLES

con = sqlite3.connect('contacts.db')
cursorObj = con.cursor()
sql_table(con, cursorObj)
