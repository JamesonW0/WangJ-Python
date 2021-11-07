car_park = []


def car_park_init():
    car_park.clear()
    for i in range(0, 10):
        car_park.append([''] * 6)
    # next i
# end procedure


def park_a_car():
    reg_num = input('Enter your car\'s registration number')
    vacancy = 0
    while vacancy == 0:
        grid_ref = input('Enter the grid reference(row, column, separated by comma, max 9 character including space)')
        for i in range(len(grid_ref)):
            if grid_ref[i] == ',':
                row = int(grid_ref[:i]) - 1
                column = int(grid_ref[i + 1:]) - 1
            # end if
        # next i
        # noinspection PyUnboundLocalVariable
        if car_park[row][column] != '':
            print('There is a car in this place, enter another grid reference')
        else:
            vacancy = 1
            car_park[row][column] = reg_num
        # end if
    # end while


def remove_a_car():
    reg_num = input('Enter your car\'s registration number')
    remove = 0
    for i in range(10):
        for u in range(6):
            if car_park[i][u] == reg_num:
                car_park[i][u] = ''
                remove = 1
            # end if
        # next u
    # next i
    if remove == 1:
        print('remove successful')
    else:
        print('no car found')
    # end if
# end procedure


def display(grids):
    print('', end='      ')
    for i in range(0, 6):
        print('', i + 1, end='        ')
    # next i
    print('\n  ' + '------' * 10)
    for i in range(0, 10):
        if i == 9:
            print(i + 1, end='')
        else:
            print(i + 1, end=' ')
        # end if
        print('|', end='')
        for u in range(0, 6):
            front_space = int((9 - len(grids[i][u])) / 2)
            back_space = 9 - len(grids[i][u]) - front_space
            print(front_space*' ' + grids[i][u] + back_space*' ', end='')
            print('|', end='')
        # next u
        print('\n  ' + '------' * 10)
    # next i
# end procedure


def end():
    exit()
# end procedure
