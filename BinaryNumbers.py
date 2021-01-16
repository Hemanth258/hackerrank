n = 439
bi = bin(n)[2::]
print(bi)
ar = []
c = 0
for i in bi:
    i = '1'
    ar.append(i)
check = "".join(ar)
if bi == check:
    for i in bi:
        c+=1
    print(c)
elif (check != bi):
    arr = []
    c = 0
    for i in bi:
        if i == '1':
            c+=1
            arr.append(c)
        else:
            c = 0
    print(max(arr))

