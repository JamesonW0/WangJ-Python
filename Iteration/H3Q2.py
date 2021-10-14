password = 'Tues1212'
for i in range(0, 3):
    entry = input('enter password')
    if password == entry:
        print('Password accepted')
        break
    else:
        print('Password rejected')
    # end if
# next i
