try:
    choice = int(input('Please choose by enter number: \n 1: Economy Car \n 2: Saloon Car \n 3: Sports Car \n'))
    if choice > 3 or choice < 1:
        raise ValueError
except ValueError:
    print('Invalid entry')
else:
    while True:  # SRC - I'm not sure why you need this and the break/continues? What are you trying to achieve?
        # if the user entered no, then the program will ask 'proceed or cancel' again, until the user enters yes.
        p_c = str(input('Proceed or cancel?'))
        if p_c[0].lower() == 'p':
            if str(input('Do you want to proceed? (y/n)'))[0].lower() == 'y':
                print('PROCEED. Have a nice day')
                break
            # end if
        else:
            if str(input('Do you want to cancel? (y/n)'))[0].lower() == 'y':
                print('CANCEL. Have a nice day')
                break
            # end if
        # end if
    # end while
# end try
