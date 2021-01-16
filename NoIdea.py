n,m = map(int, input().split())
arr  = input().split()
a =  set(input().split())
b =  set(input().split())
c = 0
r = 0
for i in arr:
    if i in a:
        c+=1
    elif i in b:
        r+=1
print(c-r)