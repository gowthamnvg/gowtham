inp1,inp2=map(int,input().split())
inp3,inp4=map(int,input().split())
inp5,inp6=map(int,input().split())
inp7,inp8=map(int,input().split())
temp1=inp4-inp2
temp2=inp6-inp8
temp3=inp5-inp3
temp4=inp7-inp1
if temp1==temp2== temp3==temp4:
	print("yes")
else:
	print("no")
