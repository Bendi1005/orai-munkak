from Dolgozo import Dolgozo

dolgozok : list[Dolgozo] = []

file = open('mobil.csv','r',encoding='utf-8')
for sor in file:
    dolgozok.append(Dolgozo(sor))
file.close()

print(f'{len(dolgozok)} dolgozónak van céges mobiltelefonja.')

letszam = 0
for item in dolgozok:
    if item.osztaly == 'Informatika':
        letszam += 1
print(f'Az informatika osztályon {letszam} embernek van céges mobiltelefonja.')

min = dolgozok[0].koltseg
minIndex = 0
max = dolgozok[0].koltseg
maxIndex = 0
for index,item in enumerate(dolgozok):
    if item.koltseg < min:
        min = item.koltseg
        minIndex = index
    if item.koltseg > max:
        max = item.koltseg
        maxIndex = index
print(f'A legnagyobb telefonköltség: {max} Ft. Dolgozó: {dolgozok[maxIndex].nev}')
print(f'A legkisebb telefonköltség: {min} Ft. Dolgozó: {dolgozok[minIndex].nev}')

osszeg = 0
for item in dolgozok:
    if item.osztaly == 'Marketing':
        osszeg += item.koltseg
print(f'A marketing osztály dolgozói összesen {osszeg} Ft értékben telefonáltak.')

osztalyok = []

print('Osztályok:')
for item in dolgozok:
    if item.osztaly not in osztalyok:
        osztalyok.append(item.osztaly)
        #print(f'\t{item.osztaly}')

osztalyok.sort()
print(osztalyok)


osztalyKoltseg = {}

for item in dolgozok:
    if item.osztaly not in osztalyKoltseg.keys():
        osztalyKoltseg[item.osztaly] = item.koltseg
    else:
        osztalyKoltseg[item.osztaly] += item.koltseg

print(osztalyKoltseg)

legmagasabbKoltseg = 0
legmagasabbOsztaly = ''
for key,value in osztalyKoltseg.items():
    if value > legmagasabbKoltseg:
        legmagasabbKoltseg = value
        legmagasabbOsztaly = key
print(f'A legtöbb telefonköltséget a(z) {legmagasabbOsztaly} generálta {legmagasabbKoltseg} Ft összegben')


file = open('tulkoltes.csv', 'w', encoding='utf-8')
for item in dolgozok:
    if item.kategoria * 10000 < item.koltseg:
        file.write(f'{item.nev};{item.koltseg - item.kategoria * 10000}\n')
file.close()






