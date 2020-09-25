import random
a=random.randint(1,10)
time=3
while time>0:
    n=int(input('请猜一个数'))
    if n>10 or n<1:
        print('输入1到10的整数')
        time=time+1
    else:
        if n==a:
            print('正确')
            break
        elif n<a:
            print('小了')
        else:
            print('大了')
    time=time-1
    print('你还有%s次机会'%(time))
if time==0:
    print('机会耗尽,下次吧') 
else:
    print('你真棒')