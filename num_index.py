inp1=int(input())
inp2=input().split()
l=[]
for i in range(0,inp1):
  if(int(inp2[i])==i):
    l.append(inp2[i])
if(l==[]):
  print("-1")
else:
  l.sort()
  for j in range(0,len(l)):
    print(l[j],end=" ")
    
