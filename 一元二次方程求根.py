import math
def quadratic(a,b,c):
    B=b**2-4*a*c
    if a==0:
        return 'a不能为零'
    else:
        if B>=0:
            x1=(-b+math.sqrt(B))/2*a
            x2=(-b-math.sqrt(B))/2*a
            return x1,x2
        else:
            return '方程无解'
