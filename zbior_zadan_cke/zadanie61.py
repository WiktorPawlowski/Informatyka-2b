ciagi = []
with open("C:/Users/wiktor/Documents/GitHub/gra-pygame-projekt_janek_wiktor/Informatyka-2b/zbior_zadan_cke/ciagi.txt") as plik:
    for linia in plik:
        liczby = [int(liczba) for liczba in linia.split()]
        if len(liczby) > 1:
            ciagi.append(liczby)

print(ciagi)
licznik = 0
maks = 0
for ciag in ciagi:
    roznica = ciag[1] - ciag[0]
    for i in range(1, len(ciag)):
        if roznica !=ciag[i] - ciag[i-1]:
            break
    else:
        licznik += 1
        if roznica > maks:
            maks = roznica
print(licznik,maks)