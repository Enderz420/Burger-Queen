# En bruker skal kunne logge inn i applikasjonen med riktig brukernavn og passord
# En bruker skal kunne registrere en ordre med hvilken burger og antall
# En bruker skal kunne se ordrene sine 
# En bruker som er ansatt skal kunne se alle ordre
# En bruker som er ansatt skal kunne se inventaret av ingredienser
# En bruker som er ansatt skal kunne markere en ordre som fullført, og systemet skal trekke fra brukte ingredienser fra inventaret
from db import loginUser, checkInventory, checkUserAnsettelse, checkUser, checkOrders, addOrder, removeOrder

isLoggedIn = False # default value
isAnsatt = False # default value
username = None # default value

def main(): # TODO: Format output to be more prettier
    print("console.log('break line')")
    print("Velkommen til Burger Queens nye bestillingsportal")
    print("Hva vil du gjøre?")
    while True:    
        if not isLoggedIn:
            Login()
        if isAnsatt:
            user_input = str(input("Vennligst oppgi valg: "))
            match user_input:
                case "a":
                    checkUser()
                case "b":
                    listInventory(username)
                case _:
                    break
        else:
            user_input = str(input("Vennligst oppgi valg: "))
            match user_input.lower():
                case "a":
                    Ordre()
                case "b":
                    listInventory(username)
                case _:
                    break
        
    
def Ordre(): # TODO: Remove later
    print("ordre")
    print("Hva vil du gjøre?")
    if isAnsatt:
        user_input = str(input("Vennligst oppgi valg: "))
        match user_input:
            case "a":
                checkUser()
            case "b":
                listInventory(username)
            case "c":
                checkOrders(username)
                removeOrder(ID=int(input("Hvilken ordre vil du fjerne")))
            case _:
                pass
    else:
        user_input = str(input("Vennligst oppgi valg: "))
        match user_input.lower():
            case "a":
                addOrder(burger=int(input("Hva vil du bestille?")), username=username)
            case "b":
                listInventory(username)
            case _:
                pass
    
    
    
def Login():
    global isAnsatt
    global isLoggedIn
    global username
    print("login")
    print("OBS! Case sensitive!")
    username=str(input("Vennligst oppgi brukernavn: "))
    if loginUser(username, password=str(input("Oppgi passord: "))):
        isLoggedIn = True
        if checkUserAnsettelse(username):
            print("Du er ansatt!")
            isAnsatt = True
        else:
            print("Du har bruker men er ikke ansatt")
            
    else:
        print("Du har ikke en bruker!")
    
    
def listInventory(username): # TODO: Remove later
    if isLoggedIn & isAnsatt:    
        print("oascnas")
        checkInventory(username)
    else:
        print("Du har ikke tilgang til dette!")



if __name__ == "__main__":
    main()
    