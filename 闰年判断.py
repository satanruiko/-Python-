n=int(input('请输入年份'))
if n%400==0:
    print('Yes')
elif n%4==0 and n%100==0:
    print('No')
else:
    if n%4==0:
        print('Yes')
    else:
        print('No')

