inp1,inp2=input().split()
c=0
for i in range(len(inp1)):
    if inp1[i]==inp2[i]:
        continue
    else:
        c+=1
if c==1:
    print("yes")
else:
    print("no")
