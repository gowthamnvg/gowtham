inp1=int(input())
L=list()
for x in range(inp1):
    h=input().split()
    h=[int(d) for d in h]
    for k in h:
        L.append(k)
L.sort()
for x in L:
    print(x,end=" ")
