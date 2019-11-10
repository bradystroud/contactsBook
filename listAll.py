#list contacts
from database import *

# DISLAYS ALL CONTACTS IN BOOK
def ls():
    cursorObj.execute("SELECT fname, lname, phone, email FROM contacts")
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    input("\nPress Enter to continue...\n")
