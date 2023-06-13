from calendar import c
import math


oldal1 = float(input('Első oldal:'))
oldal2 = float(input('Második oldal:'))
oldal3 = float(input('Harmadik oldal:'))

if oldal1 + oldal2 > oldal3 and oldal1 + oldal3 > oldal2 and oldal2 + oldal3 > oldal1:
    print(" A háromszög szerkezthető.")
    print('A háromszög kerülete:', oldal1 + oldal2 + oldal3)
    s = (oldal1 + oldal2 + oldal3) / 2
    t = math.sqrt(s * (s - oldal1) * (s - oldal2) * (s - oldal3))
    print('A háromszög területe:', t)
    
else:
    print("A háromszög nem szerkeszthető")

