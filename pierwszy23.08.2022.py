i = 2
print(type(i))

f = 2.56634
print(type(f))

c = 0.5 + 1j
print(type(c))

print(float(i), int(f),  c)


#typ logiczny (prawda i falsz)
a = 2>1
print(a)
b = 1>2
print(b)
print(type(b))

#indeksowanie

napis = ("Ala ma kota")
print(napis[::1])
print(napis[::2])


zmienna = 127
print(zmienna)
print(type(zmienna))
print(type("zmienna"))
zmienna = "127"*127
print(zmienna)
print(type(zmienna))

#dodawanie roznych typow zmiennych
napis = "Ala ma kota, a kot ma psa"
liczba_calkowita = 2

print(napis + liczba_calkowita)

#roznych typow zmiennych nie da dodac sie do siebie

#konkatenacja 
print(napis + (str(liczba_calkowita)))

