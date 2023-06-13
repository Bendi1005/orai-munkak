from random import randint


print('Melyik lottó legyen?')
print('1 - ötöslottó')
print('2 - hatoslottó')
print('3 - skandináv lottó')
valasz = input('Válasz (1-3): ')

if valasz == '1':
    LEGYNAGYOBB_SZAM = 90
    SZAMOK_DB = 5

elif valasz == '2':
    LEGYNAGYOBB_SZAM = 45
    SZAMOK_DB = 6

elif valasz == '3':
    LEGYNAGYOBB_SZAM = 35
    SZAMOK_DB = 7

else:
    print('Hibás válasz, alapértelmezett: Ötös lottó')
    LEGYNAGYOBB_SZAM = 90
    SZAMOK_DB = 5

lottoszamok = []

if SZAMOK_DB > LEGYNAGYOBB_SZAM:
    print('Lehetetlen a megadott adatokkal lottószámokat generálni')
else:
    while len(lottoszamok) < SZAMOK_DB:
        szam = randint(1, LEGYNAGYOBB_SZAM)
        if szam not in lottoszamok:
            lottoszamok.append(szam)


    lottoszamok.sort()
    print('Az e heti nyerőszámok: ', lottoszamok)




