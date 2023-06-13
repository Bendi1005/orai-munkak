


from random import randint


diakok = ['Miliczki Áron','Mizser Bálint','Molnár Bendegúz','Neuberger Flórián','Nyári Patrik','Reizinger Krisztofer','Schosz András','Schwéger Alíz','Sebestyén Krisztián','Skultéty Hunor','Szabó Kornél','Szabó Tamás Benjamin','Tóth Lehel','Tüskés Bálint','Ványik Alex','Varga Ádám Tamás','Varga Kornél']


ujra = 'i'
while ujra == 'i' and len(diakok) > 0:
    felelokSorszama = randint(0,len(diakok)-1)
    print('Felelő: ', diakok[felelokSorszama])
    diakok.remove(diakok[felelokSorszama])
    print(f'Lehetséges felelők száma: {len(diakok)}')
    if (len(diakok) > 0):
        ujra = input('Új felelő (i/n): ')



