from collections import defaultdict
a = defaultdict(list)
n,m = map(int, input().split())
for i in range(n):
	a[input()].append(i+1)
for j in range(m):
	usr = input()
	if usr in a:
		print(*a[usr])
	else:
		print('-1')