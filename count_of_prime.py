n1,n2=input().split()
n1=int(n1)
n2=int(n2)
z=0
for i in range(n1,n2+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        z=z+1
print(z)
