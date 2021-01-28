def quadratic(a,b,c):
    temp=b**2-4*a*c
    if a==0 and b==0:print('Data error!')
    elif a==0 and b!=0:
        print('%.2f'%((-c)/b))
    else:
        if temp==0:
            print('%.2f'%((-b)/(2*a)))
        elif temp<0:
            print('该方程无实数解')
        else:
            print('%.2f %.2f' %(((-b)+pow(temp,0.5))/(2*a),((-b)-pow(temp,0.5))/(2*a)))
#测试用例
quadratic(1,1,2)