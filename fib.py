inp=int(input())
first=0
second=1
for i in range(inp):
	print(second,end=" ")
	temp=first
	first=second
	second=temp+second
