from functions import *
import os


loadFromFile('autok.csv')

#while True:
#    printCar()
    
print(f'A nyilvántartásban {countCars()} darab autó van.')

speedLimit = int(input('Mennyinél gyorsabb autókat számoljunk meg?: '))
print(f'A megadott sebességnél ({speedLimit}) gyorsabb autók száma: {countCarBySpeed(speedLimit)}')

print(f'Volvo-k száma a rendszerben: {countCarByBrand("Volvo")}')
print(f'A Volvók átlag árai: {avgPriceByBrand("Volvo")}')
speedLimit = int(input('Mennyinél gyorsabb autókat számoljunk meg?:'))
if existsCarOverSpeedLimit(speedLimit):
    print(f'A megadott sebességnél ({speedLimit}) gyorsabb autók száma {countCarBySpeed}.')
else:
    print(f'Nem létezik ilyen autó.')

print(f'A nyilvántartásban szereplő autók átlag fogyasztása {avgConsumption():.2f}')

print(f'A nyilvántartásban szereplő autók átlag fogyasztása {round(avgConsumption())}')

platenumber = input(f'Írjad be a rendszámot HE:')
result = searchCarAndGiveBackAllDataYouKnowAboutItButWhenItDidntExistDontGiveBackAnything(platenumber)
if result == False:
    print('Nincs ilyen rendszám.')
else:
    print(f'Az autó adatai:')
    print(f'\t Márka:{result.Brand} ')
    print(f'\t Ára:{result.Price} ')
    print(f'\t Színe:{result.Color} ')
    print(f'\t Évjárat:{result.Year} ')


