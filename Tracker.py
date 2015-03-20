'''=========================+
  |   Refrigerator Tracker  |
  |         Tracker         |
  |           ---           |
  |      Jocelyn Huang      |
  | Last modified: 03/20/15 |
  +========================='''

import ProduceFunctionsClass

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
            print ("- fridge / f : Prints out what's in the fridge"
                  " in order of date of expiry.")
            print ("- in fridge / if: Prompts for a lookup of an item in"
                  " the current fridge stock.")
            print ("- lookup / l : Prompts for a lookup of an item in the"
                  " general produce database.")
            print ("- new produce / np : Prompts for information for a new"
                  " piece of produce")

        # Lookup command: Find a specific food in general database
        elif (cmd == "lookup" or cmd == "l"):
            prodb.produceExists(raw_input(" ?=> "))
        
        # New Produce command: Enters a new food into general database
        elif (cmd == "new produce" or cmd == "np"):
            # Produce name
            name = raw_input("Name of produce: ")
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
        
        # In Fridge command: Checks if a given food is in the fridge
        elif (cmd == "in fridge" or cmd == "if"):
            name = raw_input(" ?=> "))
            prodb.inFridge(name)

        # Fridge command: <fill in later>
        elif (cmd == "fridge" or cmd == "f"):
            pass
        
        cmd = raw_input('==> ')

if __name__ == '__main__' : main()
