value = float(input('enter value for the order'))
postage_code = int(input('Do you want guaranteed next day delivery for £5? (1 for yes, 2 for no)'))

if postage_code == 1:
    value += 5
elif value < 15:
    value += 3.5
# end if

print('You need to pay £' + str(value))
