import random

def maximum_productFast(arr):
	n = len(arr)
	max_index1 = -1
	for i in range(n):
		if(max_index1 == -1 or arr[i] > arr[max_index1]):
			max_index1 = i
	max_index2 = -1
	for j in range(n):
		if((j != max_index1) and (max_index2 == -1 or arr[j] > arr[max_index2])):
			max_index2 = j
	print(max_index1,max_index2)
	return(arr[max_index1]*arr[max_index2])

def maximum_product(arr):
	n = len(arr)
	max_product = 0
	for i in range(n):
		for j in range(i+1, n):
			if(arr[i] * arr[j] > max_product):
				max_product = arr[i] * arr[j]
	return max_product

while True:
	n = random.randint(0,4) + 2
	print(n)
	arr = []
	for i in range(0,n):
		arr.append(random.randint(0,10))
	for i in range(n):
		print(arr[i],end=" ")
	print("\n")
	res1 = maximum_productFast(arr)
	res2 = maximum_product(arr)
	if(res1 != res2):
		print("Wrong answer" +' '+ str(res1) + ' '+ str(res2))
		break
	else:
		print("OK")