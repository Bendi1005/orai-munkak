from data import *


def sportagakSzama():
    return len(sportagak)

def tobbMintEgyErem():
    darab = 0
    for erem in ermekSzama:
        if erem > 1:
            darab += 1
    return darab

def osszesErem():
    osszeg = 0
    for erem in ermekSzama:
        osszeg += erem
    return osszeg

def legtöbbÉrem():
    max = 0
    for erem in ermekSzama:
        if erem > max:
            max = erem
    return max

def legtobbEremIndexe():
    maxSorszam = 0
    for i in range(len(ermekSzama)):
        if ermekSzama[i] > ermekSzama[maxSorszam]:
            maxSorszam = i
    return maxSorszam

def sportagErmekSzama(sportag):
    for i in range(len(sportagak)):
        if sportag.upper() == sportagak[i].upper():
            return ermekSzama[i]
    return False



