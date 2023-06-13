from Player import Player

players : list[Player] = []

file = open('fob2016.txt', 'r', encoding='utf-8')
for row in file:
    players.append(Player(row.strip()))

file.close()

print(f'3. Feladat: Játékosok száma: {len(players)}')

countWoman = 0
for item in players:
    if item.category == 'Noi':
        countWoman += 1
    

print(f'4. Feladat: A női versenyzők aránya: {countWoman/len(players)*100:.2f}%')

winnerWomanPoints = -1
winnerWoman = ''
for item in players:
    if item.category == 'Noi' and item.totalPoints() > winnerWomanPoints:
        winnerWomanPoints = item.totalPoints()
        winnerWoman = item

print('6. Feladat: A bajnok női versenyző')
print(f'\tNév: {winnerWoman.name}')
print(f'\tEgyesület: {winnerWoman.team}')
print(f'\tÖsszpont: {winnerWoman.totalPoints()}')

file = open('osszpontFF.txt', 'w', encoding='utf-8')
for item in players:
    if item.category == 'Felnott ferfi':
        file.write(f'{item.name};{item.totalPoints()}\n')
file.close()

stats = {}
for item in players:
    if item.team in stats.keys():
        stats[item.team] += 1
    else:
        stats[item.team] = 1

print('8. Feladat: Egyesület statisztika')
for key,value in stats.items():
    if key != 'n.a.' and value > 2:
        print(f'\t{key} - {value} fő')

print('9. Feladat: \t')
nevek = {}
for item in players:
    if item.firstName in nevek.keys():
        nevek[item.firstName] += 1
    else:
        nevek[item.firstName] = 1
for key, value in nevek.items():
    print(f'\t {key} - {value}')





