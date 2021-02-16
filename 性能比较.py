#以下是我自己编写的计算pi的方法，花费0.48秒
#展开式末项小于0.000001
def mine():
    k=1
    m=0.000001
    while (1/(2*k+1))>=m:
        k+=1
    print('%.6f' %(4*sum(list((-1)**i*(1/(2*i+1)) for i in range(0,k)))))
#以下是答案的方法，花费0.349秒
def anwser():
    threshold = 0.000001
    pi4 = k = 0
    f = 1
    while abs(1 / (2 * k + 1)) >= threshold:
        pi4 = pi4 + f * 1 / (2 * k + 1)
        k = k + 1
        f = -f
    print("{:.6f}".format(pi4*4))
mine()
anwser()
#以后用C++来进行比较