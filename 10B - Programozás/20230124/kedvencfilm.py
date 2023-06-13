from math import floor


def óraperc( perc):
    ora = floor(perc/60)
    perc = perc % 60
    return str(ora) + 'óra' + str(perc) + 'perc' 

for i in range(3):
    film = input('Add meg egy film cimét! ')
    hossz = int(input('Hány perces a film? '))
    print(f'A {film} című film {óraperc(hossz)} ')


