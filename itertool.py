from itertools import permutations,combinations_with_replacement,combinations
s,n = input().split()
print("Permutations \n")
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep ='\n')

print("Combinations \n")
for j in range(1,int(n)+1):
	print(*[''.join(i) for i in combinations(sorted(s),j)],sep ='\n')

print(*[''.join(i) for i in combinations_with_replacement(sorted(s),int(n))],sep ='\n')

    