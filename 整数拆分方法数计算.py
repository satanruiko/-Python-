def odd():
    n=1
    while True:
        n=n+2
        yield n
def number():
    yield 1
    n=1
    while True:
        n=n+1
        yield n
odds=odd();numbers=number()
def gener():
    while True:
        yield next(numbers)
        yield next(odds)
geners=gener()
def location():
    n=1
    yield n
    while True:
        n=n+next(geners)
        yield n
locations=location()
def symbol(x):
    if x%4==0:return 1
    if x%4==1:return 1
    if x%4==2:return -1
    if x%4==3:return -1
A=[1];B=[next(locations)];C=len(A)
while C<666:
    a=0
    for i in range(1,len(A)+1):
        if i in B:
            b=B.index(i)
            a+=(A[-i]*symbol(b))
    A.append(a)
    C=len(A)
    if B[-1]<=C:
        B.append(next(locations))
print(C)
print(A[-1])
