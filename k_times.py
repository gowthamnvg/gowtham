inp=input().split()
for i in inp:
    if(i.isdigit()):
        c=int(i)
for i in inp:
    if(i.isalpha()):
        s=i
for i in range(0,c):
    print(s)
