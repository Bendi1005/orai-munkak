

from data import *
from functions import allSmallestIndex, avgArea, countOverAvg, searchCountry, smallestIndex


print(f'Az országok száma: {len(countries)}')
#print(f'Az országok száma: {len(teruletek)}')
print(f'Az átlag területnél ({round(avgArea())} km2) nagyobb országok száma: {countOverAvg()}. ')
smallest = smallestIndex()
print(f'A legkisebb ország területe: {areas[smallest]} km2', end='. ')
print('Ezek az országok: ')
for i in allSmallestIndex():
    print(f'\t{countries[i]}', end=', \n')
print()


country = input('Ország: ')
result = searchCountry(country)
if result == False:
    print('Nincs ilyen ország.')
else:
    print(f'Az ország mérete: {areas[result]}')




