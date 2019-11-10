from database import *




def add_contact():
    fname = input("enter first name: ")
    lname = input("enter last name: ")
    phone = input("enter number: ")
    email = input("enter email: ")
    contact = (fname, lname, phone, email)
    sql_insert = """
        INSERT INTO contacts(fname, lname, phone, email) 
        VALUES (?,?,?,?)"""
    cursorObj.execute(sql_insert, contact)
    con.commit()

    # CONFIRMATION MESSAGE
    print("contact", fname, lname, "added")

    # SHOWS ALL CONTACTS ADDED // COMMENTED OUT BECAUSE IT THE ADDITION OF IT MADE NO SENSE TO ME, BROOK .J
    # DEAR BROOK, THIS WAS HERE SO WHEN I WAS TESTING THE PROGRAM, I COULD IMMEDIATELY SEE IF THE QUERY WORKED. STILL, I SHOULD HAVE ADDED DOCUMENTATION FOR CONTRIBUTORS. MY BAD XOXO
    cursorObj.execute("SELECT * FROM contacts")
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

    # GIVES USER CHOICE TO ADD ANOTHER CONTACT
    userChoice = input("add another?(y/n): ")
    print()
    if userChoice == "y":
        add_contact
        con.commit()
    else:
        con.commit()
        # main.command()
