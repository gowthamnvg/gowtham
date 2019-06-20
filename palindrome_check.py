inp=input()
tup = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
if any(char in tup for char in inp):
    print('yes')
else:
    print('no')
