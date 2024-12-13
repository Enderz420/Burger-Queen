import sqlite3

# TODO: Rework file to use classes instead of functions directly.
## TODO: Clean up code.
### TODO: Comments

def init():
    with open('filler.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()

# ta inn burger, og bruker
def addOrder(burger, bruker):
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        print("add order")
        checkUser(bruker)
        cursor.execute("INSERT INTO ordre (Hvem, Hva, Produsert) VALUES (?, ?, ?)", (bruker, burger, 0,))
        con.commit()
        cursor.execute("SELECT * FROM ordre")
        print(cursor.fetchall())
        cursor.execute("SELECT * FROM ordre ORDER BY ID DESC LIMIT 1;")
        new_order = cursor.fetchone()

        if new_order:
            ordre_id, hvem, hva, produsert = new_order
            if produsert == 1:
                produsert = "Ja"
            produsert = "Nei"
            print(f"Nyeste bestilling \nBestillingsnummer: {ordre_id}\n Bestiller: {hvem}\n Burger: {hva}\n Ferdig? {produsert}")
            deductIngredienser(burger)
            
            match produsert:
                case "Ja":
                    produsert = 1
                case "Nei":
                    produsert = 0
                case _:
                    pass
        else:
            print("Ingen bestilling funnet")
    except sqlite3.Error as e:
        print(f"{e}")

def removeOrder(ID):
    try:
        con = sqlite3.connect("database.db")
        print("remove order")
        
        cursor = con.cursor()
        cursor.execute("SELECT * FROM ordre WHERE ID = ?", (ID,))
        result = cursor.fetchone()[0]
        
        cursor.execute("SELECT Produsert from ordre where ID = ?", (ID,))
        produsert = cursor.fetchone()
        if produsert == 1:
            cursor.execute("SELECT Hva FROM Ordre where ID = ?", (ID,))
            burgers = cursor.fetchone()
            deductIngredienser(burgers)
        else:
            cursor.execute("SELECT Hva FROM Ordre where ID = ?", (ID,))
            burgers = cursor.fetchone()
            addIngredienser(burgers)
        print(ID)
        print(result) 
        if result == ID: 
            cursor.execute("DELETE FROM Ordre WHERE ID = ?", (ID,))
            con.commit()
            cursor.execute("SELECT * FROM Ordre")
        else:
            print("Could not handle")
        
        con.commit()    
        con.close()
    except sqlite3.Error as e:
        print(f"{e}")

def deductIngredienser(burger):
    try:
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
                print(f"remove one {ingrediens}")

            else:
                cursor.execute("SELECT Ingrediens FROM Ingredienser WHERE ID = ?", (ingrediens,))
                print(f"Du har ikke nokk {ingrediens} til å lage dette!")
            
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print(f"{e}")
    
def addIngredienser(burger):
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
            
        cursor.execute("SELECT IngrediensID FROM BurgerHasIngredienser WHERE BurgerID = ?", (burger))
        ingredienser = cursor.fetchall()

        for g_ingrediens in ingredienser:
            ingrediens = g_ingrediens[0]

            cursor.execute("SELECT HvorMye FROM Ingredienser WHERE ID = ?", (ingrediens,))
            current_quantity = cursor.fetchone()[0]
            amount_to_add = 1 

            if int(current_quantity) >= amount_to_add:
                cursor.execute("UPDATE Ingredienser SET HvorMye = HvorMye + ? WHERE ID = ?", (amount_to_add, ingrediens))
                print(f"add one {ingrediens}")
                        
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print(f"{e}")

def checkUser(user):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    print("check user state")
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ?", (user,))
    result = cursor.fetchone()
    con.close()
    print(result)

def listUsers():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT Navn FROM Brukere")
    result = cursor.fetchall()
    print(result)
    
def checkUserAnsettelse(user):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT navn FROM Brukere WHERE Navn = ? AND Ansatt = 1", (user,))
    result = cursor.fetchone()
    con.close()
    print(result)
    if result is None:
        return False
    else:
        return True
    
def loginUser(user, password):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    print("Logging in.")
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ? AND Passord = ?", (user, password,))
    result = cursor.fetchone()
    con.close()
    if result is not None:
        return True
    else: 
        return False
    
def createUser(username, password):
    try:    
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Brukere WHERE Navn = ?", (username,))
        con.commit()
        result = cursor.fetchone()
        print(result)
        if result is not None:
            print("Bruker finnes allerede!")
        cursor.execute("INSERT INTO Brukere (Navn, Passord, Ansatt) VALUES (?, ?, ?)", (username, password, 0,))
        con.commit()
        print(f"Bruker {username} opprettet!")
        con.close()
    except sqlite3.Error as e:
        print(f"{e}")    
    
def checkInventory(user):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ? AND Ansatt = 1", (user,))
    result = cursor.fetchone()
    
    if result: 
        cursor.execute("SELECT Ingredienser.Ingrediens, Ingredienser.HvorMye FROM Ingredienser")
        ingredients = cursor.fetchall()
        for ingredient in ingredients:
            print(f"Ingrediens: {ingredient[0]}, Mengde: {ingredient[1]}")
    else:
        print("Bruker er ikke ansatt")
    con.close()
        
def checkOrders(username):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ? AND Ansatt = 1", (username,))
    result = cursor.fetchone()
    if result:
        cursor.execute("SELECT * FROM Ordre")
    else:    
        cursor.execute('SELECT * FROM Ordre WHERE Hvem = ?', (username,))
    rows = cursor.fetchall()
    cursor.execute("SELECT * FROM ordre ORDER BY ID ASC")
    
    # Determine the longest width for each column
    header = ("Ordre Nr.", "Bestiller", "Burger", "Ferdig?")
    widths = [len(cell) for cell in header]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])

    # Construct formatted row like before
    formatted_row = ' '.join('{:%d}' % width for width in widths)
        
    print(formatted_row.format(*header))
    
    for Row in rows:
        print(formatted_row.format(*Row))
    con.close
        
def completeOrder(ID):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    
    cursor.execute("SELECT Produsert FROM Ordre WHERE ID = ?", (ID,))
    result = cursor.fetchone()
    
    if result:
        cursor.execute("UPDATE Ordre SET Produsert = 1 WHERE ID = ?", (ID,))
        print(f"Ordre Nr:{ID} er ferdig.")
    
    con.commit()
    con.close()

