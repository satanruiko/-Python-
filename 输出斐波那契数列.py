def feibonaqi():
    a=1;b=1
    yield a
    yield b
    while True:
        a,b=b,a+b
        yield b
for i in feibonaqi():
    if i<2000:
        print(i)
    else:
        break
