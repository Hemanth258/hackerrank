def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i<j and i!=j and arr[i]+arr[j] == m:
                return (i+1,j+1)
print(icecreamParlor(4, [2, 2, 4, 3]))