from Result import Result

results:list[Result] = []

def readFromFile(fileName):
    file = open(fileName, 'r', encoding='utf-8')
    for row in file:
        results.append(Result(row))
    file.close()

def count(place):
    counter = 0
    for result in results:
        if result.place == place:
            counter += 1
    return counter

def totalPoints():
    sum = 0
    for item in results:
        sum += item.point()
    return sum

def countBySport(sport):
    count = 0
    for item in results:
        if item.sport == sport and item.place <= 3:
            count += 1
    return count

def printToFile(fileName):
    file = open(fileName, 'w', encoding='utf-8')
    for item in results:
        if item.sport == 'kajakkenu':
            file.write(f'{item.place} {item.members} {item.point()} kajak-kenu {item.kind}')
        else:
            file.write(f'{item.place} {item.members} {item.point()} {item.sport} {item.kind}')

    file.close

def mostMembers():
    most = 0
    mostIndex = 0
    for i, item in enumerate(results):
        if item.members > most:
            most = item.members
            mostIndex = i
    return mostIndex

def main():
    readFromFile('helsinki.txt')
    print('3. Feladat:')
    print(f'pontszerző helyezések száma: {len(results)}')
    print('4. Feladat:')
    print(f'Arany: {count(1)}')
    print(f'Ezüst: {count(2)}')
    print(f'Bronz: {count(3)}')
    print(f'Összesen: {count(1) + count(2) + count(3)}')
    print('5. Feladat:')
    print(f'Olimpiai pontok száma: {totalPoints()}')
    print('6. Feladat:')
    torna = countBySport('torna')
    uszas = countBySport('uszas')
    if uszas > torna:   
        print('Úszás sportágban szereztek több érmet.')
    elif uszas < torna:
        print('Torna sportágban szereztek több érmet.')
    else:
        print('Egyenlő volt az érmek száma.')
    printToFile('Helsinki2.txt')
    mostIndex = mostMembers()
    print('8. Feladat:')
    print(f'\t Helyezés: {results[mostIndex].place}')
    print(f'\t Sportág: {results[mostIndex].sport}')
    print(f'\t Versenyszám: {results[mostIndex].kind}')
    print(f'\t Sportolók száma: {results[mostIndex].members}')


main()
