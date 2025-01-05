# BURGER QUEEN: SQL-applikasjon i Python

## **Oppgave beskrivelse**
Du har blitt hyret inn av den nyoppstartede bedriften “Burger Queen”. Burger Queen er et nytt konsept som ønsker å utfordre burgerbransjen med sine fantastiske burgere! Per nå tilbyr de kun to typer burgere; “Whopper Queen” og “Triple Cheesy Princess”.
De ønsker et felles system med databaseintegrasjon, som både kundene og deres ansatte kan benytte for å holde oversikt over ordre og lagerbeholdningen sin.

----

### Dette er ønskene bedriften har til systemet:
Som nyoppstartet bedrift ønsker de et enkelt tekstbasert program der brukere skal kunne registrere kjøp av burgere og se sine ordre. Brukere skal kunne opprette brukere og logge inn. Ordrenummer skal kobles til den innloggede brukeren. Sjefen for Burger Queen ønsker ikke å bruke ekstra prosessorkraft på sikkerhet, så passord skal lagres i klartekst.

Systemet skal kunne registrere burgere, der hver burger har en mengde med ingredienser. 

Det samme tekstbaserte systemet skal også kunne støtte egen innlogging av ansatte. De ansatte skal kunne logge inn i applikasjonen og kunne se de ulike ordrene i systemet. 

Ansatte skal kunne se inventar av ingredienser - samt redusere ingredienser i inventaret når en burger blir produsert. 

## Installering

````bash
$ pip install -r requirements.txt

$ python3 Burger-Queen.py
````

For Docker

````bash
$ docker build -t burgerqueen .

$ docker run -it burgerqueen
````