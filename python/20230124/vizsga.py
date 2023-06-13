
def check(point):
    if point >= 48:
        return True
    else:
         return False


name = ''

while name != '':
    name = input('Add meg a vizsgázó nevét! ')
    point = int(input('Add meg a pontszámát!'))
    if check(point):
        print(f'{name} vizsgája sikeres.')
    else:
        print(f'{name} vizsgája sikertelen.')




