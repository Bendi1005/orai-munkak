from ember import Ember

def keres(nev):
    for item in emberek:
        if item.teljesNev == nev:
            return item
    return False

emberek: list[Ember] = []

file = open('szavazatok.txt', 'r', encoding='utf-8')
for sor in file:
    emberek.append(Ember(sor.strip()))
file.close()

print(f'2. feladat: A választáson {len(emberek)} képviselőjelölt indult.')

nev = input('3. feladat: Képviselő neve: ')
eredmeny = keres(nev)
if eredmeny == False:
    print('Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!')
else:
    print(f'\tA jelölt a {eredmeny.kerulet}-s számú körzetben indult')
    print(f'\tA kapott szavazatok száma: {eredmeny.szavazatokSzama}')

osszesSzavazat = 0
for item in emberek:
    osszesSzavazat += item.szavazatokSzama

print(f'4. feladat: A választáson {osszesSzavazat} szavazó a jogosultak {(osszesSzavazat / 12345) * 100}%-a vett részt.')

max = 0
for item in emberek:
    if max < item.szavazatokSzama:
        max = item.szavazatokSzama

print(f'5. feladat: A legtöbb szavazat: {max}')

statisztika = {}

for item in emberek:
    if item.part not in statisztika.keys():
        statisztika[item.part] = item.szavazatokSzama
    else:
        statisztika[item.part] += item.szavazatokSzama


print('6. feladat')
for key,value in statisztika.items():
    if key == '-':
        print(f'\tFüggetlen: {value} szavazat')
    else:    
        print(f'\t{key}: {value} szavazat')

with open('TISZ.csv', 'w', encoding='utf-8') as file:
    file.write('Körzet;Név;Szavazatok száma\n')
    for item in emberek:
        if item.part == 'TISZ':
            file.write(f'{item.kerulet};{item.teljesNev};{item.szavazatokSzama}\n')

