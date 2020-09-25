print('计算BMI')
a=int(input('输入身高cm'))
b=int(input('输入体重kg'))
c=(b/(a/100)**2)
print('%.3f'%c)
if c>=32:
    print('严重肥胖')
elif c>=28:
    print('肥胖')
elif c>=25:
    print('偏胖')
elif c>=18.5:
    print('正常')
else:
    print('偏瘦')


    