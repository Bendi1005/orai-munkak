from szamok import eldontes, feltolt, legkisebb, legnagyobb, szamok, megszamlalas, pozitivAtlag, kereses

feltolt()
print(szamok)
print(f'A számok között {megszamlalas()} darab pozitív van. ')
print(f'A pozitív számok átlaga: {pozitivAtlag()}')
print(f'A legnagyobb szám: {legnagyobb()}')
print(f'A legnagyobb szám: {legkisebb()}')
keresendo = int(input('Kerek egy számot: '))
if eldontes(keresendo):
    print('A megadott szám benne van a listában. ')
    print(f'A megadott szám sorszáma: {kereses(keresendo) + 1}')
else:
    print('A megadott szám NINCS benne a listában. ')

