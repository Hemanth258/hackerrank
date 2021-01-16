n = int(input())
l = []
for j in range(n):
	args = input().split(" ")
	if args[0] == "insert":
		l.insert(args[1],args[2])
	elif args[0] == "print":
		print(l)
	elif args[0] == "remove":
		l.remove(int(args[1]))
	elif args[0] == "append":
		l.append(int(args[1]))
	elif args[0] == "sort":
		l.sort()
	elif args[0] == "pop":
		l.pop()
	elif args[0] == "reverse":
		l.reverse()