from multiprocessing import managers
from gomb import gombFelszin, gombTerfogat
from kocka import kockaFelszin, kockaTerfogat
from gúla import gulaTerfogat, gulaFelszin

def FelszinVagyTerfogat():
    valasz = ''
    while valasz != 'f' and valasz != 't':
        valasz = input('Felszín vagy térfogat érdekli? (f/t): ').lower()
    return valasz

def menu():
    valasz = ''
    while valasz != '1' and valasz != '2' and valasz != '0' and valasz != '3':
        print('\n0 - Kilépés')
        print('1 - Kocka felszín és térfogat számítás')
        print('2 - Gömb felszín és térfogat számítás')
        print('3 - Gúla felszín és térfogat számítás')
        valasz = input('Válasz: ')
    return valasz

valasz = ''
while valasz != '0':
    valasz = menu()
    if valasz == '1':
        a = float(input('A kocka oldala: '))

        if FelszinVagyTerfogat() == 'f':
            print(f'Felszín: {kockaFelszin(a)}')

        else:
            print(f'Térfogat: {kockaTerfogat(a)}')
    elif valasz == '2':
        r = float(input('A gömb oldala: '))

        if FelszinVagyTerfogat() == 'f':
            print(f'Felszín: {gombFelszin(r)}')

        else:
            print(f'Térfogat: {gombTerfogat(r)}')

    elif valasz == '3':
        a = float(input('A gúla alapjának oldala: '))
        magassag = float(input('A gúla magassága: '))
        if FelszinVagyTerfogat() == 'f':
            print(f'Felszín: {gulaFelszin(a, magassag)}')
        else:
            print(f'Térfogat: {gulaTerfogat(a, magassag)}')


        