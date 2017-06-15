student_names = ['Randy', 'Brad', 'Anna']

# 0 is Randy, 1 is Brad, 2 is Anna
# -1 is Anna, -2 is Brad, -3 is Randy (no such thing as -0)
print(student_names)
student_names[0]='Peggy'
student_names[2]='Shannan'
#student_names[3]='Lydia' # this will error out - out of range as student_names was initialized as a 3 element array
student_names.append('Lydia') #add to end of list
print(student_names)
if 'Randy' in student_names == True:
    print('Randy is still there')
else:
    print('Randy is out of here')
listlength = len(student_names)
print('Length of student name list is: ')
print (str(listlength))

# del student_names[2] would remove 'Shannan' from the list
del student_names[2]
print(student_names)
# python lists are similar in concept to arrays

#list slicing ignore first element, get the rest
print(student_names[1:])
print(student_names[1:-1])
student_names = ['Brad', 'Peggy', 'Shannan', 'Lydia']
print(student_names[1:])
print(student_names[1:-1])
print(student_names[1:-1]) == ['Peggy', 'Shannan']

