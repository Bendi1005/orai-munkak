from Mountain import mountain

mountains: list[mountain]= []




def readFromFile(fileName):
    file = open(fileName, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        mountains.append(mountain(row))
    file.close()

def averageHeight():
    sum = 0
    for mnt in mountains:
        sum += mnt.height
    return sum/len(mountains)

def highestMountain():
    maxIndex = 0
    for i, mnt in enumerate(mountains):
        if mnt.height > mountains[maxIndex].height:
            maxIndex = i
    return maxIndex

def higherThenInput(height):
    for mnt in mountains:
        if height < mnt.height:
            return True
    return False





def main():
    readFromFile('HegyekMo.csv')
    print(f'3. feladat: Hegycsúcsok száma: {len(mountains)} db.')
    print(f'4. feladat: Hegycsúcsok átlagos magassága: {averageHeight()}')
    print(f'5. feladat: A legmagasabb hegycsúcs adatai:')
    highest = highestMountain()
    print(f'Név: {mountains[highest].name}')
    print(f'Hegység: {mountains[highest].mountainRange}')
    print(f'Magasság: {mountains[highest].height}')
    height = input('6. feladat: Kérek egy magasságot:')
    if higherThenInput(height) == True:
        print(f'Van ennél magasabb hegycsúcs.')
    else:
        print(f'Nincs magasabb hegycsúcs.')




main()











