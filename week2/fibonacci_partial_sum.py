def fibinocc(a,b):
    previous = 0
    current = 1
    res = 1
    lst = [None] * 2
    lst[0] = 0
    lst[1] = 1
    for i in range(b-1):
        previous,current = current, previous+current
        lst.append(current)
    print(lst)

    new_lst = lst[a:]

    print(new_lst)
    res = 0
    for i in range(0,len(new_lst)):
        res += new_lst[i]
    return res % 10


a,b = map(int,input().split())


print(fibinocc(a,b))

