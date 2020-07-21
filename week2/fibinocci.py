def  fib_series(a):
	if(a <= 1):
		return a
	else:
		return fib_series(a-1) + fib_series(a-2)

n = int(input())
for a in range(n):
	print(fib_series(a))

