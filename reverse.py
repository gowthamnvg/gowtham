inp=int(input())
rem=0
while inp!=0 :
        temp=inp%10
        rem=(rem*10)+temp
        inp=inp//10
print(rem)
