inp1=int(input())
inp2=input().split()
s=0
for i in range(len(inp2)):
  s+=int(inp2[i])
print(s//len(inp2))
