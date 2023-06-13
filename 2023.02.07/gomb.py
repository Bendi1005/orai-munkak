from math import pi


r = float(input('Adja meg a gömb sugarát: '))
while True:
    print(f'A gömb térfogata: {round(4*(r*r*r)*pi/3,2)}')
    print(f'A gömb felszíne: {round(4*r*r*pi,2)}')


