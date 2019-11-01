#
# COMMAND LINE CONTACT BOOK
# MADE BY 
# 
# CONTRIBUTERS:
# BROOK JEYNES, 
#
# APPLICATION DESCRIPTION:
#
#
#
#

# IMPORTS
import sqlite3
from sqlite3 import Error

# INITIALISES DATABASE VARIABLES
con = sqlite3.connect('contacts.db')
cursorObj = con.cursor()

# CREATES SQL TABLE IF NOT ALREADY CREATED
def sql_table(con):
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

# MAIN FUNCTION RUN
def main(con):
    # GET CONTACT VALUES AND INSERT THEM INTO DATABASE
    def add_contact(con):
        sql_insert = """
        INSERT INTO contacts (fname, lname, phone, email) 
        VALUES (?,?,?,?)
        """

        fname = input("enter first name: ")
        lname = input("enter last name: ")
        phone = input("enter number: ")
        email = input("enter email: ")

        cursorObj.execute(sql_insert, (fname, lname, phone, email))
        con.commit()

        # CONFIRMATION MESSAGE
        print("contact", fname, lname, "added")

        # SHOWS ALL CONTACTS ADDED // COMMENTED OUT BECAUSE IT THE ADDITION OF IT MADE NO SENSE TO ME, BROOK .J
        #cursorObj.execute("SELECT * FROM contacts")
        #rows = cursorObj.fetchall()
        #for row in rows:
        #    print(row)

        # GIVES USER CHOICE TO ADD ANOTHER CONTACT
        userChoice = input("add another?(y/n): ")
        if userChoice == "y":
            add_contact(con)
            con.commit()
        else:
            con.commit()

    # DISLAYS ALL CONTACTS IN BOOK
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
            print("\nHmmm... that doesn't seem like a command, enter 'help' to see all commands")
            main(con)

    cmd = input("enter command letter: ")
    if cmd == "help":
        help()
    else:
        norm_cmd()

# GIVES USER A RUNDOWN OF HOW TO USE THE COMMAND LINE APPLICATION
def help():
    print("""
    Type 'a' for instructions
    Type 's' to search for a contact
    Type 'ls' to list all contacts
    Type 'd' to delete a contact
    Press Enter to continue...\n
    """)
    main(con)

# WELCOME MESSAGES
def one():
    c="_"
    c=c.center(10)
    print(c*54)
    print("Welcome to your contact book\n\n")
    print("Type 'help' for instructions")
    main(con)

# APPLICATION STARTPOINT
one()