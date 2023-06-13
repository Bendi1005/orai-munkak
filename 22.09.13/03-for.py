
osszeg = 0

for i in range(10): 
    szam = int(input('Kérek egy számot: '))
    #osszeg = osszeg + szam

    osszeg += szam

print(f'A számok összege: {osszeg}')