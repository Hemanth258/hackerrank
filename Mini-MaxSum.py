def miniMaxSum(arr):
    c = 0
    f = []
    for i in arr:
        arr.pop(c)
        f.append(sum(arr))
        arr.insert(c,i)
        c+=1
    print(min(f),max(f))