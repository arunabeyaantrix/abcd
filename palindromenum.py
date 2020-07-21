
def palnum(arr,n):
	for i in range(n//2):
		if arr[i] == arr[n-1-i]:
			return("Yes its a palindrome")
		else:
			return("Soory its not a palindrome")
n = int(input())
arr = [int(i) for i in input().split()[:n]]
print(palnum(arr,n))