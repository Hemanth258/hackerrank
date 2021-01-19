def bytree(a,se):
    pos = 0
    l = 0
    u = len(a)-1
    a.sort()
    print(a)
    for i in range(len(a)):
        m = (l+u)//2
        if a[len(a)-1]==se:
            pos = len(a)
        elif a[m] == se:
            pos = m+1
        else:
            if a[m]>se:
                u = m
                if a[u]==se:
                    pos = m
            else:
                l = m
                if a[l] == se:
                    pos = m
    return pos

f = bytree([7,12,8,4,45,99],4)
print(f)
