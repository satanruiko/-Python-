import requests
import re
import json
import random
from datetime import datetime,timedelta

login_url_1='http://libuser.csu.edu.cn/center/ifcuas/login'
login_url_2='http://lib.csu.edu.cn/login.jspx?returnUrl=/'
zw_url1='http://libzw.csu.edu.cn/cas/index.php?callback=http://libzw.csu.edu.cn/index.php/Home/Web'
zw_url2='http://libzw.csu.edu.cn/Api/auto_user_check'
query_url='http://libzw.csu.edu.cn/api.php/spaces_old'
userId='8203200815';password='r6BFb563RmjCFJs'
sess=requests.Session()
access_token=None
null=None
all_cookies={'uservisit':'1','language':'zh','CSU_P2P_TOKEN':'BENLipipGBxLjcAE5FhOWlwwieie'}
tomorrow=(datetime.now()+timedelta(days=1)).strftime('%Y-%m-%d')
seat_seed=None
available_list=[]
segment=None

def get_segment():
    global segment
    segment=str(1519880+(datetime.now()-datetime(2021,1,12)).days)


def login(userId,password):
    data1={
        'userId': userId,'password':password,'appId':'zncms32',
        'retUrl': 'http://lib.csu.edu.cn/ssosync.jspx'
    }
    reque=sess.post(login_url_1,data=data1)
    data2={'username':userId,'password':userId+'@infcn'}
    reque=sess.post(login_url_2,data=data2)

def seat_sys():
    reque=sess.get(zw_url1,cookies=all_cookies)
    regex1=r'=[a-z0-9]+"'
    regex2=r'[a-z0-9]+'
    p=re.search(regex1,reque.text)
    p=re.search(regex2,p[0])[0]
    reque=sess.get(zw_url2,params={'user':userId,'p':p})
    global access_token
    access_token=reque.cookies['access_token']
    

def query_seat():
    params={'area':'59','segment':segment,'day':tomorrow,'startTime':'07:30','endTime':'22:00'}
    referer=f'http://libzw.csu.edu.cn/web/seat3?area=59&segment={segment}&day={tomorrow}&startTime=7:30&endTime=22:00'
    headers={'Origin': 'http://libzw.csu.edu.cn','Referer': referer,'Host': 'libzw.csu.edu.cn'}
    reque=sess.get(query_url,params=params,cookies=all_cookies,headers=headers)
    seat_list=reque.json()['data']['list']
    for i in seat_list:
        if i['status_name']=='空闲':
            available_list.append(i['id'])
    seat_list=None
    global seat_seed
    seat_seed=len(available_list)
    print('剩余座位数：',seat_seed)
    

def preserve():
    base_url='http://libzw.csu.edu.cn/api.php/spaces/0000/book'
    times=3
    data={'access_token': access_token,'userid': userId,'segment': segment,'type': '1'}
    referer=f'http://libzw.csu.edu.cn/web/seat3?area=59&segment={segment}&day={tomorrow}&startTime=7:30&endTime=22:00'
    headers={'Origin': 'http://libzw.csu.edu.cn','Referer': referer,'Host': 'libzw.csu.edu.cn'}
    while times>0:
        seed=str(available_list[random.randint(0,seat_seed-1)])
        url=base_url.replace('0000',seed)
        reque=sess.post(url=url,cookies=all_cookies,data=data,headers=headers)
        times-=1
        print(reque.json()['msg'])
        if reque.json()['msg']=='预约成功':
            print('预约成功，座位号为A%s' %(seed))
            break
        else:
            print('预约失败,剩余尝试次数%s' %(times))


def logout():
    url='http://libzw.csu.edu.cn/api.php/logout'
    data={'access_token':access_token,'userId':userId}
    headers={'Origin': 'http://libzw.csu.edu.cn','Referer': 'http://libzw.csu.edu.cn/home/web/f_second'}
    reque=sess.post(url,data=data,cookies=all_cookies,headers=headers)
    print(reque.json()['msg'])

def main(userId,password):
    get_segment()
    login(userId,password)
    seat_sys()
    query_seat()
    if seat_seed!=0:
        preserve()
    else:
        print('没有座位，放弃预约')
    logout()

main(userId=userId,password=password)

        