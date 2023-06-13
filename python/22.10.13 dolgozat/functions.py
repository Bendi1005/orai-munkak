from data import *

def countComptetitiors():
    return len(names)

def countAtLeast(min):
    count = 0
    for point in points:
        if point >= min:
            count += 1
    return count

def sumPoints():
    sum = 0
    for point in points:
        sum += point
    return sum

def avgPoints():
    return round(sumPoints() / len(names), 2)


def winnerIndex():
    winner = 0 
    for i in range(1, len(points)):
        if points[i] > points[winner]:
            winner = i
    return winner

def search(needle):
    for i in range(len(names)):
        if names[i].upper() == needle.upper():
            return i
    return False
            
def search2(needle):
    for i,name in enumerate(names):
        if name == needle:
            return i
    return False

def worst():
    worstIndex = 0
    for i, point in enumerate(points):
        if point < points[worstIndex]:
            worstIndex = i
    return worstIndex

def competitorsOver(limit):
    filteredNames = []
    for i, point in enumerate(points):
        if point > limit:
            filteredNames.append(names[i])


    return filteredNames






