def f(x):
    return x * x + 1

a = 0
b = 2
E = 1000

szerokosc = (b - a) / E
calka = 0
for i in range(E):
    h = f(a + i * szerokosc)
    calka += h * szerokosc

print(calka)
