string = input()
position,charecter = input().split()
print(string[:int(position)] + charecter+string[int(position)+1:])
