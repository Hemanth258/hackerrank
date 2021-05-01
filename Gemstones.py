def gemstones(arr):
    a = set(arr[0])
    for i in range(1,len(arr)):
       a = a.intersection(set(arr[i]))
    print(len(a))
print(gemstones(['abcdde', 'baccd', 'eeabg']))