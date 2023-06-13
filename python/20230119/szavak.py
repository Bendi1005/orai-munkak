szo1 = input('Adj meg egy szót! ')
szo2 = input('Adj meg egy másik szót! ')
if len(szo1) > len(szo2):
    print(f'A hosszabb szó: {szo1}')
elif len(szo2) > len(szo1):
    print(f'A hosszabb szó: {szo2}')
else:
    print('A két szó egyforma hosszú.')




