n=list(input())
n1=[]
for i in n:
  if int(i)%2!=0:
    n1.append(i)
for i in n1:
  print(i,end=" ")
