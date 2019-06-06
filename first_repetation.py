inp=int(input())
List=list(map(int,input().split()))
for i in List:
    if List.count(i)>1:
       print(i)
       break
else:
    print("unique")
