from Tornasz import Tornasz

tornaszok : list[Tornasz] = []

file = open('torna.csv', 'r', encoding='utf-8')
file.readline()
for row in file:
    egyTornasz = Tornasz(row.strip())
    tornaszok.append(egyTornasz)
file.close

for item in tornaszok:
    print(item.nev)

#min = 1
#minIndex = -1
#for index,item in enumerate(tornaszok):
#    if item.korlat != '':
#        korlat = int(item.korlat)
#       if korlat > min:
#            min = korlat
#            minIndex = index




# print(f'2. Feladat\nÖsszesen {len(tornaszok)} versenyző indult a versenyen')
# print(f'\n3. Feladat\nKorláton {tornaszok[22].nev} szerezte meg az aranyérmet')
# print()




