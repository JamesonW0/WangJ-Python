def getPword(attempt):
    while attempt != 0:
        if attempt == 1:
            entry_1 = input('enter password')
            if 8 >= len(entry_1) >= 6:
                attempt = 2
            # end if
        # end if
        if attempt == 2:
            entry_2 = input('enter password again')
            if entry_1 == entry_2:
                attempt = 0
            else:
                attempt = 1
            # end if
        # end if
    # end while
    print('password change successful')
    # end procedure


getPword(1)