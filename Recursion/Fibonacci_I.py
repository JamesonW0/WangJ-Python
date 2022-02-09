import time

def calc_fib(n_term):
    fibNumbers = [0, 1]
    for i in range(1, n_term):
        fibNumbers.append(fibNumbers[i] + fibNumbers[i - 1])
    return fibNumbers[-1]


startTime1 = time.time()
summing = 0
for i in range(3, 31):
    summing += calc_fib(i)

print(summing)
endTime1 = time.time()
print(endTime1 - startTime1)
