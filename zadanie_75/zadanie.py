def szyfruj(napis,A,B):
    zaszyfrowany = ""
    for litera in napis:
        aski = ord(litera)
        numer = aski - 97
        numer = numer * A + B
        numer = numer % 26
        znakS = chr(numer + 97)
        zaszyfrowany += znakS
    return zaszyfrowany

with open("zadanie_75/tekst.txt") as plik:
    tekst = plik.readline()

print(tekst)
wyrazy = tekst.split()
print(wyrazy)
for wyraz in wyrazy:
    if wyraz[0] == "d" and wyraz[-1] == "d":
        print(wyraz)
for wyraz in wyrazy:
    if len(wyraz) >= 10:
        print(szyfruj(wyraz,5,2))

with open("zadanie_75/probka.txt") as plik:
    for linia in plik:
        napisy = linia.split()
        for a in range(26):
            for b in range(26):
                if szyfruj(napisy[1],a,b) == napisy[0]:
                    print(napisy,a,b)
                    break