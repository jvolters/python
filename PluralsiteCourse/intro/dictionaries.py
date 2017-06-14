#json like
#dictionaries in python

student = {
    'name':'Randy',
    'id': 15163,
    'feedback': None
}  #key-value pairs

print(student.keys())
print(student.get('name','Unknown'))


all_students = [
    {'name':'Randy','id': 15163,'feedback': None},
    {'name':'John','id': 15164,'feedback': None},
    {'name':'Tim','id': 15165,'feedback': None}
]

print(all_students[1:])
