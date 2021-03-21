import jieba
dk = {}
with open('data.txt','r',encoding='utf-8') as f:
    text=f.read()
    ls=jieba.cut(text,cut_all=True)
    ls=list([i for i in ls if len(i)==2])
    for i in ls:
        if i in dk:
            dk[i]+=1
        else:
            dk[i]=1
dp = list(dk.items())
dp.sort(key= lambda x:x[1], reverse = True)

for i in range(10):
    print(':'.join([dp[i][0],str(dp[i][1])]))