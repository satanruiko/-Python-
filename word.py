def filter_(word):
    length=len(word)
    dicti={'-':0,'a':1,'b':2,'c':3,'d':4,'e':5,'é':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    sum=0;n=0
    while n<length:
        sum+=dicti[word[n]]
        n+=1
    if sum==100:
        return 1
    else:
        return 0
with open(r"D:\I.csv") as source:
    with open(r"D:\O.txt","a") as output:
        theline=1
        while theline:
            theline=source.readline()
            a=theline.split(",",1)
            a_1=str.lower(a[0])
            if filter_(a_1):
                aim='%s\n'%(a_1)
                output.write(aim)
