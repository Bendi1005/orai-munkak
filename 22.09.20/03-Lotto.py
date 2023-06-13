from random import randint


nyeroszamok = []

for i in range(0, 5):
    szam = randint(1, 90)
    nyeroszamok.append(szam)

print(f'Az ötöslottó e heti nyerőszámai: {nyeroszamok}')    

