n = int(input())
my_str = "abcdefghijklmnopqrstuvwxyz"
lst = []
for i in range(n):
	s = '-'.join(my_str[i:n])
	lst.append(s[::-1] + s[1:])
width = len(lst[0])

for i in range(n-1,0,-1):
	print(lst[i].center(width,'-'))

for i in range(n):
	print(lst[i].center(width,'-'))