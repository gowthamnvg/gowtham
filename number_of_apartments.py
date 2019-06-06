inp1,inp2=input().split()
if(inp1.isdigit() and inp2.isdigit()):
              inp1,inp2=int(inp1),int(inp2)
              if(inp2==1):
                  print("1 2")
              else:
                 print("1 "+str(inp1-inp2))
