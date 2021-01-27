def equalizeArray(arr):
    d={}
    for i in arr:
        d[i]= arr.count(i)
    m = max(d.values())
    return len(arr)-m