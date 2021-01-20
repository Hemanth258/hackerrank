def cutTheSticks(arr):
    r = []
    for i in range(len(arr)):
        r.append(len(arr))
        arr = [j-min(arr) for j in arr]
        if len(arr) == 0:
            break
        else:
            c = min(arr)
            for i in range(arr.count(c)):
                arr.remove(c)
    if 0 in r:
        i = r.index(0)
        r.pop(i)
        return r
    else:
        return r