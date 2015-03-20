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
        if (cmd == "help" or cmd == "h"):
            print ("- fridge / f : Prints out what's in the fridge"
                  " in order of date of expiry.")
            print ("- lookup / l : Prompts for a lookup of an item in the"
                  " general produce database.")
        
        elif (cmd == "lookup" or cmd == "l"):
            prodb.produceExists(raw_input(" ?=> "))
            
        elif (cmd == "fridge" or cmd == "f"):
            pass
        
        cmd = raw_input('==> ')

if __name__ == '__main__' : main()
