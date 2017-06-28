students = []

class Student:

    #class sttribute
    school_name = "Springfield Elementary"

    # self is like this in other languages
    # __init__ is a special term used for a constructor method
    def __init__(self , name, student_id=332):
        self.name = name
        self.student_id =  student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

randy = Student("Randy")
print(randy)

print ("School: " + Student.school_name)

