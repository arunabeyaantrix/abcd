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
	return(arr[max_index1]*arr[max_index2])

n = int(input())
arr = [int(x) for x in input().split(None,n)[:n]]
print(maximum_productFast(arr))