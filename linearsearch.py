n = int(input())
arr = [int(i) for i in input().split(None, n) [:n]]
k = int(input())
for i in range(n):
	if arr[i] == k:
		print("element found at index" + str(i))
	else :
		print("element not found")
