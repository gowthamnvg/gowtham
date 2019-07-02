inp1,inp2=map(int,input().split())
temp=[]
e=0
for i in range(inp1):
    temp.append(list(map(int,input().split())))   
for i in range(inp1):
    for s in range(inp2-1):
        for w in range(s+1,inp2+1):
            if temp[i][s:w]==[1]*len(temp[i][s:w]):
                 if all(temp[p+i][s:w]==[1]*len(temp[p+i][s:w]) for p in range(len(temp[i][s:w])-1)):
                     if len(temp[i][s:w])>e:
                        e=len(temp[i][s:w])
if len(temp)==1 and len(temp[0])==1 and temp[0][0]==1:
    print(1)
for i in range(e):
    print(*[1]*e)
