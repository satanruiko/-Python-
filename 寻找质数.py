def odd_num():
    n=1
    while True:
        n+=2
        yield n
def judge(factor):
    return lambda x:x%factor >0
def PrimeNum():
    yield 2
    OriginalList=odd_num()
    while True:
        n=next(OriginalList)
        yield n
        OriginalList=filter(judge(n),OriginalList)
for i in PrimeNum():
    if i<2000:
        print(i)
    else:
        break
        
