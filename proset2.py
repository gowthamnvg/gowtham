n1,n2=map(int,input().split())
lis=list(map(int,input().split()))
n1=[]
lis.insert(0,0)
for y in range(n2):
     v=[]
     temp=0
     c,d=map(int,input().split())
     for i in range(c,d+1):         
         temp^=lis[i]     
     n1.append(temp)
for y in n1:
    print(y)
