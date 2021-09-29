exam = int(input('enter exam result'))
attendance = int(input('enter the attendance'))
grade = ''

if attendance <= 90 or exam <= 70:
    grade = 'FAIL'
else:
    if exam > 90:
        grade = 'A'
    elif exam > 80:
        grade = 'B'
    else:
        grade = 'C'
    # end if
# end if

print('The student\'s result is', grade)
