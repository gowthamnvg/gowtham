inp1,inp2 = map(int,input().split())
c = list(map(int,input().split()))
amount = int(input())
total = (sum(c)-c[inp2])//2
if amount == total:
  print("Bon Appetit")
else:
  print(amount-total)
