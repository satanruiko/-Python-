import requests
import re
from datetime import datetime

encoded=r'ODIwMzIwMDgxNQ==%%%cjZCRmI1NjNSbWpDRkpz'
class getGrade(object):
    def __init__(self,encoded):
        self.encoded=encoded
        self.sess=requests.Session()
        self.get_url='http://csujwc.its.csu.edu.cn/jsxsd/kscj/cjcx_list?Ves632DSdyV=NEW_XSD_WDCJ'
        self.login_url='http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk'
        self.logout_url='http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk?method=exit&tktime=substitute000'
        self.get_rank_url='http://csujwc.its.csu.edu.cn/jsxsd/kscj/zybm_cx'

    def login(self):
        data={'encoded':self.encoded}
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

def main(encoded):
    hzx=getGrade(encoded)
    hzx.login()
    try:
        hzx.get()
        hzx.get_rank()
    except:
        print('error')
    hzx.logout()

main(encoded)

