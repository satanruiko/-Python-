def findMinAndMax(*L):
    if len(L)==0:
        return (None,None)
    a=L[0]
    for i in L:
        if a>=i:
            continue
        else:
            a=i
    b=L[0]
    for i in L:
        if b<=i:
            continue
        else:
            b=i
    return (a,b)

