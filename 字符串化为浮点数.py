from functools import reduce
dict1={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def floatstr(x):
    def fun (s):
        return dict1[s]
    def pro (x,y):
        return x*10+y
    n=x.index('.')
    x=x[:n]+x[n+1:]
    return (reduce(pro,map(fun,x)))/(10**n)
print(floatstr('123.456'))

    
        




