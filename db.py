import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

def addOrder():
    print("add order")