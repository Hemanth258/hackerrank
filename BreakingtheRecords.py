def breakingRecords(scores):
    h = 0
    l = 0
    arr = [scores[0]]
    for i in scores:
        if min(arr) > i:
            l+=1
        elif max(arr) < i:
            h+=1
        arr.append(i)
    return h,l
print(breakingRecords([10,5,20,20,4,5,2,25,1]))