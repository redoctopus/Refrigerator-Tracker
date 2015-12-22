'''=========================+
  |   Refrigerator Tracker  |
  |         Tracker         |
  |           ---           |
  |      Jocelyn Huang      |
  | Last modified: 12/22/15 |
  +========================='''

import ProduceFunctionsClass
import time
import datetime

#Make things lowercase!

def main():
    print "+======================+"
    print "| Refrigerator Tracker |"
    print "|    Jocelyn Huang     |"
    print "|        v.1.0         |"
    print "+======================+"
    print "\nRefrigerator Tracker! Enter \"quit\" (or just \"q\") to quit."
    print "For a list of commands and what they do, enter \"help\". \n"

    # Datetime
    print "Date is: ", datetime.date.today().strftime("%m/%d/%y")
    
    cmd = raw_input('==> ')
    
    prodb = ProduceFunctionsClass.produceDatabaseFuncts()
    
    while (cmd != "quit" and cmd != "q"):
        # Help command
        if (cmd == "help" or cmd == "h"):
            print ("- add / a : Prompts for multiple items to add to the"
                   "fridge.")
            print ("- add one / ao : Prompts for a single item to add to the"
                  "fridge. If it's not already in the db, asks for more info.")
            print ("- edit produce / ep : Prompts for some produce to edit"
                  " its information in produce_info")
            #print ("- fridge / f : Prints out what's in the fridge"
            #      " in order of date of expiry.")
            print ("- in fridge / if: Prompts for a lookup of an item in"
                  " the current fridge stock.")
            print ("- list / ls : Returns the items in the fridge, in order of"
                  " date of expiry.")
            print ("- lookup / l : Prompts for a lookup of an item in the"
                  " general produce database.")
            print ("- new produce / np : Prompts for information for a new"
                  " piece of produce")
            print ("- remove / r : Prompts for an item to remove from fridge.")
            print ("- remove produce / rp : Prompts for some produce to remove"
                  " from the information database.")
            print ("- quit / q : Quit.")

        # Lookup command: Find a specific food in general database
        # Keys: lookup, l
        elif (cmd == "lookup" or cmd == "l"):
            prodb.produceExists(raw_input(" ?=> "))
        
        # New Produce command: Enters a new food into general database
        # Keys: new produce, np
        elif (cmd == "new produce" or cmd == "np"):
            # Produce name
            name = raw_input("Name of produce: ")
            
            print "Checking if this already exists..."
            if(prodb.produceExists(name)):
                cmd = raw_input("Are you sure you want to replace? ")
                if(cmd != "yes" and cmd != "y"): continue

            prodb.newProduce(name)

            print "Success! Inserted", name, "into the database."
        
        # Edit Produce command: Changes the info for some produce
        # Keys: edit produce, ep
        elif (cmd == "edit produce" or cmd == "ep"):
            name = raw_input(" ?=> ")
            if (not prodb.produceExists(name)):
                continue
            print "Enter 1 to change name,"
            print "2 to change number of days until expiry,"
            print "and 3 to change the comment."
            cmd = raw_input( "Enter 4 to quit.\n ==> ")

            if (cmd == "4"): # Quits
                continue

            if (cmd == "1"): # Changes name
                newname = raw_input(" New name: ")
                if(newname == ""):
                    print "Not a valid name."
                    continue
                prodb.changeName(name, newname)

            if (cmd == "2"): # Change days before expiry
                while(True):
                    try:
                        days = raw_input(" Number of days: ")
                        if(cmd == "cancel" or cmd == "c"): break
                        expiry = int(cmd)
                        if(expiry < 0): raise ValueError
                        break
                    except ValueError:
                        print "Not an int; \"cancel\" to cancel"
                        continue
                prodb.changeDays(name, days)

            if (cmd == "3"): # Change comment
                comment = raw_input(" New comment: ")
                prodb.changeComment(name, comment)

        # Remove Produce command : Deletes the produce from the info db
        # Keys: remove produce, rp
        elif (cmd == "remove produce" or cmd == "rp"):
            name = raw_input(" ?=> ")
            prodb.removeProduce(name)
            print name,"removed from database."

        #|===========================================|
        #|=======<Fridge Functions Start Here>=======|
        #|===========================================|

        # In Fridge command: Checks if a given food is in the fridge
        # Keys: in fridge, if
        elif (cmd == "in fridge" or cmd == "if"):
            name = raw_input(" ?=> ")
            prodb.inFridge(name)

        # Add command: Adds produce to the fridge.
        # add, a
        elif (cmd == "add one" or cmd == "ao"):
            # Produce names
            name = raw_input("Name of produce: ")
            if (prodb.inFridge(name)):          # It's already in the fridge
                print "That's already in the fridge. Do you want to replace?"
                if(cmd != "yes" and cmd != "y"): continue

            elif not prodb.produceExists(name): # Needs to be added to the database
                print name,"isn't in the database yet."

                while (True):
                    try:
                        cmd = raw_input("# Days before expiring: ")
                        if(cmd == "cancel" or cmd == "c"): break
                        expiry = int(cmd)
                        if(expiry < 0): raise ValueError
                        break
                    except ValueError:
                        print "Not an int; \"cancel\" to cancel"
                        continue
                if (cmd == "cancel" or cmd == "c"): continue

                comments = raw_input("Additional comments about produce: ")

                if(name == "" or expiry == 0):
                    print "Invalid produce input"
                    continue

                prodb.newProduce(name, expiry, comments)
                print "Inserted", name, "into the database."

            print "Inserting", name, "into the fridge..."
            
            # Get data of the specified produce from database ###############

            print "Success! Inserted", name, "into the fridge."
        
        elif (cmd == "add" or cmd == "a"): ##################################
            testlist = ["test234"]
            prodb.addToFridge(testlist)

        # Remove command: Removes some item from the fridge.
        # Keys: remove, r
        elif (cmd == "remove" or cmd == "r"):
            name = raw_input(" ?=> ")
            prodb.removeFromFridge(name)
            print name,"removed from fridge."

        # List command: Gives a list of the first n items that will spoil
        # Keys: list, ls
        elif (cmd == "list" or cmd == "ls"):
            items = prodb.listFridge() # Need to figure out return type...
                                       # List of strings w/ relevant info?
            #for x in items:
            #    print x
        
        cmd = raw_input('==> ')
    
    del prodb

if __name__ == '__main__' : main()
