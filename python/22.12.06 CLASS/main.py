from data import autok
from Auto import Auto


def feltolt():
    a = Auto('AA-BB-123',150,'Metál Piros', 2022)
    #a.rendszam = 'AA-BB-123'
    #a.gyartasiEv = 2022
    #a.szin = 'Metál Piros'
    #a.teljesitmeny = 150
    autok.append(a)

    a = Auto('AA-CC-345',110,'Sárga', 2021)
    #a.rendszam = 'AA-CC-345'
    #a.gyartasiEv = 2021
    #a.szin = 'Sárga'
    #a.teljesitmeny = 110
    autok.append(a)

def AutoBeker():
    a = Auto()
    print('Adja meg az auto adatait: ')
    a.rendszam = input('Rendszám: ')
    a.gyartasiEv = input('Gyártási év: ')
    a.szin = input('Szín: ')
    a.teljesitmeny = input('Teljesítmény: ')
    autok.append(a)

def AutoKiir(auto):
    print(f'Rendszám: {auto.rendszam}, Gyártási év {auto.gyartasiEv}, Szín: {auto.szin}, Teljesítmény: {auto.teljesitmeny}')

def OsszesAutoKiir():
    for auto in autok:
        AutoKiir(auto)

#AutoBeker()
feltolt()
OsszesAutoKiir()