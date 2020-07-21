
def fibinocc(n):
    if n < 2:
        return n
    else:
        previous = 0
        current = 1
        res = 1
        for i in range(n-1):
            previous,current = current, previous+current
            res += current
        return res

        
n = int(input())
print(fibinocc(n) % 10)

