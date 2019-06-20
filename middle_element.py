inp=input()
if len(inp)%2==0:
    t=(len(inp)//2)
    temp1=inp[:t-1]
    temp2=inp[t+1:len(inp)]
    print(temp1+'**'+temp2)
else:
    t=int(len(inp)/2)
    temp1=inp[:t]
    temp2=inp[t+1:len(inp)]
    print(temp1+'*'+temp2)
