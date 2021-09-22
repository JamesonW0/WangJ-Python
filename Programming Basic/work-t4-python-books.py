no_students = int(input('enter the number of students'))
no_books = int(input('enter the number of books'))

print('each student can get',no_books//no_students, 'books. there are', no_books%no_students, 'left over')