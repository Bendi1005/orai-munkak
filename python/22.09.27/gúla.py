from math import sqrt


def gulaFelszin(a, magassag):
    magassagOldallap = sqrt(pow(a/2,2)+pow(magassag,2))
    teruletOldallap = a + magassagOldallap / 2
    teruletAlap = a * a
    return teruletAlap + teruletOldallap * 4

def gulaTerfogat(a, magassag):
    return a * a * magassag / 3


