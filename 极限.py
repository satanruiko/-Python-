accuracy=float(input('Please enter'))
n=1;sum_a=0;sum_b=0;L=[0]
while True:
    sum_a+=n
    sum_b+=(1/sum_a)
    L.append(sum_b)
    n+=1
    if L[1]-L[0]<10**-accuracy:
        print(L[1])
        break
    else:
        L.pop(0)
        continue
    