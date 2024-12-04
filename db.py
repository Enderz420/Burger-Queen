import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()


# ta inn burger, og bruker
def addOrder(burger, bruker):
    con = sqlite3.connect("database.db")
    print("add order")
    isDone = 0 # Default Value, cannot use Bool
    cursor.execute("INSERT INTO ordre (Hvem, Hva, Produsert) VALUES (?, ?, ?)", (bruker, burger, isDone))
    con.commit()
    cursor.execute("SELECT * FROM ordre")
    print(cursor.fetchall())
    if isDone == 1: # TODO Add proper order handling.
        cursor.execute("SELECT * FROM BurgerHasIngredienser INNER JOIN Burger ON BurgerHasIngredienser.BurgerID = Burger.ID INNER JOIN Ingredienser ON BurgerHasIngredienser.IngrediensID = Ingredienser.ID;")

def checkUser(user):
    con = sqlite3.connect("database.db")
    print("check user state")
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ?", (user,))
    result = cursor.fetchone()
    con.close()
    print(result)

def checkUserAnsettelse(user):
    con = sqlite3.connect("database.db")
    cursor.execute("SELECT navn FROM Brukere WHERE Navn = ? AND Ansatt = 1", (user,))
    result = cursor.fetchone()
    con.close()
    print(result)
    if result is None:
        return False
    else:
        return True
    
    print(result)
    
def loginUser(user, password):
    con = sqlite3.connect("database.db")
    print("loginUser")
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ? AND Passord = ?", (user, password,))
    result = cursor.fetchone()
    con.close()
    if result is not None:
        return True
    else: 
        return False
def checkInventory(user):
    con = sqlite3.connect("database.db")
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ? AND Ansatt = 1", (user,))
    result = cursor.fetchone()
    
    if result: 
        cursor.execute("SELECT Ingredienser.Ingrediens, Ingredienser.HvorMye FROM Ingredienser")
        ingredients = cursor.fetchall()
        for ingredient in ingredients:
            print(f"Ingredient: {ingredient[0]}, Quantity: {ingredient[1]}")
    else:
        print("Bruker er ikke ansatt")
    con.close()
        
def checkOrders():
    con = sqlite3.connect("database.db")
    cursor.execute('SELECT * FROM Ordre')
    rows = cursor.fetchall()
    con.close()
    for row in rows:
        print(f"{row}\n", sep='-')
        
checkOrders()