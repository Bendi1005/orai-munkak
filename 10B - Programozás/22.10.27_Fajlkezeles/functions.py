from genericpath import exists
from data import students
from os import system
studentFile = 'students.txt'

def menu():
    choice = ''
    system('cls')
    print('-----------------------')
    print('0 - Kilép')
    print('1 - Új tanuló felvétele')
    print('2 - Tanulók listázása')
    # print('3 - Tanulók mentése fájlba')
    # print('4 - Tanulók beolvasása fájlból')
    choice = input('Válasszon egy menüpontot: ')
    return choice

def newStudent():
    print('Új tanuló felvétele')
    name = input('Kérem a tanuló nevét: ')
    students.append(name)
    saveStudentToFile(name)
    print('Tanuló sikeresen felvételre került.')

def showStudents():
    print('Tanulók listája:')
    for student in students:
        print(f'\t{student}')

def saveStudentToFile(student):
    file = open(studentFile, 'a', encoding='utf-8')
    file.write(student + '\n')
    file.close()

def saveToFile():
    file = open(studentFile, 'w', encoding='utf-8')
    for student in students:
        file.write(student + '\n')
    file.close()
    print('Sikeres mentés.')

def loadFromFile():
    if exists(studentFile):
        file = open(studentFile, 'r', encoding='utf-8')
        for row in file:
            students.append(row.strip()) #strip - eltávolítja a whitespace-eket (szóköz, enter, tab) a string elejéről, végéről
        file.close()
        # print('Sikeres betöltés.')        