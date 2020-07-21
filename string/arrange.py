string = input()
lower = []
upper =[]
for i in string:
	if i.isupper():
		upper.append(i)
	if i.islower():
		lower.append(i)
print(''.join(lower + upper))