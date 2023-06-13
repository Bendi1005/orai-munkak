from Fogadasi_fordulo import Fogadasi_fordulo

fordulok : list[Fogadasi_fordulo] = []

file = open('toto.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    fordulok.append(Fogadasi_fordulo(row.strip()))

file.close()

print('3. feladat: Toto')
print('3.1 feladat: Adatok beolvasása és tárolása')
print(f'3.2 feladat: Fogadási fordulók száma: {len(fordulok)}')

teiltalalatosDarab = 0
for item in fordulok:
    teiltalalatosDarab += item.T13p1
print(f'3.3 feladat: Telitalálatos szelvények száma {teiltalalatosDarab} darab')

for item in fordulok:
    if 'X' not in item.Eredmények:
        print('3.4 feladat: Volt döntetlen mentes forduló')
        break
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló')

