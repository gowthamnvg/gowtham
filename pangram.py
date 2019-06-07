import string
def pangram(st):
    s=set(string.ascii_lowercase)
    return s<=set(st.lower())

inp1=input()
if pangram(inp1):
    print('yes')
else:
    print('no')
    
