n = int(input())
k = 2*n -2
for i in range(n):
	for j in range(k):
		print(end=" ")
	k = k-1
	for j in range(i+1):
		print('* ', end = "")
	print("\r")


def triangle(n): 
    k = 2*n - 2
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
        k = k - 1
        for j in range(0, i+1): 
            print("* ", end="") 
        print("\r") 
triangle(n)

for i in range(1,n+1):
	a = "* " * i
	print(str(a).center(4*n-2 ," "))