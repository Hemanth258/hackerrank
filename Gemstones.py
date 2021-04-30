def gemstones(arr):
    a = set(arr[0])
    for i in range(1,len(arr)):
        temp = set(arr[i])
        a = a.intersection(temp)
    return len(a)
