def checkIsAP(arr):
	d = arr[1]-arr[0]
	for i in range(n-1):
		if arr[i+1]- arr[i] != d:
			return(False)
	return True

n = int(input())
arr = [int(i) for i in input().split(None,n)[:n]]
arr.sort()
print("Yes") if(checkIsAP(arr, n)) else print("No") 