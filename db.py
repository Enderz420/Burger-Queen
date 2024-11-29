import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()


# ta inn burger, og bruker
def addOrder(burger, bruker):
    print("add order")
    cursor.execute("INSERT INTO ordre VALUES (?, ?, ?)", (bruker, burger, "Nei"))
    con.commit()
    cursor.execute("SELECT * FROM ordre")
    print(cursor.fetchone())

def checkUser(user):
    print("check user state")
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ?", (user,))
    
    result = cursor.fetchone()
    print(result)