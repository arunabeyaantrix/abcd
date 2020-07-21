arr = [12,11,13,5,6]

for i in range(1,len(arr)):
	key=arr[i]
	j = i - 1
	while key < arr[j] and j >= 0:
		arr[j], arr[j+1] = arr[j+1], arr[j]
		j-=1
print(arr)
