
from data import *


def avgArea():
    sum = 0
    for area in areas:
        sum += area
    return sum/len(areas)

def countOverAvg():
    count = 0
    avg = avgArea()
    for area in areas:
        if area > avg:
            count += 1
    return count

def smallestIndex():
    minIndex = 0
    minValue = areas[0]
    for i, area in enumerate(areas):
        if area < minValue:
            minValue = area
            minIndex = i

    return minIndex

def allSmallestIndex():
    smallests = []
    minIndex = smallestIndex()
    minValue = areas[minIndex]
    for i, area in enumerate(areas):
        if area == minValue:
            smallests.append(i)
    return smallests

def searchCountry(needle):
    for i, country in enumerate(countries):
        if needle == country:
            return i
    return False


