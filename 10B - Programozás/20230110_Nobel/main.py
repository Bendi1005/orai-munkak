from Awarded import Awarded

awardedList : list[Awarded] = []


def readFromFile(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        a = Awarded(row.strip())
        awardedList.append(a)
        
    file.close()

def searhByName(name):
    for awarded in awardedList:
        if awarded.firstname +' '+ awarded.lastname == name:
            return awarded
    return False

def SearchByTypeAndYear(type, year):
    for awarded in awardedList:
        if awarded.year == year and awarded.type == type:
            return awarded
    return False

def awardedSinceYear(Year):
    print(f'Az adott {Year} év után az alábbi emberek kaptak béke Nobel-díjat: ')
    for awarded in awardedList:
        if awarded.year >= Year and awarded.type == 'béke':
            print(f'\t{awarded.firstname} {awarded.lastname}')

kaksi = {}

def numberOfTypes():
    for awarded in awardedList:
        if awarded.type in kaksi.keys():
            kaksi[awarded.type] += 1
        else:
            kaksi[awarded.type] = 1




def main():
    readFromFile('nobel.csv')
    result = searhByName('Arthur B. McDonald')
    print(f'Arthur B. McDonald {result.type} nobel díjat-kapott, az alábbi évben: {result.year}')
    
    type = input('Adja meg a típust: ')
    year = int(input('Adja meg az évet: '))
    result = SearchByTypeAndYear(type, year)
    if result == False:
        print(f'Nincs találat')
    else:
        print(f'{year}-ban/ben az {type} nobel díjat kapta: {result.firstname} {result.lastname}')
    
    year = int(input('Adja meg az évet: '))
    awardedSinceYear(year)
    
    print(f'\t\nNobel-díj fajtáinak a száma')
    for key, value in kaksi.items():
        print(f'{key} - {value}')

main()






