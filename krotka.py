#TUPLE - krotka
#Przechowuja tylko stale wartosci. Odczytywanie wyglada tak samo jak przy liscie za pomoca indeksowania.

#Krotki zapisuje sie przy uzyciu zwyklych nawiasow.

jan = ("Jan", "Kowalski", 33)
janina = ("Janina", "Nowak", (21,12,1978), "K")
print(jan)
print(janina)

print(janina[2]) #w tym wypadku wybrany zostanie element krotki

imie, nazwisko, wiek = jan   #przypisanie danych powyzej przez co mozna wywolac wszystkie atrybuty "jan"
print(nazwisko, wiek, imie)

#Odczyt elementow krotki przez podanie indeksow:
imie = jan[0]
nazwisko = jan[1]
wiek = jan[2]

print(jan[0])
print(jan[1])
print(jan[2])

