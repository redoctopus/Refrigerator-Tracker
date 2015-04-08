'''=========================+
  |   Refrigerator Tracker  |
  |         Tracker         |
  |           ---           |
  |      Jocelyn Huang      |
  | Last modified: 04/08/15 |
  +========================='''

import ProduceFunctionsClass

#Make things lowercase!

def main():
    print "+======================+"
    print "| Refrigerator Tracker |"
    print "|    Jocelyn Huang     |"
    print "|        v.1.0         |"
    print "+======================+"
    print "\nRefrigerator Tracker! Enter \"quit\" (or just \"q\") to quit."
    print "For a list of commands and what they do, enter \"help\". \n"
    
    cmd = raw_input('==> ')
    
    prodb = ProduceFunctionsClass.produceDatabaseFuncts()
    
    while (cmd != "quit" and cmd != "q"):
        # Help command
        if (cmd == "help" or cmd == "h"):
            print ("- add / a : Prompts for an item to add to the fridge."
                  " if it's not already in the db, asks for additional info.")
            print ("- edit produce / ep : Prompts for some produce to edit"
                  " its information in produce_info")
            print ("- fridge / f : Prints out what's in the fridge"
                  " in order of date of expiry.")
            print ("- in fridge / if: Prompts for a lookup of an item in"
                  " the current fridge stock.")
            print ("- list / lst : Prompts for a number n, then returns the"
                  " first n items that will spoil in the fridge.")
            print ("- lookup / l : Prompts for a lookup of an item in the"
                  " general produce database.")
            print ("- new produce / np : Prompts for information for a new"
                  " piece of produce")
            print ("- remove / r : Prompts for an item to remove from fridge.")
            print ("- remove produce / rp : Prompts for some produce to remove"
                  " from the information database.")
            print ("- quit / q : Quit.")

        # Lookup command: Find a specific food in general database
        elif (cmd == "lookup" or cmd == "l"):
            prodb.produceExists(raw_input(" ?=> "))
        
        # New Produce command: Enters a new food into general database
        elif (cmd == "new produce" or cmd == "np"):
            # Produce name
            name = raw_input("Name of produce: ")
            
            print "Checking if this already exists..."
            if(prodb.produceExists(name)):
                cmd = raw_input("Are you sure you want to replace? ")
                if(cmd !="yes" and cmd != "y"): continue

            # Attempt to get days before expiry
            while (True): # This feels a bit clunky. Possibly refactor?
                try:
                    cmd = raw_input("# Days before expiring: ")
                    if(cmd == "cancel" or cmd == "c"): break
                    expiry = int(cmd)
                    break
                except ValueError:
                    print "Not an int; \"cancel\" to cancel"
                    continue
            if (cmd == "cancel" or cmd == "c"): continue
            # Comments if applicable
            comments = raw_input("Additional comments: ")

            if(name == "" or expiry == 0):
                print "Invalid produce input"
                continue
            
            prodb.newProduce(name, expiry, comments)
            print "Success! Inserted", name, "into the database."
        
        # Edit Produce command: Changes the info for some produce
        elif (cmd == "edit produce" or cmd == "ep"):
            name = raw_input(" ?=> ")
            if (not prodb.produceExists(name)):
                continue
            print "Enter 1 to change name,"
            print "2 to change number of days until expiry,"
            print "and 3 to change the comment."
            cmd = raw_input( "Enter 4 to quit.\n ==> ")

            #######FINISH IMPLEMENTING THESE#######
            if (cmd == "4"):
                continue

            if (cmd == "1"):
                pass###      # Delete and and recreate.########

            if (cmd == "2"): # Change days before expiry
                while(True):
                    try:
                        days = raw_input(" Number of days: ")
                        if(cmd == "cancel" or cmd == "c"): break
                        expiry = int(cmd)
                        break
                    except ValueError:
                        print "Not an int; \"cancel\" to cancel"
                        continue
                prodb.changeDays(name, days)

            if (cmd == "3"): # Change comment
                comment = raw_input(" New comment: ")
                prodb.changeComment(name, comment)

        # Remove Produce command : Deletes the produce from the info db
        elif (cmd == "remove produce" or cmd == "rp"):
            name = raw_input(" ?=> ")
            prodb.removeProduce(name)

        # In Fridge command: Checks if a given food is in the fridge
        elif (cmd == "in fridge" or cmd == "if"):
            name = raw_input(" ?=> ")
            prodb.inFridge(name)

        # Add command: Adds produce to the fridge. (Should prompt
            #if new produce, remember to do this!)
        elif (cmd == "add" or cmd == "a"):
            # Produce name
            name = raw_input("Name of produce: ")
            if (prodb.inFridge(name)):
                pass #query for##########
            # Otherwise, ask for data, insert into both
            
            print "Success! Inserted", name, "into the fridge."
        

        # Remove command: Removes some item from the fridge.
            #Check if exists first.
        elif (cmd == "remove" or cmd == "r"):
            pass

        # Fridge command: <fill in later>
        elif (cmd == "fridge" or cmd == "f"):
            pass

        # List command: Gives a list of the first n items that will spoil
        elif (cmd == "list" or cmd == "lst"):
            pass
        
        cmd = raw_input('==> ')
    
    del prodb

if __name__ == '__main__' : main()
