# Notacja lista.metoda() (np.: lista.sort(), lista.append())
# jest przykładem programowania obiektowego (OOP = Object Oriented Programming),
# ponieważ obiekt jakim jest lista ma zdefiniowaną funkcję dostępną przez notację ..
# Sprawdzić wszystkie metody można w Ipython używając autokompletowania (Tab)

# Slide Type
# Lista ma wiele użytecznych metod
# .append(x) – dodaje x do listy
# .remove(x) – usuwa pierwszy x z listy
# .pop() – usuwa i zwraca ostatni element listy
# .insert(i, x) – wstawia x przed indeksem i
# .extend(x) – dodaje na koniec listy dodatkową zmienną iterowalną x
# .count(x) – zwraca ilość wystąpień x
# .index(x) – zwraca indeks pierwszego wystąpienia x
# .sort() – sortuje listę rosnąco
# .reverse() – sortuje listę w odwróconym porządku



lista = [1, 'Berta', 3,4,5, 'kot', -10.75, 3.14]
lista.insert(2,'zebra')
print(lista)
lista.pop()
print(lista)


# Funkcje działające na sekwencjach (listach, ciągach znaków oraz krotkach)
# len() – zwraca ilość elementów
# reversed() – zwraca obiekt zawierający odwróconą sekwencję
# sorted(lista) – zwraca kopię listy posortowanej rosnąco
# sorted(lista, reverse=True) – zwraca kopię listy w odwrotnym porządku
# enumerate() – zwraca obiekt zawierający indeksy i elementy sekwencji


