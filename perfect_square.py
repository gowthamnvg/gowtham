import math
n1,n2=input().split()
n1=int(n1)
n2=int(n2)
n=n1*n2
r=math.sqrt(n)
if (int(r+0.5)**2==n):
  print("yes")
else:
  print("no")
