#计算斐波那契数列第n项
n=int(input('Please enter a number'))
a=1
b=1
if n==1 or n==2:
    print(1)
else:
    while n>=3:
        c=(a+b)
        a=b
        b=c
        n=n-1
        c=c+2
    print(c)

