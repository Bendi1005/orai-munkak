from random import randint


diakok = []

nev = input('Kérem a tanuló nevét: ')

while nev != 'VÉGE':
    diakok.append(nev)
    nev = input('Kérem a tanuló nevét: ')

print(diakok)


feleloSorszama = randint(0,len(diakok)-1)
print(f'A felelő {diakok[feleloSorszama]}')

