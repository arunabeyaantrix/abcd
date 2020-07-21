def gcd(a,b):
	if(b == 0):
		return a
	else:
		rem = a%b
		return(gcd(b,rem))
a = int(input())
b = int(input())
print(gcd(a,b))