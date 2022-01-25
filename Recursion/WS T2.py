def addToEven(n):
	if n - 2 == 0:
		return n
	else:
		return n + addToEven(n - 2)


print(addToEven(8))
