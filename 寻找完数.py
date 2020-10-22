def check(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum+=i
        else:
            continue
    if a==sum:
        return True
    else:
        return False
print(list(filter(check,range(6,10000))))
