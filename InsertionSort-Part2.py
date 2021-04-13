def insertionSort2(n, arr):
    m = 0
    c = 0
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            while True:
                m = arr[i]
                if arr[c] > m:
                    arr.pop(arr.index(m))
                    arr.insert(c,m)
                    break
                c+=1
            c = 0
        print(" ".join(map(str, arr)))
print(insertionSort2(6, [3,4,7,5,6,2,1]))