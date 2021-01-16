n = int(input())
arr = list(map(int,input().split()))[:n]
m = max(arr)
res = []
for i in arr:
	if i < m:
		res.append(i)
res.sort()
rev = res[::-1]
print(rev[0])