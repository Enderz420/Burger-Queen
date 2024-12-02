import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()


# ta inn burger, og bruker
def addOrder(burger, bruker):
    print("add order")
    isDone = "Nei" # Default Value, cannot use Bool
    cursor.execute("INSERT INTO ordre VALUES (?, ?, ?)", (bruker, burger, isDone))
    con.commit()
    cursor.execute("SELECT * FROM ordre")
    print(cursor.fetchone())
    if isDone == "Ja":
        cursor.execute("SELECT * FROM BurgerHasIngredienser INNER JOIN Burger on BurgerHasIngredienser.BurgerID = Burger.ID AND WHERE BurgerHasIngredienser.IngrediensID = Ingredienser.ID")

def checkUser(user):
    print("check user state")
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ?", (user,))
    result = cursor.fetchone()
    print(result)
    
def loginUser(user, password):
    print("loginUser")
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ? AND Passord = ?", (user, password,))
    result = cursor.fetchone()
    if result is not None:
        return True
    else: 
        return False
    
def checkInventory(user):
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ? AND Ansatt = 'Ja'", (user,))
    result = cursor.fetchone()
    
    if result: 
        cursor.execute("SELECT Ingredienser.Ingrediens, Ingredienser.HvorMye FROM Ingredienser")
        ingredients = cursor.fetchall()
        for ingredient in ingredients:
            print(f"Ingredient: {ingredient[0]}, Quantity: {ingredient[1]}")
    else:
        print("Bruker er ikke ansatt")