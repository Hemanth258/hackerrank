import math
def encryption(s):
    l = len(s)
    c = math.ceil(l**0.5)
    arr = []
    for i in range(c):
        arr.append(s[i::c])
    return " ".join(arr)