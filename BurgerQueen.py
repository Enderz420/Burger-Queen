# En bruker skal kunne logge inn i applikasjonen med riktig brukernavn og passord
# En bruker skal kunne registrere en ordre med hvilken burger og antall
# En bruker skal kunne se ordrene sine 
# En bruker som er ansatt skal kunne se alle ordre
# En bruker som er ansatt skal kunne se inventaret av ingredienser
# En bruker som er ansatt skal kunne markere en ordre som fullført, og systemet skal trekke fra brukte ingredienser fra inventaret
from db import loginUser, checkInventory, checkUserAnsettelse, checkUser, checkOrders, addOrder, removeOrder, createUser, completeOrder, init, listBurgers
from os import get_terminal_size, system
from colorama import Fore, Style
import time
import sys
from datetime import datetime


isLoggedIn = False # default value
isAnsatt = False # default value
username = None # default value
term_size = get_terminal_size() # for buffers
side = None # default
c = datetime.now()
current_time = c.strftime('%H:%M:%S')

def main(): # TODO: Format output to be more prettier
    global username
    global isLoggedIn
    global isAnsatt
    global side
    side = "Start"
    
    system("cls")
    print(Fore.BLUE + '=' * term_size.columns)
    print(" ")
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
    for s in font: # kul type on effect!
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.001)
    print("") # vil ødelegge dividers
    print('=' * term_size.columns)
    print(" ")
    print(f"{Fore.LIGHTMAGENTA_EX}Klokken er {current_time}{Fore.RESET}")
    print(f"{Fore.LIGHTMAGENTA_EX}Side: {side}{Fore.RESET}")
    print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)
    print(Style.BRIGHT + "Velkommen til Burger Queens nye bestillingsportal")
    print("Hva vil du gjøre?" + Style.RESET_ALL)
    while True:    
        if not isLoggedIn: # Vil alltid starte her pga isLoggedIn
            print("Hovedmeny")
            print(Fore.GREEN + "1: Logg inn")
            print(Fore.GREEN + "2: Registrer")
            print(Fore.RED + "3: Avslutt programmet" + Fore.RESET)
            user_input = int(input("Velg et av alternativene "))
            match user_input: # Start skjerm
                case 1:
                    side = "Logg inn"
                    Login()
                case 2:
                    side = "Registrering"
                    User()
                case 3:
                    exit()
                case _:
                    pass
        if isAnsatt: # Ansatt panel
            isLoggedIn = True
            side = "Ansatt Meny"
            print(f"{Fore.LIGHTMAGENTA_EX}Side: {side}{Fore.RESET}")
            print(f"{Fore.LIGHTMAGENTA_EX}Bruker: {username}{Fore.RESET}")
            print(f"{Fore.LIGHTMAGENTA_EX}Klokken er {current_time}{Fore.RESET}")
            print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)
            print(Fore.LIGHTCYAN_EX + """
                1: Sjekk aktive brukere 
                2: Vis lager
                3: Ordre
                4: Reset Database
                5: Logg ut""" + Fore.RESET)
            print("")
            user_input = int(input("Vennligst oppgi valg: "))
            match user_input:
                case 1:
                    checkUser(username)
                case 2:
                    checkInventory(username)
                case 3:
                    side = Ordre
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
        else: # Bruker meny
            isLoggedIn = True
            side = "Meny"
            print(f"{Fore.LIGHTMAGENTA_EX}Side: {side}{Fore.RESET}")
            print(f"{Fore.LIGHTMAGENTA_EX}Bruker: {username}{Fore.RESET}")
            print(f"{Fore.LIGHTMAGENTA_EX}Klokken er {current_time}{Fore.RESET}")
            print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)
            print(f"Meny: \n{Fore.GREEN}1: Bestill mat! \n{Fore.BLUE}2: Sjekk dine bestillinger! \n{Fore.RED}3: Logg ut {Fore.RESET}")
            print(" " * term_size.columns)
            user_input = int(input("Vennligst oppgi valg: ")) 
            match user_input:
                case 1:
                    listBurgers()
                    burger=int(input("Hvilken burger vil du bestille? "))
                    addOrder(burger, username)
                case 2:
                    checkOrders(username)         
                case 3: # logg ut
                    isLoggedIn = False
                    username = None
                    isAnsatt = False
                    main()
                case _:
                    pass
        
    
def Ordre(): # Her kan du bestille og Håndtere aktive bestillinger.
    
    system("cls")
    print(f"{Fore.LIGHTMAGENTA_EX}Side: {side}{Fore.RESET}")
    print(f"{Fore.LIGHTMAGENTA_EX}Bruker: {username}{Fore.RESET}")
    print(f"{Fore.LIGHTMAGENTA_EX}Klokken er {current_time}{Fore.RESET}")
    print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)
    print("")
    print(f"""
          Valg: 
            {Fore.BLUE}1: Sjekk bestillinger på en bruker 
            {Fore.GREEN}2: Marker en bestilling som ferdig for bruker 
            {Fore.RED}3: Fjerne bestilling {Style.BRIGHT}!!! Gjør dette etter du har markert en bestilling som ferdig !!!{Style.RESET_ALL}{Fore.RESET} """)
    print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)
    print(" ")
    user_input = str(input("Vennligst oppgi valg: "))
    match user_input:
        case "1":
            checkOrders(username)
        case "2":
            checkOrders(username)
            completeOrder(ID=int(input(f"{Fore.GREEN}Hvilken ordre er du ferdig med?{Fore.RESET} ")))
        case "3":
            checkOrders(username)
            removeOrder(ID=int(input(f"{Fore.RED}Hvilken ordre vil du fjerne{Fore.RESET} ")))
        case _:
            pass
    
    
def Login(): # Logg in i programmet, sjekker om du er en bruker og er ansatt.
    global isAnsatt
    global isLoggedIn
    global username
    global side
    
    system("cls")
    print(f"{Fore.LIGHTMAGENTA_EX}Side: {side}{Fore.RESET}")
    print(f"{Fore.LIGHTMAGENTA_EX}Klokken er {current_time}{Fore.RESET}")
    print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)

    print("Du må logge inn for å bruke appen")
    print(f"{Style.BRIGHT}OBS! Case sensitive!{Style.RESET_ALL}")
    username=str(input("Vennligst oppgi brukernavn:\n"))
    if checkUser(username) is None or False:
        print(Fore.YELLOW + Style.BRIGHT + "Du har ikke bruker!" + Style.RESET_ALL + Fore.RESET)
        print(f"{Fore.RED}Du må lage en bruker for å bruke programmet{Fore.RESET}")
        User()
        
    if loginUser(username, password=str(input("Oppgi passord:\n"))): # klar tekst passord
        isLoggedIn = True
        if checkUserAnsettelse(username):
            print(Fore.GREEN + "Du er ansatt!" + Fore.RESET)
            isAnsatt = True
            system("cls")
        else:
            isAnsatt = False
            print(Fore.GREEN + "Du har bruker men er ikke ansatt" + Fore.RESET)
            system("cls")
    else:
        print(Fore.RED + "Du har ikke en bruker!" + Fore.RESET)
    
def User(): # Registerer ny bruker i prod
    global username
    system("cls")
    print(f"{Fore.LIGHTMAGENTA_EX}Side: {side}{Fore.RESET}")
    print(f"{Fore.LIGHTMAGENTA_EX}Klokken er {current_time}{Fore.RESET}")
    print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)
    print("Registrer deg selv!")
    print(" ")
    username = str(input(Fore.LIGHTGREEN_EX + "Vennligst oppgi et unikt brukernavn:\n" + Fore.RESET))
    createUser(username, password=str(input(Fore.LIGHTWHITE_EX + "Vennligst oppgi et passord som du husker:\n" + Fore.RESET)))
    print("Du vil nå bli logget inn automatisk")
    time.sleep(0.5)

if __name__ == "__main__":
    main()
    