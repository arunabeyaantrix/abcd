string = input()
string.lower()
temp_str = string[::-1]
if temp_str == string:
	print("Yes it is")
else:
	print("No its not a palindrome")