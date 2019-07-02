o,i=input().split()
o=int(o)
i=int(i)
count=0
l=list(map(int,input().split()))
for x in range(o):
    for y in range(x+1,o):
        ss=0
        ss=l[x]+l[y]
        if(ss==x):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
