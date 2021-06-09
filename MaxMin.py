def maxMin(k, arr):
    arr.sort()
    m = arr[-1]
    for i in range(len(arr)-k+1):
        mi = arr[i]
        mx = arr[k-1]
        m = min(m,mx-mi)
        k = k+1
    return(m)

print(maxMin(3,[100,200,300,350,400,401,402]))