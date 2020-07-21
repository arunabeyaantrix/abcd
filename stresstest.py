import random



while True:
	dist = random.randint(300,1000) 
	print(n)
	miles = random.randint(10,1500)
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