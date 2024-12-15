import sqlite3

def init(): # Automatisk laster inn filler.sql for start data.
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
            deductIngredienser()
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

def removeOrder(ID): # tar inn ID og fjerner ordre
    try: # try except for bedre error håndtering.
        con = sqlite3.connect("database.db") # åpne databasen
        print("remove order")
        
        cursor = con.cursor()
        cursor.execute("SELECT * FROM ordre WHERE ID = ?", (ID,))
        result = cursor.fetchone()[0]
        
        cursor.execute("SELECT Produsert from ordre where ID = ?", (ID,))
        produsert = cursor.fetchone()
        if produsert == 0: # hvis burger ikke er ferdig
            cursor.execute("SELECT Hva FROM Ordre where ID = ?", (ID,))
            burgers = cursor.fetchone() # hent burger
            addIngredienser(burgers) # legg til ingredienser 
        if result == ID: # sjekke om result samsvarer med id på ordre
            cursor.execute("DELETE FROM Ordre WHERE ID = ?", (ID,))
            con.commit()
        else:
            print("Could not handle")
        
        con.commit()    
        con.close()
    except sqlite3.Error as e:
        print(f"{e}")

def deductIngredienser(burger): # fjerner 1 ingrediens fra burgeren. Burgeren er ID nummeret på den.
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
                cursor.execute("SELECT Ingrediens FROM Ingredienser WHERE ID = ?", (ingrediens,))
                current_ingrediens = cursor.fetchone()
                print(f"fjerner {"".join(current_ingrediens)}")

            else:
                cursor.execute("SELECT Ingrediens FROM Ingredienser WHERE ID = ?", (ingrediens,))
                current_ingrediens = cursor.fetchone()
                print(f"Du mangler {"".join(current_ingrediens)}")
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print(f"{e}")
    
def addIngredienser(burger): # Legger til 1 av hver ingrediens som blir brukt av en burger, kan bare kalled hvis burger er ikke produsert
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
                cursor.execute("SELECT Ingrediens FROM Ingredienser WHERE ID = ?", (ingrediens,))
                current_ingrediens = cursor.fetchone()
                print(f"legger til en {"".join(current_ingrediens)}")   
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print(f"{e}")

def checkUser(user): # Direkte kaller til databasen og gir tilbake data
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ?", (user,))
    result = cursor.fetchone()
    con.close()
    if result is None:
        return False
    else:
        return result

def listUsers(): # gir en liste over brukere med navn
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT Navn FROM Brukere")
    result = cursor.fetchall()
    print("Aktive brukere:")
    for row in result:
        print(f"- {row[0]}")

def checkUserAnsettelse(user): # sjekker om brukeren er ansatt
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
    
def loginUser(user, password): # Logg inn bruker til applikasjonen med passord og brukernavn
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
    
def createUser(username, password): # Lar bruker registrere seg til databasen med form av brukernavn og passord
    try:    
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Brukere WHERE Navn = ?", (username,))
        con.commit()
        result = cursor.fetchone()
        print(result)
        if result is not None:
            print("Brukeren finnes allerede!")
        cursor.execute("INSERT INTO Brukere (Navn, Passord, Ansatt) VALUES (?, ?, ?)", (username, password, 0,))
        con.commit()
        print(f"Bruker {username} opprettet!")
        con.close()
        
    except sqlite3.Error as e:
        print(f"{e}")    
    
def checkInventory(user): # Sjekker inventar for hvor mye ingredienser du har
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Brukere WHERE Navn = ? AND Ansatt = 1", (user,))
    result = cursor.fetchone()
    
    if result: 
        cursor.execute("SELECT Ingredienser.Ingrediens, Ingredienser.HvorMye FROM Ingredienser")
        ingredients = cursor.fetchall()
        for ingredient in ingredients:
            print(f"Ingrediens: {ingredient[0]} Mengde: {ingredient[1]}")
    else:
        print("Bruker er ikke ansatt")
    con.close()
        
def checkOrders(username): # Sjekker alle aktive bestillinger med form av Nummer, Bestiller, Burger og om den er ferdig eller ikke
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
    con.close()
        
def completeOrder(ID): # Setter en ordre som ferdig
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    
    cursor.execute("SELECT Produsert FROM Ordre WHERE ID = ?", (ID,))
    result = cursor.fetchone()
    
    if result:
        cursor.execute("UPDATE Ordre SET Produsert = 1 WHERE ID = ?", (ID,))
        print(f"Ordre Nr:{ID} er ferdig.")
    
    con.commit()
    con.close()

def listBurgers(): # Gir tilbake alle burgere
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM Burger")
    rows = cursor.fetchall()
    
        # Determine the longest width for each column
    header = ("Burger Nr.", "Navn")
    widths = [len(cell) for cell in header]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])

    # Construct formatted row like before
    formatted_row = ' '.join('{:%d}' % width for width in widths)
        
    print(formatted_row.format(*header))
    
    for Row in rows:
        print(formatted_row.format(*Row))
    con.close()
