arr = [int(i) for i in input().split()]
for i in range(0,len(arr)):
	for j in range(i+1,len(arr)):
		if arr[j] < arr[i]:
			temp = arr[j]
			arr[j] = arr[i]
			arr[i] = temp 
print(arr)