# exception handling
student = {
    'name':'Randy',
    'id': 15163,
    'feedback': None
}  #key-value pairs

student['last_name'] = 'Kowalski'

try:
    last_name = student['last_name']
    numbered_last_name = 3 + last_name
except KeyError:
    print('Error finding last_name')
except TypeError as error:
    print('Cannot concatenate and int and a str')
    print(error)
except Exception: # generic handle anything exception
    print('Unknown error')
print('This code executes')
