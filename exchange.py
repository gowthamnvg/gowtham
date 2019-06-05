inp1=input()
inp1=list(inp1)
for i in range(0,len(inp1),2):
    inp1[i],inp1[i+1]=inp1[i+1],inp1[i]
print(''.join(inp1))
