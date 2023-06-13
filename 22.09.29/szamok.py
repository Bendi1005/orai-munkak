from random import randint


szamok = []

def feltolt():
    for i in range(randint(5,25)):
        szamok.append(randint(-100,100))

def megszamlalas():
    darab = 0
    for szam in szamok:
        if szam > 0:
            darab += 1
    return darab
            
def pozitivAtlag():
    osszeg = 0
    darab = 0
    for szam in szamok:
        if szam > 0:
            osszeg += szam 
            darab += 1
    return osszeg / darab

def legnagyobb():
    max = szamok[0]
    for szam in szamok:
        if max < szam:
            max = szam
    return max

def legkisebb():
    min = szamok[0]
    for szam in szamok:
        if min > szam:
            max = szam
    return min

def eldontes(keresettSzam):
    for szam in szamok:
        if szam == keresettSzam:
            return True
    return False

def kereses(keresettSzam):
    for i in range(len(szamok)):
        if szamok[i] == keresettSzam:
            return i
    return False







