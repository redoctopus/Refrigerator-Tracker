'''=========================+
  |   Refrigerator Tracker  |
  |    Produce Functions    |
  |           ---           |
  |      Jocelyn Huang      |
  | Last modified: 03/18/15 |
  +========================='''

''' This file contains the functions that interact with the database.'''

# Note: currently all the functions connect to the db individually.
#       This is pretty costly--refactor once more set up?
#       (Try classes? See the StackOverflow answer.)

import sqlite3

#=====<produceExists>=====
# Checks if the given produce exists in produce_info
# Returns: Boolean

def produceExists(name):
    conn = sqlite3.connect("refrigerator_tracker.db")
    cursor = conn.cursor()

#=====<newProduce>=====
# Inserts new kinds of produce into produce_info
# Returns: None

def newProduce(name, expiry, comments):
    conn = sqlite3.connect("refrigerator_tracker.db")
    cursor = conn.cursor()

#=====<inFridge>=====
# Checks if the given produce is in the fridge
# Returns: Boolean

def inFridge(name):
    pass

#=====<addToFridge>=====
# Adds some produce into the fridge
# Returns: None

def addToFridge(name):
    pass

#=====<removeFromFridge>=====
# Removes some produce from the fridge
# Returns: None

def removeFromFridge(name):
    pass

#=====<allFridgeItems>=====
# Retrieves all items that are in the fridge
# Returns: Array with: String (name) -> Date

def allFridgeItems():
    pass

#=====<quickestSpoil>=====
# Retrieves the first (n) produce items in the fridge based on spoil date
# Returns: Array

def quickestSpoil(n):
    pass
