inp1,inp2=input().split()
temp=abs(len(inp1)-len(inp2))
for i in range(len(inp1)):
    if len(inp2)==1 and inp2[i] in inp1:
        break
    if inp1[i]!=inp2[i]:
        temp+=1
print(temp)
