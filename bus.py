inp, b, f, k = map(int, input().split())
counter = 0
b2 = b-f
if (b2 >= 0):
    di = (inp-f)*2
    for i in range (k):
        if (i == k-1):
             di =di/ 2
        if (b2 < di):
            b2 = b
            counter += 1
        b2 = b2 - di
        if (b2 < 0):
            counter = -1
            break
        di = 2*inp - di

    print (counter)
else:
    print (-1)
