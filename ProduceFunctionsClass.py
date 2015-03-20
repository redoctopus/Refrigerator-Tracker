'''==========================+
  |   Refrigerator Tracker  |
  | Produce Functions Class |
  |           ---           |
  |      Jocelyn Huang      |
  | Last modified: 03/19/15 |
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
    # Returns: Boolean

    def produceExists(self, name):
        print name
        #self.cursor.execute("")
        #self.conn.commit()
        return self.cursor

    #=====<newProduce>=====
    # Inserts new kinds of produce into produce_info
    # Returns: None

    def newProduce(self, name, expiry, comments):
        pass

    #=====<inFridge>=====
    # Checks if the given produce is in the fridge
    # Returns: Boolean

    def inFridge(self, name):
        pass

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
        self.conn.close()

# End of file
