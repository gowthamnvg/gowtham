inp1 = int(input())
if inp1 > 1:
   for i in range(2,inp1):
       if (inp1 % i) == 0:
           print("no")
           break
   else:
       print("yes")
else:
   print("no")
