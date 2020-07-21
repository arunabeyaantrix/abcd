def lcm(a,b):
	if b == 0:
		return a
	else:
		rem = a%b
	return lcm(b,rem)
a,b = map(int,input().split())
print(a*b//lcm(a,b))
