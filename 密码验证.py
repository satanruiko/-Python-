password='123';time=3
while time>0:
    n=input('输入密码')
    if '*' in n:
        print('error')
        continue
    if n==password:
        print('密码正确')
        break
    else:
        print('密码错误')
    time=time-1
    if time==0:
        print('10分钟后重试')
    else:
        print('您还有%s次机会，请重新输入'%(time))



