student_names = ['Brad', 'Peggy', 'Shannan', 'Lydia']

# for loop in python
for name in student_names:
    print('Student name is {0}'.format(name))  #var name refers to {0}

# range
x = 0
for index in range(10):
    x += 10
    print('The value of X is {0}'.format(x))
    #0123456789 >-10,20,30,40,50,60,70,80,90,100
# but we can have total control over the range, like this...
print('')
x = 0
for index in range(5,10,1):
    x += 10
    print('The value of X is {0}'.format(x))
    # range is index {0 , 1, 2, 3, 4,5 6, 7, 8, 9]
    # 0123456789 >- 10,20,30,40,50?? expected 60,70,80,90,100
print('')
for index in range(5,10,2):
    x += 10
    print('The value of X is {0}'.format(x))
    # range is index {0 , 1, 2, 3, 4,5 6, 7, 8, 9]
    # 0123456789 >-60,70,80?? expected 60,80,100