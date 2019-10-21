import sqlite3
from sqlite3 import Error

con = sqlite3.connect('contacts.db')
cursorObj = con.cursor()


def sql_connection():
    try:
        con = sqlite3.connect('contacts.db')
        print("Connection is established: Database is created on path")
        return con
    except Error:
        print(Error)
 
sql_connection()
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(''' CREATE TABLE if not exists contacts(
                                     cID INTEGER PRIMARY KEY,
                                     fname TEXT,
                                     lname TEXT,
                                     phone TEXT,
                                     email TEXT
                                 )''')
 
    con.commit()
con = sql_connection()





def main(con):

    def add_contact(con):
        fname = input("enter first name: ")
        lname = input("enter last name: ")
        phone = input("enter number: ")
        email = input("enter email: ")

        cursorObj.execute(""" INSERT INTO contacts
                                (
                                    fname, lname, phone, email
                                )
                                VALUES
                                (
                                    ?,?,?,?
                                ); """, (fname, lname, phone, email))
        con = sql_connection()
        con.commit()
        print("contact "+fname+" "+lname+" added")

        cursorObj.execute("SELECT * FROM contacts")
        rows = cursorObj.fetchall()
        for row in rows:
            print(row)
        con.commit()
        q = input("add another?(y/n): ")
        if q == "y":
            add_contact(con)
        else:
            con.commit()
            main(con)

    def ls():
        cursorObj.execute("SELECT * FROM contacts")
        rows = cursorObj.fetchall()
        for row in rows:
            print(row)
        input("Press Enter to continue...")
        main(con)

    def update():
        upcon = int(input("which contact to update?(enter first name): "))
        cursorObj.execute("SELECT fname, lname FROM contacts WHERE cID = ?;"), (upcon)
        rows = cursorObj.fetchall()
        for row in rows:
            deta = input("which detail would you like to change for "+str(row)+"?: ")
        cursorObj.execute("UPDATE")


        


    def norm_cmd():
        if cmd == "a":
            add_contact(con)
        # elif cmd == "s":
        #     search()
        elif cmd == "u":
            update()
        # elif cmd == "d":
        #     delete()
        elif cmd == "ls":
            ls()
        else:
            print()
            print("Hmmm... that doesn't seem like a command, enter 'help' to see all commands")
            main(con)

    



    cmd = input("enter command letter: ")
    if cmd == "help":
        help()
    else:
        norm_cmd()


def help():
    print("Type 'a' for instructions")
    print("Type 's' to search for a contact")
    print("Type 'ls' to list all contacts")
    print("Type 'd' to delete a contact")
    input("Press Enter to continue...")
    print()
    print()
    main(con)


def one():
    c="_"
    c=c.center(10)
    print(c*54)
    print("Welcome to your contact book")
    print()
    print()
    print("Type 'help' for instructions")
    main(con)
one()