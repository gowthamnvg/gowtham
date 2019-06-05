p,q=list(map(str,input().split()))
r=len(set(p))
s=len(set(q))
if r==s :
    print("yes")
else:
    print("no")
