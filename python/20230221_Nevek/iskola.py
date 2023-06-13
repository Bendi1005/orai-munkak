from Tanulo import Tanulo

tanulok : list[Tanulo] = []

def azonositoKeres(azonosito):
    for item in tanulok:
        if item.azonosito() == azonosito:
            return item
    return False

file = open('nevek.txt', 'r', encoding='utf-8')
for row in file:
    tanulok.append(Tanulo(row.strip()))
file.close()

print(f'3. Feladat: Az iskolába {len(tanulok)} tanuló jár. ')

leghosszabb = tanulok[0].nevHossz()
for item in tanulok:
    if leghosszabb < item.nevHossz():
        leghosszabb = item.nevHossz()

print(f'4. Feladat: A leghosszabb ({leghosszabb}karakter) nevű tanulók:')

for item in tanulok:
    if leghosszabb == item.nevHossz():
        print(f'\t{item.nev}')


print(f'5.Feladat: Azonosítók:')
print(f'\tElső: {tanulok[0].nev} - {tanulok[0].azonosito()}')
print(f'\tUtolsó: {tanulok[-1].nev} - {tanulok[-1].azonosito()}')

azonosito = input('6. Feladat: Kérek egy azonosítót [pl.: 4dvavkriJ]: ')
tanulo = azonositoKeres(azonosito)
if tanulo == False:
    print('Nincs megfelelő tanuló.')
else:
    print(f'{tanulo.ev} {tanulo.osztaly} {tanulo.nev}')


