import requests
import json

sess=requests.Session()
login_url='https://sockboom.art/auth/login'
checkin_url='https://sockboom.art/user/checkin'
data={'email':'lp932515@gmail.com','passwd':'12345678.'}
req=sess.post(login_url,data=data)
req=sess.post(checkin_url)
print(req.json()['msg'])
