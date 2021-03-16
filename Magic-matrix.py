def fill(n):
    ls=[[0 for i in range(n)] for i in range(n)]
    x,y = 0,n//2 #original position
    for i in range(1,n*n+1):
        ls[x][y]=i
        #move
        xm,ym=x-1,y+1
        if xm<0:
            xm=n-1
        if ym>n-1:
            ym=0
        if ls[xm][ym]!=0:
            x+=1
        else:
            x,y=xm,ym
    return ls
print(fill(5))