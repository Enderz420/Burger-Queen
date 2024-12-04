import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()
# TODO: Rework file to use classes instead of functions directly.
## TODO: Clean up code.

# ta inn burger, og bruker
def addOrder(burger, bruker):
    con = sqlite3.connect("database.db")
    print("add order")
    cursor.execute("INSERT INTO ordre (Hvem, Hva, Produsert) VALUES (?, ?, ?)", (bruker, burger, 0,))
    con.commit()
    cursor.execute("SELECT * FROM ordre")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM ordre ORDER BY ID DESC LIMIT 1;")
    new_order = cursor.fetchone()
    con.close()

    if new_order:
        ordre_id, hvem, hva, produsert = new_order
        if produsert == 1:
            produsert = "Ja"

        produsert = "Nei"
        print(f"Nyeste bestilling: Bestillingsnummer: {ordre_id}\n Bestiller: {hvem}\n Burger: {hva}\n Ferdig? {produsert}")
        deductIngredienser(burger)
        if is_order_completed():
            print("Bestilling er ferdig!")
        else:
            print("Nyeste bestilling er ikke ferdig enda.")
    else:
        print("Ingen bestilling funnet")

def is_order_completed(status):
    ORDER_COMPLETED = 1
    return status == ORDER_COMPLETED

def deductIngredienser(burger): # TODO Fix database writes, so that it doesn't throw database is locked operational error.
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    
    cursor.execute("SELECT IngrediensID FROM BurgerHasIngredienser WHERE BurgerID = ?", (burger,))
    ingredienser = cursor.fetchall()

    for g_ingrediens in ingredienser:
        ingrediens = g_ingrediens[0]

        cursor.execute("SELECT HvorMye FROM Ingredienser WHERE ID = ?", (ingrediens,))
        current_quantity = cursor.fetchone()[0]
        amount_to_deduct = 1 

        if int(current_quantity) >= amount_to_deduct:
            cursor.execute("UPDATE Ingredienser SET HvorMye = HvorMye - ? WHERE ID = ?", (amount_to_deduct, ingrediens))
            print("remove 1")

        else:
            print(f"Du har ikke nokk {ingrediens} til å lage dette!")
        
    con.commit()
    
    con.close()

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

addOrder(1, "Geralt")