


time = int(input('Hány órás visszaszámlálást tervezünk? '))

totalTime = time

for i in range(time, 0, -1):
    print(f'Visszaszámlálás: {i}')
    choose = input('Fel kell függeszteni a visszaszámlálást, (I/N)?')
    if choose == 'i' or 'I':
        totalTime += 1
print(f'A rakéta a visszaszámlálást követően ennyi órával indult: {totalTime}')



