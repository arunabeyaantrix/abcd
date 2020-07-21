n = int(input())

for i in range(1,n+1):
	for j in range(1,n+1):
		min = i if i<j else j
		print((n-min) +1, end="")
	for j in range(n - 1, 0, -1): 
		min = i if i<j else j
		print(n - min + 1, end = "")
	print("\n")





#Input : n = 3

#Output :

#1*2*3*10*11*12
#--4*5*8*9
#----6*7

#Input : n = 4

#Output :

#1*2*3*4*17*18*19*20
#--5*6*7*14*15*16
#----8*9*12*13
#------10*11