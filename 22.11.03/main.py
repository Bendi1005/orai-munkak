from functions import *

loadFromFile()
choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        showCompetitors()
    elif choice == '2':
        showResults2()
    elif choice == '3':
        addResult()
    elif choice == '4':
        deleteResult()

#loadFromFile()
#showCompetitors()
#showResults()
