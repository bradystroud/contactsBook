#delyeet

from database import *

#MIGHT DELETE CONTACT??. SOMETIMES IT JUST DOES NOTHING AYE
def delete():
    cont = input("which contact to delete?(enter first name): ")
    rows = cursorObj.execute("SELECT fname, lname FROM contacts WHERE fname = ?", (cont,))
    for row in rows:
        cont_to_del = row
        confirm = input("Are you sure you want to delete this contact"+str(cont_to_del)+"? (you cannot recover it ever)y/n: ")
        if confirm == "y":
            cursorObj.execute("DELETE FROM contacts WHERE fname = ? ", (cont,))
            con.commit()
            
            print("Ok, "+str(cont_to_del)+" has been yeeted into the bin")
            input("Press Enter to continue...")
            print()
        else:
            print("Ok")
            input("Press Enter to continue...")
            print()
        