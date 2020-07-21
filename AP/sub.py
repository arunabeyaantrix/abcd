# Python code for finding the 
# maximum length of AP 
def maxlenAP(a, n, d): 
	# key = starting element of an AP, 
	# value = length of AP 
	m = dict() 

	
	maxt = 1

	
	for i in range(n): 
		if (a[i] - i * d) in m: 
			m[a[i] - i * d] += 1
		else: 
			m[a[i] - i * d] = 1
		print(m)

	 
	for it in m: 
		if m[it] > maxt: 

			 
			maxt = m[it] 

	return maxt 

if __name__ == "__main__": 
	n, d = 10, 3
	a = [1, 4, 2, 5, 20, 11, 56, 100, 20, 23] 
	print(maxlenAP(a, n, d)) 

# This code is contributed by 
# sanjeev2552 
