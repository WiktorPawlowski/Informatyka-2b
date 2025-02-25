
def jednolity(napis):
    for i in range(len(napis)-1):
        if napis[i] != napis[i+1]:
            return False
    return True

lista_napisow = []
with open("C:/Users/wik.pawlowski/Downloads/inf-pr-dane/dane/68/dane_napisy.txt") as plik:
    for linia in plik:
        lista_napisow.append(linia.split())
print(lista_napisow)
licznik = 0
for napis in lista_napisow:
    if napis[0] == napis[1]:
        if jednolity(napis[0]):
            licznik += 1
print(licznik)

print(sorted("burza"))
print(sorted("burza"))