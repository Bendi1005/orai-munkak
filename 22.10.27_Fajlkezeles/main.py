from functions import loadFromFile, menu, newStudent, saveToFile, showStudents

loadFromFile()
choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        newStudent()
        input()
    elif choice == '2':
        showStudents()
        input()
    # elif choice == '3':
    #     saveToFile()
    # elif choice == '4':
    #     loadFromFile()
