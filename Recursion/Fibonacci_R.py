import time


def calc_fib(n_term):
    if n_term == 0:
        return 0
    elif n_term == 1 or n_term == 2:
        return 1
    else:
        return calc_fib(n_term - 1) + calc_fib(n_term - 2)


startTime1 = time.time()
summing = 0
for i in range(3, 31):
    summing += calc_fib(i)
endTime1 = time.time()
print(endTime1 - startTime1)
