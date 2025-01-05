from db import loginUser, checkInventory, checkUserAnsettelse, checkUser, checkOrders, addOrder, removeOrder, createUser, completeOrder, init, listBurgers, listUsers
from os import get_terminal_size, system 
from colorama import Fore, Style # colorama for farger
import time
import sys 
from datetime import datetime # hente tid


isLoggedIn = False # default value
isAnsatt = False # default value
username = None # default value
term_size = get_terminal_size() # for buffers 
side = None # default

def main(): # main funksjon
    global username
    global isLoggedIn
    global isAnsatt
    global side
    side = "Start"
    
    font = r"""
                ______                                   _____                           
                | ___ \                                 |  _  |                          
                | |_/ / _   _  _ __   __ _   ___  _ __  | | | | _   _   ___   ___  _ __  
                | ___ \| | | || '__| / _` | / _ \| '__| | | | || | | | / _ \ / _ \| '_ \ 
                | |_/ /| |_| || |   | (_| ||  __/| |    \ \/' /| |_| ||  __/|  __/| | | |
                \____/  \__,_||_|    \__, | \___||_|     \_/\_\ \__,_| \___| \___||_| |_|
                                    __/ |                                              
                                    |___/                                                                                                                         
                """ # kreves for type on effect 

    system("cls") # sletter alt i terminalen fra før sånn at du får en ren opplevelse
    print(Fore.BLUE + '=' * term_size.columns)
    print(" ")
    for s in font: # kul type on effect!
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.005)
    print("") # vil ødelegge dividers
    print('=' * term_size.columns)
    print(" ")
    topBar(sys_cls=True, logo=True) # vil printe logo med 
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
                    login()
                case 2:
                    side = "Registrering"
                    user()
                case 3:
                    exit()
                case _:
                    pass
        if isAnsatt: # Ansatt panel
            isLoggedIn = True
            side = "Ansatt Meny"
            topBar(sys_cls=False, logo=False)
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
                    listUsers()
                    time.sleep(0.5)
                case 2:
                    checkInventory(username)
                    time.sleep(0.5)
                case 3:
                    side = "Ordre"
                    ordre()
                case 4: # reset
                    init() # database reset
                case 5: # logout
                    isLoggedIn = False
                    username = None
                    isAnsatt = False
                    main()
                case _:
                    pass
        else: # Bruker meny
            isLoggedIn = True
            side = "Meny"
            topBar(sys_cls=False, logo=False)
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
        
    
def ordre(): # Her kan du bestille og Håndtere aktive bestillinger.
    
    topBar(sys_cls=False, logo=False)
    print(f"""
          Valg: 
            {Fore.BLUE}1: Sjekk bestillinger på en bruker 
            {Fore.GREEN}2: Marker en bestilling som ferdig for bruker 
            {Fore.RED}3: Fjerne bestilling {Style.BRIGHT}!!! Gjør dette etter du har markert en bestilling som ferdig !!!{Style.RESET_ALL}{Fore.RESET} 
            {Fore.CYAN}4: Tilbake til hovedmeny{Fore.RESET}""")
    print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)
    print(" ")
    user_input = str(input("Vennligst oppgi valg: "))
    match user_input:
        case "1":
            checkOrders(username)
            ordre()
        case "2":
            checkOrders(username)
            completeOrder(ID=int(input(f"{Fore.GREEN}Hvilken ordre er du ferdig med?{Fore.RESET} ")))
            ordre()
        case "3":
            checkOrders(username)
            removeOrder(ID=int(input(f"{Fore.RED}Hvilken ordre vil du fjerne{Fore.RESET} ")))
            ordre()
        case "4":
            main()
        case _:
            pass
    
    
def login(): # Logg in i programmet, sjekker om du er en bruker og er ansatt.
    global isAnsatt
    global isLoggedIn
    global username
    global side
    
    topBar(sys_cls=True, logo=True)

    print("Du må logge inn for å bruke appen")
    print(f"{Style.BRIGHT}OBS! Case sensitive!{Style.RESET_ALL}")
    username=str(input("Vennligst oppgi brukernavn:\n"))
    if checkUser(username) is None or False:
        print(Fore.YELLOW + Style.BRIGHT + "Du har ikke bruker!" + Style.RESET_ALL + Fore.RESET)
        print(f"{Fore.RED}Du må lage en bruker for å bruke programmet{Fore.RESET}")
        user()
        
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
    
def user(): # Registerer ny bruker i prod
    global username
    topBar(sys_cls=True, logo=True)
    print("Registrer deg selv!")
    print(" ")
    username = str(input(Fore.LIGHTGREEN_EX + "Vennligst oppgi et unikt brukernavn:\n" + Fore.RESET))
    createUser(username, password=str(input(Fore.LIGHTWHITE_EX + "Vennligst oppgi et passord som du husker:\n" + Fore.RESET)))
    print("Du vil nå bli logget inn automatisk")
    time.sleep(0.5)

def topBar(sys_cls, logo): # topBar for applikasjonen som viser tid logo, bruker, side og wiper terminalen. Logo og CLS er 2 variabler som er enten true eller false

    c = datetime.now()
    current_time = c.strftime('%H:%M:%S')
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
    if sys_cls is True:
        system("cls")
    if logo is True:    
        print(" ")
        print(Fore.BLUE + '=' * term_size.columns)
        print(" ")
        print(font)
        print(" ") 
        print('=' * term_size.columns)
        print(" " + Fore.RESET)    
    print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)
    print(f"{Fore.LIGHTMAGENTA_EX}Side: {side}{Fore.RESET}")
    print(f"{Fore.LIGHTMAGENTA_EX}Klokken er {current_time}{Fore.RESET}")
    print(Fore.LIGHTYELLOW_EX + '-' * term_size.columns + Fore.RESET)

if __name__ == "__main__":
    main()
