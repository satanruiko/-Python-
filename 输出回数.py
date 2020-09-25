def veri(dd):
    x=str(dd)
    n=0;a=(len(x))//2
    while n<a:
        if x[n]==x[-n-1]:
            n+=1
            continue
        else:
            return False
    return True




