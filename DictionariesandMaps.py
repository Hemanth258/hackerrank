n = int(input())
d = {}
for i in range(n):
    a,b = input().split()
    d.update({a:b})
for i in range(n):
    s = input()
    if s in d.keys():
        print(s+"="+str(d[s]))
    else:
        print("Not found")
