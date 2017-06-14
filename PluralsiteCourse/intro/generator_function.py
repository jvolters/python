students = []


def read_file():# for loop to go through all the results from the bottom for loop's iteration and add to list (student)
    try:
        f = open("students.txt", "r") # second arg "r" is read mode;
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")


def read_students(f): # for loop to iterate over the file on hard drive
    for line in f:
        yield line


read_file()
print(students)
