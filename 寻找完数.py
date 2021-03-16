def check(a):
    sum=1
    factor=[1]
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            sum+=(i+a/i)
            factor.extend([i,int(a/i)])
        else:
            continue
    if a==sum:
        return map(str,sorted(factor))
    else:
        return 0
i=1;ls=0
n=int(input())
while True:
    ff=check(i)
    if ff:
        print('{}={}'.format(i,'+'.join(ff)))
        ls+=1
    i+=1
    if ls==n:
        break