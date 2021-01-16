import requests
import re
import json
import random
from datetime import datetime,timedelta

null=None
tomorrow=(datetime.now()+timedelta(days=1)).strftime('%Y-%m-%d')
class auto_preserve(object):
    def __init__(self,userId,password):
        self.login_url_1='http://libuser.csu.edu.cn/center/ifcuas/login'
        self.login_url_2='http://lib.csu.edu.cn/login.jspx?returnUrl=/'
        self.zw_url1='http://libzw.csu.edu.cn/cas/index.php?callback=http://libzw.csu.edu.cn/index.php/Home/Web'
        self.zw_url2='http://libzw.csu.edu.cn/Api/auto_user_check'
        self.query_url='http://libzw.csu.edu.cn/api.php/spaces_old'
        self.all_cookies={'uservisit':'1','language':'zh','CSU_P2P_TOKEN':'BENLipipGBxLjcAE5FhOWlwwieie'}
        self.sess=requests.Session()
        self.available_list=[]
        self.seat_seed=None
        self.access_token=None
        self.segment=None
        self.userId=userId
        self.password=password


    def get_segment(self):
        self.segment=str(1519880+(datetime.now()-datetime(2021,1,12)).days)


    def login(self):
        data1={
            'userId': self.userId,'password':self.password,'appId':'zncms32',
            'retUrl': 'http://lib.csu.edu.cn/ssosync.jspx'
        }
        res=self.sess.post(self.login_url_1,data=data1)
        data2={'username':self.userId,'password':self.userId+'@infcn'}
        res=self.sess.post(self.login_url_2,data=data2)

    def seat_sys(self):
        res=self.sess.get(self.zw_url1,cookies=self.all_cookies)
        regex1=r'=[a-z0-9]+"'
        regex2=r'[a-z0-9]+'
        p=re.search(regex1,res.text)
        p=re.search(regex2,p[0])[0]
        res=self.sess.get(self.zw_url2,params={'user':self.userId,'p':p})
        self.access_token=res.cookies['access_token']
    

    def query_seat(self):
        params={'area':'59','segment':self.segment,'day':tomorrow,'startTime':'07:30','endTime':'22:00'}
        referer=f'http://libzw.csu.edu.cn/web/seat3?area=59&segment={self.segment}&day={tomorrow}&startTime=7:30&endTime=22:00'
        headers={'Origin': 'http://libzw.csu.edu.cn','Referer': referer,'Host': 'libzw.csu.edu.cn'}
        res=self.sess.get(self.query_url,params=params,cookies=self.all_cookies,headers=headers)
        seat_list=res.json()['data']['list']
        for i in seat_list:
            if i['status_name']=='空闲':
                self.available_list.append(i['id'])
        seat_list=None
        self.seat_seed=len(self.available_list)
        print('剩余座位数：',self.seat_seed)
    

    def preserve(self):
        base_url='http://libzw.csu.edu.cn/api.php/spaces/0000/book'
        times=3
        data={'access_token': self.access_token,'userid': self.userId,'segment': self.segment,'type': '1'}
        referer=f'http://libzw.csu.edu.cn/web/seat3?area=59&segment={self.segment}&day={tomorrow}&startTime=7:30&endTime=22:00'
        headers={'Origin': 'http://libzw.csu.edu.cn','Referer': referer,'Host': 'libzw.csu.edu.cn'}
        while times>0:
            seed=str(self.available_list[random.randint(0,self.seat_seed-1)])
            url=base_url.replace('0000',seed)
            res=self.sess.post(url=url,cookies=self.all_cookies,data=data,headers=headers)
            times-=1
            print(res.json()['msg'])
            if '预约成功'in res.json()['msg']:
                print('预约成功，座位号为A%s' %(seed))
                break
            else:
                print('预约失败,剩余尝试次数%s' %(times))


    def logout(self):
        url='http://libzw.csu.edu.cn/api.php/logout'
        data={'access_token':self.access_token,'userId':self.userId}
        headers={'Origin': 'http://libzw.csu.edu.cn','Referer': 'http://libzw.csu.edu.cn/home/web/f_second'}
        res=self.sess.post(url,data=data,cookies=self.all_cookies,headers=headers)
        print(res.json()['msg'])

def main(userId,password):
    zw=auto_preserve(userId,password)
    zw.get_segment()
    zw.query_seat()
    if zw.seat_seed!=0:
        zw.seat_sys()
        zw.preserve()
        zw.logout()
    else:
        print('没有座位，放弃预约')
    

main(userId='',password='')

        