szam1 = float(input('Első szám:'))
szam2 = float(input('Másik szám:'))
muvelet = input('Művelet (+-*/):')

if muvelet == '+' :
    print(szam1, '+', szam2, '=', szam1 + szam2)

elif muvelet == '-' :
    print(szam1, '-', szam2, '=', szam1 - szam2)

elif muvelet == '*' :
    print(szam1, '*', szam2, '=', szam1 * szam2)

elif muvelet == '/' :
    if szam2 == 0:
        print('0-val nem lehet osztani.')
    else:
        print(szam1, '/', szam2, '=', szam1 / szam2)
        


