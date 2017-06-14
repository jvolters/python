students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
        return students_titlecase


def print_students_titlecase():
    student_titlecase = get_students_titlecase()
    print (students_titlecase)


def add_student(name, student_id=332):
    student = {"name":name, "student_id": student_id}
    students.append(student)


def var_args(name, *args):
    print("name is: ",name)
    print("args are: ",args)


def var_args2(name, **kwargs):
    print("name is: ",name)
    print("args are: ",kwargs["description"], kwargs["feedback"], kwargs["Pluralsight_subscriber"])

student_list = get_students_titlecase()

add_student(name="Randy Volters", student_id=2815)

var_args("Randy", "Loves Python", None, "Hello", True)

var_args2("Randy", description="Loves Python", feedback=None, Pluralsight_subscriber=True)


