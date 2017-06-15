student_names =['James', 'Katarina', 'Jessica', 'Bort', 'Mark', 'Frank Grimes', 'Max Power']

for name in student_names:
    if name == 'Mark':
        print('Found him! ' + name)
        break # no need to continue processing
    print('Currently testing ' + name)

for name in student_names:
    if name == 'Bort':
        continue  # Don't print 'Bort'
        print('Found him! ' + name)
    print('Currently testing ' + name)