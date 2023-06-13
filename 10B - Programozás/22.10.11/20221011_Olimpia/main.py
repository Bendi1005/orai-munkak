import imp
from functions import *
from data import *


print(f'{sportagakSzama()} sportágban osztottak érmet az 1924-es Párizsi olimpián.')

print(f'{tobbMintEgyErem()} olyan sportág volt, ahol több, mint 1 érmet osztottak.')

print(f'Összesen {osszesErem()} aranyérmet oszottak')

print(f'A legtöbb érem amit kiosztanak egy sportágban: {legtöbbÉrem()}')

print(f'{sportagak[legtobbEremIndexe()]} sportágból osztották a legtöbb érmet.')

sportagNeve = input('Sportág neve: ')
ermekSzama = sportagErmekSzama(sportagNeve)

if ermekSzama == False:
    print('Nincs ilyen sportág')
else:
    print(f'{sportagNeve} sportágból {ermekSzama} érmet osztottak.')



