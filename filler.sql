CREATE TABLE "Brukere" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Navn"	TEXT NOT NULL UNIQUE,
	"Passord"	TEXT NOT NULL,
	"Ansatt"	TEXT NOT NULL DEFAULT 'Nei',
	PRIMARY KEY("ID" AUTOINCREMENT)
);

CREATE TABLE "Ordre" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Hvem"	TEXT NOT NULL,
	"Hva"	TEXT NOT NULL,
	"Produsert"	TEXT NOT NULL DEFAULT 'Nei',
	PRIMARY KEY("ID" AUTOINCREMENT),
	CONSTRAINT "BurgerID" FOREIGN KEY("Hva") REFERENCES "",
	CONSTRAINT "Bruker" FOREIGN KEY("Hvem") REFERENCES "Brukere"("Navn")
);

CREATE TABLE "Ingredienser" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Ingrediens"	TEXT NOT NULL,
	"Hvor mye"	INTEGER NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);

CREATE TABLE "Burger" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Navn"	TEXT NOT NULL UNIQUE,
	"Ingredienser"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT),
	CONSTRAINT "Antall" FOREIGN KEY("Ingredienser") REFERENCES "Ingredienser"("Hvor mye")
);

insert into Brukere (ID, Navn, Passord, Ansatt)
values 
(1, "Geralt", "hesterbest", "Nei"),
(2, "Yennefer", "qwerty", "Nei"),
(3, "Roach", "pizza", "Nei"),
(4, "Jaskier", "nyttpassord", "Ja");

insert into Burgere (ID, Navn, Ingredienser)
Values
(1, "Whopper Queen", "Burgerbrød, burgerkjøtt, salat, tomat"),
(2, "Triple Cheese Princess", "Burgerbrød, burgerkjøtt, ost, salat, tomat"),
(3, "Kingdom Fries", "Potet");

Insert into Ordre (ID, Hvem, Hva, Produsert)
Values
(1, "Geralt", "Whopper Queen", "Ja"),
(2, "Geralt", "Whopper Queen", "Nei"),
(3, "Jaskier", "Triple Cheesy Princess" "Nei"),
(4, "Roach", "Whopper Queen", "Nei");

Insert into Ingredienser (ID,  Ingrediens, Hvor mye)
Values
(1, "Burgerbrød topp og bunn", 9001),
(2, "Burgerkjøtt", 10),
(3, "Salat", 8006),
(4, "Tomat", 1337),
(5, "Ost", 42),
(6, "Agurk", 666),
(7, "Potet", 420);