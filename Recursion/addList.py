list_to_calc = [3, 6, 2, 8, 1]


def calc(to_calc):
    if len(to_calc) == 0:
        return 0
    else:
        return calc(to_calc[1:]) + to_calc[0]
    # end if
# end function


print(calc(list_to_calc))
