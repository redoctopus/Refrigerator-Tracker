'''==========================+
  |   Refrigerator Tracker  |
  | Produce Functions Class |
  |           ---           |
  |      Jocelyn Huang      |
  | Last modified: 12/22/15 |
  +========================='''

''' This file contains the functions that interact with the database.
    In particular, it uses a class that connects to db refrigerator_tracker
    to open a connection instead of having standalone methods
    that open them individually. '''

import sqlite3

class produceDatabaseFuncts(object):
    def __init__(self):
        self.conn = sqlite3.connect('refrigerator_tracker.db')
        self.cursor = self.conn.cursor()
    
    #=====<produceExists>=====
    # Checks if the given produce exists in produce_info
    # Returns: Boolean, and prints out the data if it exists.

    def produceExists(self, name):
        self.cursor.execute("SELECT * FROM produce_info WHERE name=(?)",
                (name,)) #These tuples... that one comma...
        result = self.cursor.fetchone()
        if (not(result==None)):
            print "\n============"
            print result[0]
            print "------------"
            print "Typically expires in", result[1], "days"
            print "Other comments:\n", result[2], "\n============\n"
            return True

        else:
            print "\n",name,"doesn't exist in the database.\n"
            return False

    #=====<newProduce>=====
    # Inserts new kinds of produce into produce_info
    # Returns: None

    def newProduce(self, name):
        # probably want to make some checks before arbitrarily inserting
        # into the database.

        # Attempt to get days before expiry
        while (True): # This feels a bit clunky. Possibly refactor?
            try:
                cmd = raw_input("# Days before expiring: ")
                if(cmd == "cancel" or cmd == "c"): break
                expiry = int(cmd)
                if(expiry < 0): raise ValueError
                break
            except ValueError:
                print "Not an int; \"cancel\" to cancel"
                continue
        if (cmd == "cancel" or cmd == "c"): return
        # Comments if applicable
        comments = raw_input("Additional comments: ")

        if(name == "" or expiry == 0):
            print "Invalid produce input"
            return

        self.cursor.execute(
                "INSERT OR REPLACE INTO produce_info VALUES (?,?,?)",
                (name, expiry, comments))
        self.conn.commit()

    #=====<changeName>=====
    # Changes the name of the given produce into another given string.
    # Note: Have to delete and then re-create. This is sub-optimal...
    # Returns: None
    
    def changeName(self, name, name2):
        self.cursor.execute("SELECT * FROM produce_info WHERE name=(?)",
                (name,))
        result = self.cursor.fetchone()
        expiry = result[1]
        comments = result[2]

        if(self.produceExists(name2)):
            confirm = raw_input("Already exists, replace? ")
            if(confirm == "no" or confirm == "n"):
                print "Not replacing."
                return
        self.newProduce(name2, expiry, comments)
        print "Deleting the original..."
        self.removeProduce(name)
        print "Done!"

    #=====<changeDays>=====
    # Changes the days before expiry given a produce name
    # Returns: None

    def changeDays(self, name, days):
        self.cursor.execute(
            "UPDATE produce_info SET expiry=(?) WHERE name=(?)",
            (days, name))
        self.conn.commit()

    #=====<changeComment>=====
    # Changes the comments of some given produce
    # Returns: None

    def changeComment(self, name, comment):
        self.cursor.execute(
            "UPDATE produce_info SET comments=(?) WHERE name=(?)",
            (comment, name))
        self.conn.commit()

    #=====<removeProduce>=====
    # Removes the produce and its information from the info database
    # Returns: None

    def removeProduce(self, name):
        if (self.produceExists(name)):
            print "Are you sure you want to delete", name, "?"
            confirm = raw_input(" ?=> ")
            if (confirm == "yes" or confirm == "y"):
                self.cursor.execute(
                    "DELETE FROM produce_info WHERE name=(?)",
                    (name,))
                self.conn.commit()

    #=====<inFridge>=====
    # Checks if the given produce is in the fridge
    # Returns: Boolean

    def inFridge(self, name):
        self.cursor.execute("SELECT * FROM fridge WHERE name=(?)",
                (name,))
        result = self.cursor.fetchone()
        if (not(result==None)):
            print "\n============"
            print "Index:",result[0] #Don't need, index.
            print result[1] #name
            print result[2] #insertDate
            print result[3] #expDate
            print result[4] #Need to check if no comment--empty string?
            print "------------"
            return True

        else:
            print "\n",name,"doesn't exist in the fridge.\n"
            return False

    #=====<addToFridge>=====
    # Adds some produce into the fridge from a list of produce names
    # Returns: None

    def addToFridge(self, prodList):
        unadded = []

        for name in prodList:
            self.cursor.execute(
                "SELECT * FROM produce_info WHERE name=(?)",
                (name,))
            result = self.cursor.fetchone()
            if (result == None):
                print name, "isn't in the database."
                add = raw_input("Would you like to add it to the database? (y/n) ")
                if (add == "y" or add == "yes"):
                    self.newProduce(name)
                else:
                    print name, "will not be added."
                    unadded.append(name)

        print "\nThe following items were not added:"
        for x in range(len(unadded)):
            print x+1, ":", unadded[x]

    #=====<removeFromFridge>=====
    # Removes some produce from the fridge
    # Returns: None

    def removeFromFridge(self, name):
        ############Need more checks here. ########
        self.cursor.execute("DELETE FROM fridge WHERE name=(?)", (name,))
        print "removed", name

    #=====<listFridge>=====
    # Retrieves all items that are in the fridge
    # Returns: Array with: String (name) -> Date

    def listFridge(self):
        pass

    #=====<quickestSpoil>=====
    # Retrieves the first (n) produce items in the fridge based on spoil date
    # Returns: Array

    def quickestSpoil(self, n):
        pass

    #=====<Deletion>=====
    def __del__(self):
        self.cursor.close()
        self.conn.close()

# End of file
