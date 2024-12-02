DROP TABLE IF EXISTS Ordre;
DROP TABLE IF EXISTS Burger;
DROP TABLE IF EXISTS Ingredienser;
DROP TABLE IF EXISTS Brukere;
DROP TABLE IF EXISTS BurgerHasIngredienser;

CREATE TABLE IF NOT EXISTS "Brukere" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Navn"	TEXT NOT NULL UNIQUE,
	"Passord"	TEXT NOT NULL,
	"Ansatt"	TEXT NOT NULL DEFAULT 'Nei',
	PRIMARY KEY("ID" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Ingredienser" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Ingrediens"	TEXT NOT NULL,
	"HvorMye"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Burger"(
	"ID"	INTEGER NOT NULL UNIQUE,
	"Navn"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("ID" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Ordre" (
	"ID" INTEGER NOT NULL UNIQUE,
	"Hvem"	TEXT NOT NULL,
	"Hva"	TEXT NOT NULL,
	"Produsert"	TEXT NOT NULL DEFAULT 'Nei',
	PRIMARY KEY("ID" AUTOINCREMENT),
	CONSTRAINT "BurgerID" FOREIGN KEY("Hva") REFERENCES "Burger"("Navn"),
	CONSTRAINT "Bruker" FOREIGN KEY("Hvem") REFERENCES "Brukere"("Navn")
);

CREATE TABLE IF NOT EXISTS "BurgerHasIngredienser" (
	"BurgerID" INTEGER NOT NULL,
	"IngrediensID" INTEGER NOT NULL,
	CONSTRAINT "FK_BurgerID" FOREIGN KEY ("BurgerID") REFERENCES "Burger"("ID"),
	CONSTRAINT "FK_IngrediensID" FOREIGN KEY ("IngrediensID") REFERENCES "Ingredienser"("ID")
);

INSERT INTO Brukere (ID, Navn, Passord, Ansatt)
Values 
(1, "Geralt", "hesterbest", "Nei"),
(2, "Yennefer", "qwerty", "Nei"),
(3, "Roach", "pizza", "Nei"),
(4, "Jaskier", "nyttpassord", "Ja");

INSERT INTO Burger (ID, Navn)
Values
(1, "Whopper Queen"),
(2, "Triple Cheese Princess"),
(3, "Kingdom Fries");


INSERT INTO Ingredienser (ID,  Ingrediens, HvorMye)
Values
(1, "Burgerbrød topp og bunn", 9001),
(2, "Burgerkjøtt", 10),
(3, "Salat", 8006),
(4, "Tomat", 1337),
(5, "Ost", 42),
(6, "Agurk", 666),
(7, "Potet", 420);

INSERT INTO Ordre (ID, Hvem, Hva, Produsert)
Values
(1, "Geralt", "Whopper Queen", "Ja"),
(2, "Geralt", "Whopper Queen", "Nei"),
(3, "Jaskier", "Triple Cheese Princess", "Nei"),
(4, "Roach", "Whopper Queen", "Nei");

INSERT INTO BurgerHasIngredienser (BurgerID, IngrediensID)
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(2, 5),
(3, 7)