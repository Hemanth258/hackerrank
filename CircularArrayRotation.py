def circularArrayRotation(a, k, queries):
    for i in range(k):
        p = a.pop()
        a.insert(0,p)
    f = []
    for i in queries:
        f.append(a[i])
    return f