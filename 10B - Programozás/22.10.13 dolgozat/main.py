from data import *
from functions import *

# A 2021-es olimpián tízpróbában a names listában felsorolt versenyzők indultak. Elért eredményeiket a points lista tartalmazza.
# Oldja meg az alábbi feladatokat!

# Írja ki a képernyőre, hogy a 2021-es olimpián hány atléta teljesített a 10 próbát!
print(f'A versenyen {countComptetitiors()} versenyző indult.')
# Írja ki a képernyőre, hány olyan versenyző volt, aki legalább 8600 pontot ért el!
print(f'{countAtLeast(8600)} versenyző ért el legalább 8600 pontot.')
# Írja ki a képernyőre a versenyzők pontszámának az átlagát!
print(f'A versenyzők pontszámának az átlaga {avgPoints()}.')
# Írja ki a képrnyőre a győztes versenyző nevét és pontszámát!
print(f'A verseny győztese {names[winnerIndex()]} {points[winnerIndex()]} pont eredménnyel')
# Kérje be a felhasználótól egy versenyző nevét és írja ki pontszámát!
# Ha nem találja, írja ki, hogy a versenyző nem indult a versenyen!
name = input('Versenyző neve:')
# index = search(namer)
index = search2(name)
if index == False:
    print('A versenyző nem szerepel a listában.')
else:
    print(f'A versenyző pontszáma {points[index]}.')


print(f'A legrosszabb versenyző {names[worst()]}, {points[worst()]} pontos eredménnyel.')

print('Versenyzők 8600 pont felett: ')
for name in competitorsOver(8600):
    print(f'\t{name}')

