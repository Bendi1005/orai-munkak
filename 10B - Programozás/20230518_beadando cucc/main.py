from Utca import Utca


Adozas : list[Utca] = []

file = open('utca.txt','r',encoding='utf-8')
file.readline()
for row in file:
    Adozas.append(Utca(row))
file.close()

print(f'2. Feladat. A mintában {len(Adozas)} telek szerepel.')
#for item in Adozas:
#    print(len())

adoszam = int(input(f'3. feladat. Egy utca tulajdonos adószáma:'))
for item in Adozas:
    if adoszam == item.adoszam:
        print(f'{item.utca} {item.hazszam}')
    else: 
        print('Nem szerepel az adatállományban.')
        break

def ado(adosav, alapterulet):
    for item in Adozas:
        if item.adosav == 'A':
            adofizet = 800 * alapterulet
        elif item.adosav == 'B':
            adofizet = 600 * alapterulet
        elif item.adosav == 'C':
            adofizet = 100 * alapterulet
        if adofizet < 10000:
            adofizet == 0
        return adofizet