import requests
import re
from datetime import datetime

def encodeInp(string):
    keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    i=0
    length=len(string)
    output=''
    chr1,chr2,chr3,enc1,enc2,enc3,enc4=None,None,None,None,None,None,None
    while i<length:
        try:
            chr1=ord(string[i])
        except:
            chr1=0
        i+=1
        try:
            chr2=ord(string[i])
        except:
            chr2=0
        i+=1
        try:
            chr3=ord(string[i])
        except:
             chr3=0
        i+=1
        enc1 = chr1 >> 2
        enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
        enc3 = ((chr2 & 15) << 2) | (chr3 >> 6)
        enc4 = chr3 & 63
        if chr2==0:
            enc3,enc4=64,64
        else:
            if chr3==0:
                enc4=64
        output+=keyStr[enc1]+keyStr[enc2]+keyStr[enc3]+keyStr[enc4]
    return output

class getGrade(object):
    def __init__(self,account,password):
        self.account=encodeInp(account)
        self.password=encodeInp(password)
        self.sess=requests.Session()
        self.get_url='http://csujwc.its.csu.edu.cn/jsxsd/kscj/cjcx_list?Ves632DSdyV=NEW_XSD_WDCJ'
        self.login_url='http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk'
        self.logout_url='http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk?method=exit&tktime=substitute000'
        self.get_rank_url='http://csujwc.its.csu.edu.cn/jsxsd/kscj/zybm_cx'

    def login(self):
        data={'encoded':self.account+r'%%%'+self.password}
        headers={'Referer':'http://csujwc.its.csu.edu.cn/jsxsd/kscj/yscjcx_list'}
        res=self.sess.post(self.login_url,data=data,headers=headers)

    def get(self):
        headers={'Referer':'http://csujwc.its.csu.edu.cn/jsxsd/framework/xsMain.jsp'}
        res=self.sess.get(self.get_url)
        target=res.text
        regex1=r'<td align="left">\S*</td>'
        subject=re.findall(regex1,target)
        regex2=r"zcj=\S{1,3}"
        point=re.findall(regex2,target)
        regex3=r'\]\S*<'
        regex4=r"=[\S]{1,3}'"
        for i in range(len(subject)):
            subject[i]=re.search(regex3,subject[i])[0]
        for i in range(len(point)):
            point[i]=re.search(regex4,point[i])[0]
        for i in range(len(subject)):
            print("'"+subject[i][1:-1]+point[i])
    def get_rank(self):
        headers={'Referer':'http://csujwc.its.csu.edu.cn/jsxsd/kscj/yscjcx_list'}
        res=self.sess.get(self.get_rank_url)
        info=re.findall(r'<td>\S{1,5}</td>',res.text)
        for i in info:
            print(i)

    def logout(self):
        tktime=str(int(datetime.now().timestamp()))
        url=self.logout_url.replace('substitute',tktime)
        res=self.sess.get(url)
        res=self.sess.get('https://ca.csu.edu.cn/authserver/logout')

def main(account,password):
    hzx=getGrade(account,password)
    hzx.login()
    try:
        hzx.get()
        hzx.get_rank()
    except:
        print('error')
        hzx.logout()

with open(r'D:\source.csv') as source:
    flag=1
    while flag:
        flag=source.readline()
        account,password=flag.split(',')
        password=password.strip()
        print(account)
        main(account,password)