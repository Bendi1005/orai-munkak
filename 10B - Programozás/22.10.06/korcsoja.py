from random import randint


versenyzok = []

def birokPontszamai():
    pontok = []
    for i in range(7):
        pontok.append(randint(0,40) / 4)
    return pontok

def legjobbPont(pontok):
    max = 0
    for pont in pontok:
        if max < pont:
            max = pont
    return max

def legrosszabbPont(pontok):
    min = 99
    for pont in pontok:
        if min > pont:
            min = pont
    return min

def osszeg(pontok):
    szumma = 0
    for pont in pontok:
        szumma += pont
    return szumma

def pontszamGeneral():
    for i in range(10):
        pontszamok = birokPontszamai()
        osszpontszam = osszeg(pontszamok) - legjobbPont(pontszamok) - legrosszabbPont(pontszamok)
        versenyzok.append(osszpontszam)

def gyoztesPontszam():
    max = 0
    for versenyzo in versenyzok:
        if versenyzo > max:
            max = versenyzo
    return max

def gyoztesVersenyzo():
    maxi = 0
    for i in range(len(versenyzok)):
        if versenyzok[i] > versenyzok[maxi]:
            maxi = i
    return maxi

def atlagPontszam():
    osszeg = 0
    for versenyzo in versenyzok:
        osszeg += versenyzo
    return round(osszeg / len(versenyzok), 2)

def atlagAlattDb():
    darab = 0
    for versenyzo in versenyzok:
        if versenyzo < atlagPontszam():
            darab += 1
    return darab

# # # #     # # # # #   #        #  #  ##########
#       #   #           # #      #  #  #
#       #   #           #  #     #  #  #
# # # #     #           #   #    #  #  #
#           # # # #     #    #   #  #  ##########
#           #           #     #  #  #           #
#           #           #      # #  #           #
#           # # # # #   #        #  #  ##########