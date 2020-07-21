def palindrome(my_str):
	for i in range(int(len(my_str)/2)):
		if my_str[i] != my_str[len(my_str)-i - 1]:
			return False
		else:
			return True



def vowel_palindrome(my_str):
	b = ""
	for i in my_str:
		if i in "aeiou":
			b += i
	print(b)
	for i in range(int(len(b)/2)):
		if b[i] != b[len(b)-i - 1]:
			return False
		else:
			return True
my_str = input()
print(palindrome(my_str))

print("vowelPalindrome")

print(vowel_palindrome(my_str))


