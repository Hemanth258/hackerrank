def aVeryBigSum(ar):
    st = str(ar[0])
    f = 0
    l = 0
    for i in ar:
        i = str(i)
        f = f + int(i[0])
        l = l + int(i[1:])
    l = str(l)
    return str(f)+st[1:len(st)-len(l)]+str(l)
print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))