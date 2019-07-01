inp1,inp2=map(int,input().split())
n=list(map(int,input().split()))[:inp1]
n1=list(map(int,input().split()))[:inp2]
n2=list(map(int,input().split()))[:inp2]
n3=list(map(int,input().split()))[:inp2]
print(min(inp1+n1))
print(min(inp1+n2))
print(min(inp1+n3))

