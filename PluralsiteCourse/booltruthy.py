python_course = True
if python_course: # <--Not python_course == True
    print('This will execute')

aliens_found = None
if aliens_found: # Nothing prints because it is None, not True, not False; this is 'falsy'
    print('This will NOT execute')