inp= int(input())
if inp>1:
	for i in range(2,inp):
		if(inp%i==0):
			print("yes")
			break
	else:
		print("no")
