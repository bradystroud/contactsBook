#update
from database import *

# UPDATES CONTACTS DETAILS
def update():
    cursorObj = con.cursor()
    print()
    cont = input("which contact to update?(enter first name): ")
    detail = input("which detail would you like to change for "+str(cont)+"?: ")
    rows = cursorObj.execute("SELECT %s FROM contacts WHERE fname = ?" % (detail), (cont,))
    for row in rows:
        old_value = row
        new = input("what would you like "+cont+"'s "+detail+" to be?(current is:"+str(old_value)+"): ")
    cursorObj.execute("UPDATE contacts SET %s = ? WHERE fname = ? " % (detail), (new, cont,))
    con.commit()

    # CONFIRM UPDATED CONTACT
    rows = cursorObj.execute("SELECT %s FROM contacts WHERE fname = ?" % (detail), (cont,))
    for row in rows:
        print("sucessfully updated "+cont+"'s "+detail+" to "+str(row)+" from "+str(old_value))
    input("Press Enter to continue...")
    print()