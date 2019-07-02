def c(l):
        di=1
        for x in range(0,len(l)-1):
                if l[x]!=l[x+1]:
                        di=di+1
                else:
                    break
        return di
num=int(input())
l=list(map(int,input().split()))
for x in range(0,len(l)):
        if l[x]>0:
                l[x]=1
        else:
             l[x]=0
si=""
for x in range(0,len(l)):
        k=l[x::]
        si=si+str(c(k))+" "
print(si.strip())
