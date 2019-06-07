var=int(input())
n=var
c=0
while (n!=1):
    n=n//2
    c=c+1
temp=2**c
if (var==temp):
    print("yes")
else:print("no")
