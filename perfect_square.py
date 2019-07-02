import math
numb1,numb2=input().split()
numb1=int(numb1)
numb2=int(numb2)
num=numb1*numb2
root=math.sqrt(num)
if (int(root+0.5)**2==num):
  print("yes")
else:
  print("no")
