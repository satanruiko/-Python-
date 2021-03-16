import requests
import json

class checkin(object):
    def __init__(self,email,passwd):
        self.sess=requests.Session()
        self.login_url='https://sockboom.lol/auth/login'
        self.checkin_url='https://sockboom.lol/user/checkin'
        self.email=email
        self.passwd=passwd

    def check(self):
        data={'email':self.email,'passwd':self.passwd}
        req=self.sess.post(self.login_url,data=data)
        req=self.sess.post(self.checkin_url)
        print(req.json()['msg'])

eg=checkin('','')
eg.check()
