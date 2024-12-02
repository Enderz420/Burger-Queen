# En bruker skal kunne logge inn i applikasjonen med riktig brukernavn og passord
# En bruker skal kunne registrere en ordre med hvilken burger og antall
# En bruker skal kunne se ordrene sine 
# En bruker som er ansatt skal kunne se alle ordre
# En bruker som er ansatt skal kunne se inventaret av ingredienser
# En bruker som er ansatt skal kunne markere en ordre som fullført, og systemet skal trekke fra brukte ingredienser fra inventaret
from db import checkUser, loginUser, checkInventory

isLoggedIn = False # default value
isAnsatt = False # default value

def main():
    print("console.log('break line')")
    print("Velkommen til Burger Queens nye bestillingsportal")
    print("Hva vil du gjøre?")
    
    
def Ordre():
    print("ordre")
    
    
    
def Login():
    global isAnsatt
    global isLoggedIn
    print("login")
    print("OBS! Case sensitive!")
    username=str(input("Vennligst oppgi brukernavn: "))
    loginUser(password=str(input("Oppgi passord: ")))
    if loginUser:
        checkUser(username)
        isLoggedIn = True
        if checkUser:
            print("Du er ansatt!")
            isAnsatt = True
        else:
            print("Du har bruker men er ikke ansatt")
            
    else:
        print("Du har ikke en bruker!")
    
    
def listInventory():
    if isLoggedIn & isAnsatt:    
        print("oascnas")
        checkInventory()
    else:
        print("Du har ikke tilgang til dette!")
checkUser("Geralt")
listInventory()