n = int(input("Enter number of students"))
a = {}
for _ in range(n):
	name = input()
	marks = list(map(float, input().split()))
	a.update({name:marks})
query = input("enter name")
for k,v in a.items():
	if k == query:
		s = sum(v)/3
		print('%2f's)