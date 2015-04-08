'''==========================+
  |   Refrigerator Tracker  |
  | Produce Functions Class |
  |           ---           |
  |      Jocelyn Huang      |
  | Last modified: 04/08/15 |
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

    def newProduce(self, name, expiry, comments):
        # probably want to make some checks before arbitrarily inserting
        # into the database.
        self.cursor.execute("INSERT OR REPLACE INTO produce_info VALUES (?,?,?)",
                (name, expiry, comments))
        self.conn.commit()

    #=====<changeName>=====
    # Changes the name of the given produce into another given string
    # Returns: None
    
    def changeName(self, name, name2):
        pass # Have to delete and then re-create

    #=====<changeDays>=====
    # Changes the days before expiry given a produce name
    # Returns: None

    def changeDays(self, name, days):
        print name, days

    #=====<changeComment>=====
    # Changes the comments of some given produce
    # Returns: None

    def changeComment(self, name, comment):
        pass

    #=====<removeProduce>=====
    # Removes the produce and its information from the info database
    # Returns: None

    def removeProduce(self, name):
        if (self.produceExists(name)):
            print "Are you sure you want to delete", name, "?"
            confirm = raw_input(" ?=> ")
            if (confirm == "yes" or confirm == "y"):
                self.cursor.execute("DELETE FROM produce_info WHERE name=(?)",
                        (name,))
                self.conn.commit()

    #=====<inFridge>=====
    # Checks if the given produce is in the fridge
    # Returns: Boolean

    def inFridge(self, name):
        self.cursor.execute("SELECT * FROM fridge WHERE name=(?)",
                (name,))
        result = self.cursor.fetchone()
        if (not(result==None)): ######Probably want more here
            return True

        else:
            print "\n",name,"doesn't exist in the fridge.\n"
            return False

    #=====<addToFridge>=====
    # Adds some produce into the fridge
    # Returns: None

    def addToFridge(self, name):
        pass

    #=====<removeFromFridge>=====
    # Removes some produce from the fridge
    # Returns: None

    def removeFromFridge(self, name):
        pass

    #=====<allFridgeItems>=====
    # Retrieves all items that are in the fridge
    # Returns: Array with: String (name) -> Date

    def allFridgeItems(self):
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
