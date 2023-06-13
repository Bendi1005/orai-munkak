import math



ido = int(input(f'Mennyi idő van most?(óó:pp)'))
splitted = ido.split(':')
ora = int(splitted[0])
perc = int(splitted[1])
ossesPerc = ora * 60 + perc
if ido >= 8 and ido < 16:
    print('A bolt nyitva van.')
    maradekOra = math.floor((16*60-ossesPerc)/60)
    maradekPerc = 60 - (ossesPerc%60)
    if maradekPerc==60:            
        maradekPerc = 0
    print(f'Ennyi időd van még oda érni: {math.floor((16 * 60 - ossesPerc) / 60)}óra {60 - (ossesPerc % 60)}')
else:
        print('A bolt zárva van.')






