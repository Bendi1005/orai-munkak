

from random import randint

atlag = 0
for i in range(5):
    dobas = randint(1,6)
    atlag += dobas
    print(dobas)

print(f'A dobások átlaga:  {atlag / 5}')
