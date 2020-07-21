arr = [int(i) for i in input().split()]
n = len(arr)
count = 0
for i in range(n):
	for j in range(n-i-1):
		if arr[j] > arr[j+1]:
			arr[j],arr[j+1] = arr[j+1], arr[j]
			count+= 1
print(arr)
print("No of swaps = " + str(count))
