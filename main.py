#main
import sqlite3
from sqlite3 import Error

from addContact import add_contact
from delete import delete
from listAll import ls
from update import update
from search import search




def norm_cmd(cmd):
        if cmd == "a":
            add_contact()
            command()
        elif cmd == "s":
            search()
            command()
        elif cmd == "u":
            update()
            command()
        elif cmd == "d":
            delete()
            command()
        elif cmd == "ls":
            ls()
            command()
        else:
            print("\nHmmm... that doesn't seem like a command, enter 'help' to see all commands")
            command()

def command():
    cmd = input("enter command letter: ")
    if cmd == "help":
        help()
    else:
        norm_cmd(cmd)

# WELCOME MESSAGES
def welcome():
    c="_"
    c=c.center(10)
    print(c*54)
    print("Welcome to your contact book\n\n")
    print("Type 'help' for instructions")
    command()

# APPLICATION STARTPOINT
welcome()