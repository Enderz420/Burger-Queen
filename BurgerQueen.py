# En bruker skal kunne logge inn i applikasjonen med riktig brukernavn og passord
# En bruker skal kunne registrere en ordre med hvilken burger og antall
# En bruker skal kunne se ordrene sine 
# En bruker som er ansatt skal kunne se alle ordre
# En bruker som er ansatt skal kunne se inventaret av ingredienser
# En bruker som er ansatt skal kunne markere en ordre som fullført, og systemet skal trekke fra brukte ingredienser fra inventaret
from db import loginUser, checkInventory, checkUserAnsettelse, checkUser, checkOrders, addOrder, removeOrder, createUser, completeOrder
from os import get_terminal_size
import time
import sys

isLoggedIn = False # default value
isAnsatt = False # default value
username = None # default value


def main(): # TODO: Format output to be more prettier
    term_size = get_terminal_size()
    print('=' * term_size.columns)
    font = """
            $$$$$$$\                                                           $$$$$$\                                          
            $$  __$$\                                                         $$  __$$\                                         
            $$ |  $$ |$$\   $$\  $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\        $$ /  $$ |$$\   $$\  $$$$$$\   $$$$$$\  $$$$$$$\  
            $$$$$$$\ |$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$ |  $$ |$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ 
            $$  __$$\ $$ |  $$ |$$ |  \__|$$ /  $$ |$$$$$$$$ |$$ |  \__|      $$ |  $$ |$$ |  $$ |$$$$$$$$ |$$$$$$$$ |$$ |  $$ |
            $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$   ____|$$ |            $$ $$\$$ |$$ |  $$ |$$   ____|$$   ____|$$ |  $$ |
            $$$$$$$  |\$$$$$$  |$$ |      \$$$$$$$ |\$$$$$$$\ $$ |            \$$$$$$ / \$$$$$$  |\$$$$$$$\ \$$$$$$$\ $$ |  $$ |
            \_______/  \______/ \__|       \____$$ | \_______|\__|             \___$$$\  \______/  \_______| \_______|\__|  \__|
                                        $$\   $$ |                               \___|                                        
                                        \$$$$$$  |                                                                            
                                        \______/                                                                             
            """
    for s in font:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.001)
    print('=' * term_size.columns)
    print("Velkommen til Burger Queens nye bestillingsportal")
    print("Hva vil du gjøre?")
    while True:    
        if not isLoggedIn:
            Login()
        if isAnsatt:
            print("""
            Meny: 
                1: Sjekk aktive brukere 
                2: Vis lager
                3: Ordre """)

            user_input = int(input("Vennligst oppgi valg: "))
            match user_input:
                case "1":
                    checkUser()
                case "2":
                    listInventory(username)
                case "3":
                    Ordre()
                case _:
                    break
        else:
            user_input = int(input("Vennligst oppgi valg: "))
            match user_input:
                case "1":
                    addOrder(burger=int(input("Hvilken burger vil du bestille?")), username=username)
                case _:
                    break
        
    
def Ordre():
    print("ordre")
    print("""
          Valg: 
            1: Sjekk bestillinger på en bruker 
            2: Marker en bestilling som ferdig for bruker 
            3: Fjerne bestilling !!! Gjør dette etter du har markert en bestilling som ferdig !!! """)

    user_input = str(input("Vennligst oppgi valg: "))
    match user_input:
        case "1":
            checkOrders(username)
        case "2":
            checkOrders(username)
            completeOrder(ID=int(input("Hvilken ordre er du ferdig med?")))
        case "3":
            checkOrders(username)
            removeOrder(ID=int(input("Hvilken ordre vil du fjerne")))
        case _:
            pass
    
    
def Login():
    global isAnsatt
    global isLoggedIn
    global username
    print("login")
    print("OBS! Case sensitive!")
    username=str(input("Vennligst oppgi brukernavn: "))
    if checkUser(username):
        print("Du har ikke bruker!")
        print("Du må lage en bruker for å bruke programmet")
        User()
    if loginUser(username, password=str(input("Oppgi passord: "))):
        isLoggedIn = True
        if checkUserAnsettelse(username):
            print("Du er ansatt!")
            isAnsatt = True
        else:
            print("Du har bruker men er ikke ansatt")
            
    else:
        print("Du har ikke en bruker!")
    
def User():
    global username
    print("Registrer ny bruker")
    username = str(input("Vennligst oppgi et unikt brukernavn"))
    createUser(username, password=str(input("Vennligst oppgi et passord som du husker!")))
    
def listInventory(username): # TODO: Remove later
    if isLoggedIn & isAnsatt:    
        print("oascnas")
        checkInventory(username)
    else:
        print("Du har ikke tilgang til dette!")



if __name__ == "__main__":
    main()
    