import math
import functools
inp1,inp2=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(inp2):
    c,d=map(int,input().split())
    temp=functools.reduce(math.gcd,List[c-1:d])
    print(temp)
