def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i
print(lonelyinteger([1,1,2]))