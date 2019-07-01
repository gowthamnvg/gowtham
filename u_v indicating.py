inp1,inp2=map(int,input().split())
l=list(map(int,input().split()))
for x in range (1,inp1):
    l[x]+=l[x-1]
for x in range (inp2):
    s,temp=map(int,input().split())
    y=l[temp-1] if s==1 else l[temp-1]-l[s-2]
    print(y)
