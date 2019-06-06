a=int(input())
b=input().split()
x=[]
for i in range(0,a):
  if(int(b[i])==i):
    x.append(b[i])
if(x==[]):
  print("-1")
else:
  x.sort()
  for j in range(0,len(x)):
    print(x[j],end=" ")
    
