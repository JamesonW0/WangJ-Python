symptom = str(input('enter symptom'))
if symptom.lower() == 'temperature':
    if str(input('Is your throat sore? (y/n)'))[0].lower() == 'y':
        print('You may have a throat infection.')
    elif str(input('Do you have a cough? (y/n)'))[0].lower() == 'y':
        print('You have a chest infection')
    else:
        print('You have a fever')
    # end if
else:
    print('Go home and get some sleep or go to your GP')
# end if
