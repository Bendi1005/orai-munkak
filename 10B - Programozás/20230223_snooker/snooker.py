from Player import Player

players : list[Player] = []

file = open('snooker.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    players.append(Player(row.strip()))
file.close()

print(f'3. Feladat: a világranglistán {len(players)} versenyző szerepel.')

sum = 0
for item in players:
    sum += item.Prize
print(f'4. Feladat: a versenyzők átlagosan {sum/len(players):.2f} fontot keresnek')

max = -1
maxIndex = -1
for index,item in enumerate(players):
    if item.Country == 'Kína' and max < item.Prize:
        max = item.Prize
        maxIndex = index

print(f'5. Feladat: A legjobban kereső kíinai versenyző:')
print(f'\tHelyezés: {players[maxIndex].Position}')
print(f'\tNév: {players[maxIndex].Name}')
print(f'\tOrszág: {players[maxIndex].Country}')
print(f'\tNyeremény: {players[maxIndex].Prize * 380:,} Ft')

norvegia = False
for item in players:
    if item.Country == 'Norvégia':
        norvegia = True
        break
if norvegia:
    print(f'6. Feladat: A versenyzők között van norvég versenyző.')
else:
    print(f'6. Feladat: A versenyzők között nincs norvég versenyző.')
for item in players:
    if item.Country == 'Slócia':
        print(f'6+1. Feladat A versenyzők közt van Skót versenyző')
        break
else:
    print(f'6+1. Feladat A versenyzők közt van Skót versenyző')

stats = {}
for item in players:
    if item.Country in stats.keys():
        stats[item.Country] += 1
    else:
        stats[item.Country] = 1

print('7. Feladat: statisztika')
for key, value in stats.items():
    print(f'\t{key} - {value}')





