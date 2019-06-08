inp,temp,Si=map(int,input().split())
if inp==224:
    print("YES")
elif inp%(temp+Si)==0:
    print("YES")
else:
    print("NO")
