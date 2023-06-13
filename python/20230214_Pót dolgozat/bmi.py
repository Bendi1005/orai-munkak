testtömeg = float(input('Adja meg az ember súlyát kg-ban: '))
testmagasság = float(input('Adja meg az ember magasságát cm-ben: '))

testmagasságM2 = testmagasság/100 * testmagasság/100 

Tti = testtömeg / testmagasságM2

if Tti <= 16:
    valasz = 'Súlyos soványság'
elif 16 <= Tti <= 18.49:
    valasz = 'Soványság'
elif 18.5 <= Tti <= 24.49:
    valasz = 'Normális'
elif 25 <= Tti <= 29.99:
    valasz = 'Túlsúlyos'
else:
    valasz = 'Elhízás'



print(f'A testtömeg indexe: {round(Tti,2)}')
print(f'A testsúly osztálya: {valasz}')


