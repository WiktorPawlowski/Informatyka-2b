ciagi = []
with open("C:/Users/wiktor/Documents/GitHub/gra-pygame-projekt_janek_wiktor/Informatyka-2b/zadanie_63/ciagi.txt") as plik:
    for linia in plik:
        ciagi.append(linia.strip())
print(ciagi)
for i in range(len(ciagi)):
    if ciagi[i][:len(ciagi[i])//2] == ciagi[i][len(ciagi[i])//2:]:
        print(ciagi[i])
licznik = 0
for i in range(len(ciagi)):
    if "11" not in ciagi[i]:
        licznik += 1
print(licznik)

liczby = []
for i in range(len(ciagi)):
    liczby.append(horner(ciagi[i],2))
print(liczby)