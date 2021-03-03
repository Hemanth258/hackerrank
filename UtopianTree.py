def utopianTree(n):
    arr = [0]
    for i in range(n+1):
        if (i%2)==0:
            c = arr[i]+1
            arr.append(c)
        else:
            c = arr[i]*2
            arr.append(c)
    return (arr[n+1])