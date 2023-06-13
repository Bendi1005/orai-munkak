from Pilota import Pilota

pilots : list[Pilota] = []

file = open('pilotak.csv', 'r', encoding='utf-8')
file.readline()
for row in file:
    pilots.append(Pilota(row.strip()))

file.close

print(f'3. Feladat: {len(pilots)}')
print(f'4. Feladat: {pilots[-1].name}')

print('5. Feladat:')
for item in pilots:
    if item.year < 1901:
        print(f'\t{item.name} {item.birthDate}')


min = 9999999
minIndex = -1
for index,item in enumerate(pilots):
    if item.startNumber != '':
        startNumber = int(item.startNumber)
        if startNumber < min:
            min = startNumber
            minIndex = index

print(f'6. Feladat: {pilots[minIndex].name} - {pilots[minIndex].country}')

stat = {}
for item in pilots:
    if item.startNumber in stat.keys():
        stat[item.startNumber] += 1
    else:
        stat[item.startNumber] = 1


print(f'7. Feladat: ', end='')
first = True
for key,value in stat.items():
    if key != '' and value > 1:
        
        if first != True:
            print(f', {key}', end='')
        else:
            print(f'{key}', end='')
            first = False


















