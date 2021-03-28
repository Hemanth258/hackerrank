def insertionSort1(n, arr):
    el = 0
    mx = 0
    c = 0
    while c < n-1:
        c+=1
        if arr[c-1] > arr[c]:
            el = arr[c]
            mx = arr[c-1]
            arr[c] = mx
            while True:
                c-=1
                if el > arr[c]:
                    arr[c+1] = el
                    print(" ".join(map(str, arr)))
                    break
                elif c == 0:
                    mx = arr[c]
                    arr[c+1] = mx
                    arr[c] = mx
                    print(" ".join(map(str, arr)))
                    arr[c] = el
                    print(" ".join(map(str, arr)))
                elif el < arr[c]:
                    mx = arr[c]
                    arr[c] = mx
                    arr[c+1]= mx
                    print(" ".join(map(str, arr)))
                if c == 0:
                    break

print(insertionSort1(10, [2,3,4,5,6,7,8,9,10,1]))