def diagonalDifference(arr):
    l = 0
    r = 0
    c = len(arr)-1
    for i in range(len(arr)):
        l = l + arr[i][i]
        r = r + arr[i][c]
        c-=1
    if l>r:
        return(l-r)
    else:
        return(r-l)