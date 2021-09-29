trigger = int(input('enter trigger'))

if trigger == 1:
    movementGround = int(input('enter ground sensor status'))
    movementFirst = int(input('enter first floor sensor status'))
    if movementGround == 1:
        print('alarm on, intrusion on the ground floor')
    # end if
    if movementFirst == 1:
        print('alarm on, intrusion on the first floor')
    # end if
