from names import students

def printStudents():
    for student in students:
        print(student)


def printStudentsWithNumbers():
    for i in range(len(students)):
        print(f'{i+1}. {students[i]}')

def printReverseStudents():
    for i in range(len(students)-1, -1, -1):
        print(f'{i+1}. {students[i]}')

def existsStudent(nameToSearch):
    for student in students:
        if student == nameToSearch:
            return True
    return False

def searchStudent(nameToSearch):
    for i in range(len(students)):
        if nameToSearch == students[i]:
            return i 
    return False

def longestNameLength():
    longest = len(students[0])
    for student in students:
        if len(student) > longest:
            longest = len(student)
    return longest

def searchNameByLength(length):
    for student in students:
        if length == len(student):
            return student
    return False

def longestName():
    longest = len(students[0])
    longestName = students[0]
    for student in students:
        if len(student) > longest:
            longest = len(student)
            longestName = student
    return longestName

def averageNameLength():
    sum = 0
    for student in students:
        sum += len(student)
    return round(sum / len(students), 1)






# # # #     # # # # #   #        #  #  ##########
#       #   #           # #      #  #  #
#       #   #           #  #     #  #  #
# # # #     #           #   #    #  #  #
#           # # # #     #    #   #  #  ##########
#           #           #     #  #  #           #
#           #           #      # #  #           #
#           # # # # #   #        #  #  ##########