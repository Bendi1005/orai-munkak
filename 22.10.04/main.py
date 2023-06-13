
from functions import *
from names import *

#printStudentsWithNumbers()
#printReverseStudents()

Name = input('Kérek egy nevet: ')
if existsStudent(Name):
    print('Létezik ilyen nevű tanuló')
else:
    print('Nem létezik ilyen nevű tanuló')

if searchStudent(Name):
    print(f'A tanuló sorszáma: {searchStudent(Name)}')

print(f'A leghosszabb név: {searchNameByLength(longestNameLength())} ')    
print(f'A leghosszabb nén: {longestName()}')

print(f'Az osztálytanulók nevének átlagos hosszúsága, kerekítve tizedesre: {averageNameLength()}')

# # # #     # # # # #   #        #  #  ##########
#       #   #           # #      #  #  #
#       #   #           #  #     #  #  #
# # # #     #           #   #    #  #  #
#           # # # #     #    #   #  #  ##########
#           #           #     #  #  #           #
#           #           #      # #  #           #
#           # # # # #   #        #  #  ##########