from itertools import permutations
a,b = input().split()
c = "".join(sorted(a))
conv =  list(permutations(c,int(b)))
for i in conv:
    print("".join(i))
