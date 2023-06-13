
osszdiak = int(input('Összes diák száma:'))
bukott = int(input('Bukott diákok száma:'))

atment = osszdiak - bukott

atmentszazalek = atment / osszdiak * 100

print(f'Átment tanulók százaléka: {atmentszazalek}%')