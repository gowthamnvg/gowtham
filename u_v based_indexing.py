inp1,inp2=map(int ,input().split())
l=list(map(int,input().split()))
c=[]
for x in range(inp2):
    u,v=map(int,input().split())
    for y in range(u-1,v):
        c.append(l[y])
    a=min(c)
    print(a)
