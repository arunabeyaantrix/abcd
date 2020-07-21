n = int(input())
arr = [[input(),float(input())] for i in range(n)]
arr.sort(key=lambda x: (x[1],x[0]))
print(arr)

names = [i[0] for i in arr]
marks = [i[1] for i in arr]

min_value = min(marks)

while marks[0] == min_value:
	marks.remove(marks[0])
	names.remove(names[0])
for x in range(len(marks)):
	if marks[x] == min(marks):
		print(names[x])