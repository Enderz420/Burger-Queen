# En bruker skal kunne logge inn i applikasjonen med riktig brukernavn og passord
# En bruker skal kunne registrere en ordre med hvilken burger og antall
# En bruker skal kunne se ordrene sine 
# En bruker som er ansatt skal kunne se alle ordre
# En bruker som er ansatt skal kunne se inventaret av ingredienser
# En bruker som er ansatt skal kunne markere en ordre som fullført, og systemet skal trekke fra brukte ingredienser fra inventaret
from db import loginUser, checkInventory, checkUserAnsettelse, checkUser, checkOrders, addOrder, removeOrder, createUser, completeOrder, init
from os import get_terminal_size, system
from colorama import Fore, Style
import time
import sys

isLoggedIn = False # default value
isAnsatt = False # default value
username = None # default value


def main(): # TODO: Format output to be more prettier
    global username
    global isLoggedIn
    global isAnsatt
    
    
    system("cls")
    term_size = get_terminal_size()
    print(Fore.BLUE + '=' * term_size.columns)
    font = r"""
            ______                                   _____                           
            | ___ \                                 |  _  |                          
            | |_/ / _   _  _ __   __ _   ___  _ __  | | | | _   _   ___   ___  _ __  
            | ___ \| | | || '__| / _` | / _ \| '__| | | | || | | | / _ \ / _ \| '_ \ 
            | |_/ /| |_| || |   | (_| ||  __/| |    \ \/' /| |_| ||  __/|  __/| | | |
            \____/  \__,_||_|    \__, | \___||_|     \_/\_\ \__,_| \___| \___||_| |_|
                                __/ |                                              
                                |___/                                                                                                                         
            """
    for s in font:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.001)
    print("") # vil ødelegge dividers
    print('=' * term_size.columns)
    Style.RESET_ALL
    print("Velkommen til Burger Queens nye bestillingsportal")
    print("Hva vil du gjøre?")
    while True:    
        if not isLoggedIn:  
            print("Hovedmeny")
            print(Fore.GREEN + "1: Logg inn")
            print(Fore.RED + "2: Avslutt programmet" + Fore.RESET)
            user_input = int(input("Velg et av alternativene "))
            match user_input:
                case 1:
                    Login()
                case 2:
                    break
                case _:
                    break
        if isAnsatt:
            print("Meny:  ")
            print(Fore.LIGHTCYAN_EX + """
                1: Sjekk aktive brukere 
                2: Vis lager
                3: Ordre
                4: Reset Database
                5: Logg ut""" + Fore.RESET)

            user_input = int(input("Vennligst oppgi valg: "))
            match user_input:
                case 1:
                    checkUser(username)
                case 2:
                    listInventory(username)
                case 3:
                    Ordre()
                case 4:
                    init()
                case 5:
                    isLoggedIn = False
                    username = None
                    isAnsatt = False
                    main()
                case _:
                    pass
        else:
            print(f"Meny: \n{Fore.GREEN}1: Bestill mat! \n{Fore.RED}2: Logg ut{Fore.RESET}")
            user_input = int(input("Vennligst oppgi valg: "))
            match user_input:
                case 1:
                    burger=int(input("Hvilken burger vil du bestille?"))
                    addOrder(burger, username)
                case 2:
                    isLoggedIn = False
                    username = None
                    isAnsatt = False
                    main()
                case _:
                    pass
        
    
def Ordre():
    print("Side: Ordre")
    print('#' * get_terminal_size())
    print(f"""
          Valg: 
            {Fore.BLUE}1: Sjekk bestillinger på en bruker 
            {Fore.GREEN}2: Marker en bestilling som ferdig for bruker 
            {Fore.RED}3: Fjerne bestilling !!! Gjør dette etter du har markert en bestilling som ferdig !!!{Fore.RESET} """)
    print('#' * get_terminal_size())
    user_input = str(input("Vennligst oppgi valg: "))
    match user_input:
        case "1":
            checkOrders(username)
        case "2":
            checkOrders(username)
            completeOrder(ID=int(input("Hvilken ordre er du ferdig med? ")))
        case "3":
            checkOrders(username)
            removeOrder(ID=int(input("Hvilken ordre vil du fjerne ")))
        case _:
            pass
    
    
def Login():
    global isAnsatt
    global isLoggedIn
    global username
    print('#' * get_terminal_size())
    print('#' * get_terminal_size())
    print("Du må logge inn for å bruke appen")
    print(f"{Style.BRIGHT}OBS! Case sensitive!{Style.RESET_ALL}")
    print('#' * get_terminal_size())
    print('#' * get_terminal_size())
    username=str(input("Vennligst oppgi brukernavn: "))
    if checkUser(username):
        print(Fore.YELLOW + Style.BRIGHT + "Du har ikke bruker!")
        print("Du må lage en bruker for å bruke programmet")
        Style.RESET_ALL
        Fore.RESET
        User()
    if loginUser(username, password=str(input("Oppgi passord: "))):
        isLoggedIn = True
        if checkUserAnsettelse(username):
            print(Fore.GREEN + "Du er ansatt!")
            Fore.RESET
            isAnsatt = True
        else:
            isAnsatt = False
            print(Fore.GREEN + "Du har bruker men er ikke ansatt")
            Fore.RESET
            
    else:
        print(Fore.RED + "Du har ikke en bruker!")
        Fore.RESET
    
def User():
    global username
    print("Registrer ny bruker")
    username = str(input("Vennligst oppgi et unikt brukernavn "))
    createUser(username, password=str(input("Vennligst oppgi et passord som du husker! ")))
    
def listInventory(username): # TODO: Remove later
    if isLoggedIn & isAnsatt:    
        print("oascnas")
        checkInventory(username)
    else:
        print("Du har ikke tilgang til dette!")



if __name__ == "__main__":
    main()
    