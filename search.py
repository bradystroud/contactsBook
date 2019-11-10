#search

from database import *

def search():
    c = cursorObj
    contact = input("Who do you want to search for?")
    contact = ("%"+contact+"%")
    c.execute("SELECT * FROM contacts WHERE fname LIKE ?", (contact,))
    row = c.fetchone()
    if row == None:
        c.execute("SELECT fname FROM contacts WHERE fname LIKE ?", (contact,))
        row = c.fetchone()
        row = str(row)
        print("There are no results for this query, did you mean "+ row +"?")
        yes = input("(y/n): ")
        if yes == "y":
            c.execute("SELECT * FROM contacts WHERE fname = ?", (row,))
            row = c.fetchone()
            print("Ok, here are the details: "+str(row))
            input("Press Enter to continue...")
    else:
        print(str(row)+"\n")