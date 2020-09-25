a=1;n=1;c=[]
while len(c)<3:
    n=a*7
    a=a+1
    if n%2==1 and n%3==2 and n%5==4 and n%6==5:
        c.append(n)
print(c)        
    


    

