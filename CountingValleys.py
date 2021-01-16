def countingValleys(steps, path):
    arr = []
    c = 0
    count = 0
    for i in path:
        if i == 'U':
            c = c+1
            arr.append(c)
        elif i == 'D':
            c = c-1
            arr.append(c)
        if c == 0 and arr[len(arr)-2] <0:
            count +=1
    return count