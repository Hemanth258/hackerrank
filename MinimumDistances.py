def minimumDistances(a):
    f = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i<j and a[i]-a[j] == 0:
                f.append(j-i)
    if not f:
        return -1
    else:
        return min(f)