from Car import Car
from data import cars


def loadFromFile(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        newCar = Car(row.strip())
        cars.append(newCar)
    return cars

def printCar():
    for car in cars:
        print(f'{car.PlateNumber} - {car.Brand} - {car.Year} - {car.Cm3} - {car.Price} - {car.Doors} - {car.Speed} - {car.HP} - {car.Consumption} - {car.Color} - {car.FirstOwner}')

def countCars():
    return len(cars)

def countCarBySpeed(speed):
    counter = 0
    for car in cars:
        if speed < car.Speed:
            counter += 1
    return counter

def countCarByBrand(Brand):
    counter = 0
    for car in cars:
        if Brand == car.Brand:
            counter += 1
    return counter

def avgConsumption():
    sum = 0
    for car in cars:
        sum += car.Consumption
    return sum / countCars()

def avgPriceByBrand(Brand):
    sum = 0
    count = 0
    for car in cars:
        if Brand == car.Brand:
            sum += car.Price
            count += 1
    return sum / count

def existsCarOverSpeedLimit(limit):
    for car in cars:
        if car.Speed > limit:
            return True
    return False

def searchCarAndGiveBackAllDataYouKnowAboutItButWhenItDidntExistDontGiveBackAnything(platenumber):
    for car in cars:
        if car.PlateNumber == platenumber:
            return car
    return False

