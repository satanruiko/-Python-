a=int(input('请输入年份'))
if (a%4==0 and a%100!=0) or (a%400==0):
    print(f'{a}是闰年')
else:
    print(f'{a}不是闰年')

