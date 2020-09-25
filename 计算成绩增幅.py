print(r'Hi,Please input your grade')
a= int(input(r'Last time'))
b= int(input('This time'))
c=((b-a)/a)*100
if c >=0:
    print('Your grade improves','%.3f %%'%(c))
else:
    print('Your grade declines','%.3f %%'%(c))

