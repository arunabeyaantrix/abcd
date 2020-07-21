n = int(input())
temp = n
res = 0
while temp > 0:
	digit = temp%10
	res += digit ** 3
	temp //= 10
if n == res:
	print("Armstrom")
else:
	print("Not")




#1345

