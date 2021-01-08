import requests
import re
import json
import random
import os
from datetime import datetime,timedelta
from apscheduler.schedulers.blocking import BlockingScheduler

login_url_1='http://libuser.csu.edu.cn/center/ifcuas/login'
login_url_2='http://lib.csu.edu.cn/login.jspx?returnUrl=/'
zw_url1='http://libzw.csu.edu.cn/sso/home.php'
zw_url2='http://libzw.csu.edu.cn/Api/auto_user_check'
zw_url3='http://libzw.csu.edu.cn/'
userId='8203200815';password='r6BFb563RmjCFJs'
sess=requests.Session()
access_token=None
all_cooki=None
hour='6';minute='3'

def login(userId,password):
    data1={
        'userId': userId,'password':password,'appId':'zncms32',
        'retUrl': 'http://lib.csu.edu.cn/ssosync.jspx'
    }
    reque=sess.post(login_url_1,data=data1)
    data2={'username':userId,'password':userId+'@infcn'}
    reque=sess.post(login_url_2,data=data2)
#    print(reque.cookies)

def enter_zwsys():
    cookies1={'uservisit':'1','language':'zh'}
    reque=sess.get(zw_url1,cookies=cookies1)
#    print(reque.text)
    regex1=r'=[a-z0-9]+"'
    regex2=r'[a-z0-9]+'
    p=re.search(regex1,reque.text)
    p=re.search(regex2,p[0])[0]
    reque=sess.get(zw_url2,params={'user':userId,'p':p})
    got_cooki=reque.cookies
#    print(got_cooki)
    all_cooki={**cookies1,**got_cooki}
    reque=sess.get(zw_url3,cookies=all_cooki)
    access_token=got_cooki['access_token']
    
def logout():
    url='http://libzw.csu.edu.cn/api.php/logout'
    data={'access_token':access_token,'userId':userId}
    headers={'Origin': 'http://libzw.csu.edu.cn','Referer': 'http://libzw.csu.edu.cn/home/web/f_second'}
    reque=sess.post(url,data=data,cookies=all_cooki,headers=headers)
    print(reque.json()['msg'])

def preserve():
    base_url='http://libzw.csu.edu.cn/api.php/spaces/0000/book'
    times=3
    while times>0:
        seed=random.randint(1,180)
        number=str(seed+9165)
        url=base_url.replace('0000',number)
        data={'access_token': access_token,'userid': '8203200815','segment': '1519875','type': '1'}
        tomorrow=(datetime.now()+timedelta(days=1)).strftime('%Y-%m-%d')
        referer=f'http://libzw.csu.edu.cn/web/seat3?area=59&segment=1519875&day={tomorrow}&startTime=6:00&endTime=22:00'
        headers={'Origin': 'http://libzw.csu.edu.cn','Referer': referer}
        reque=sess.post(url=url,cookies=all_cooki,data=data,headers=headers)
        times-=1
        if reque.json()['msg']=='预约成功':
            print('预约成功，座位号为A%s' %(seed))
            break
        else:
            print('预约失败,剩余尝试次数%s' %(times))
def main(userId,password):
    login(userId,password)
    enter_zwsys()
    preserve()
    logout()

mission=BlockingScheduler()
mission.add_job(main,'cron',args=[userId,password],hour=hour,minute=minute)
print('⏰ 已启动定时程序，每天 %02d:%02d 为您预约' % (int(hour), int(minute)))
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
    mission.start()
except(KeyboardInterrupt, SystemExit):
    print('疑问')


        