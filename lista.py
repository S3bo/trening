# lista = [1,2,3,4,-5,-10]
#
# print(lista)
# print(type(lista))
#
# liczby = [0.1, 0.2, 0.3, 4.5, -7.3, 6.87, 10]
#
# print(type(liczby))
#
# imiona = ['Ala', 'Zygmunt', 'Alojzy', 'Boguslawa']
#
# print(imiona)
#
# print(type(imiona))


#mozliwe jest wykrawanie kawalkow listy stiosujac adnotacje
#
#
#
#lista[start:stop:krok]
#
#
#modyfikowanie list:
#
# lista=[2,3,5,7,9]
# lista[2:4] = ["pies", "a", '2']
# print(lista)

# Dodawanie kolejnych elementow na koncu list (uzycie append)
#
# lista = [1, 'Berta', 3,4,5, 'kot', -10.75, 3.14]
# lista.append('zebra')
# print(lista)

# dodawanie kolejnych elementow na i-tym indeksie(za pomoca insert. w tym przypadku na 2 pozycji listy
lista = [1, 'Berta', 3,4,5, 'kot', -10.75, 3.14]
lista.insert(2,'zebra')
print(lista)