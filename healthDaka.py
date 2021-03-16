# -*- coding: utf-8 -*-
import datetime
import time

import json
import re
import requests
import urllib3

null=None
class DaKa(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_url = "http://ca.its.csu.edu.cn/Home/Login/215"
        self.validate_url = "https://wxxy.csu.edu.cn/a_csu/api/sso/validate"
        self.base_url = "https://wxxy.csu.edu.cn/ncov/wap/default/index"
        self.save_url = "https://wxxy.csu.edu.cn/ncov/wap/default/save"
        self.info = None
        self.sess = requests.Session()

    def login(self):
        """Login to CSU platform and verify"""
        data1 = {
            "userName": self.username,
            "passWord": self.password,
            "enter": 'true'
        }
        res2 = None
        try:
            res2 = self.sess.post(url=self.login_url, data=data1)
        except:
            print("无法连接信网中心")
            exit(1)
        if res2 is None:
            print("请检查账号密码是否正确")
            exit(1)

        regex = r'tokenId.*value="(?P<tokenId>\w+)".*account.*value="(?P<account>\w+)".*Thirdsys.*value="(' \
                r'?P<Thirdsys>\w+)" '
        data2 = None
        try:
            re_result = re.search(regex, res2.text)
            data2 = {
                "tokenId": re_result["tokenId"],
                "account": re_result["account"],
                "Thirdsys": re_result["Thirdsys"]
            }
        except:
            print("请检查账号密码是否正确")
            exit(1)
        try:
            self.sess.post(self.validate_url, data=data2)
        except:
            print("无法通过信网中心认证")
            exit(1)
        return self.sess

    def get_info(self, html=None):
        """Get hitcard info, which is the old info with updated new time."""
        if not html:
            urllib3.disable_warnings()
            res = self.sess.get(self.base_url, verify=False)
            html = res.content.decode()

        jsontext = re.findall(r'def = {[\s\S]*?};', html)[0]
        jsontext = eval(jsontext[jsontext.find("{"):jsontext.rfind(";")].replace(" ", ""))

        geo_text = jsontext['geo_api_info']
        geo_text = geo_text.replace("false", "False").replace("true", "True")
        geo_obj = eval(geo_text)['addressComponent']
        area = geo_obj['province'] + " " + geo_obj['city'] + " " + geo_obj['district']
        name = re.findall(r'realname: "([^\"]+)",', html)[0]
        number = re.findall(r"number: '([^\']+)',", html)[0]

        new_info = jsontext.copy()
        new_info['name'] = name
        new_info['number'] = number
        new_info['area'] = area
        new_info["date"] = self.get_date()
        new_info["created"] = round(time.time())
        new_info['city'] = geo_obj['city']
        new_info['address'] = eval(geo_text)['formattedAddress']
        self.info = new_info
        return new_info

    def get_date(self):
        today = datetime.date.today()
        return "%4d%02d%02d" % (today.year, today.month, today.day)

    def post(self):
        """Post the hitcard info"""
        res = self.sess.post(self.save_url, data=self.info)
        return json.loads(res.text)


def main(username, password):
    print("\n[Time] %s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    dk = DaKa(username, password)
    dk.login()
    dk.get_info()
    res = dk.post()
    if str(res['e']) == '0':
        print('已为您打卡成功！')
    else:
        print(res['m'])

main(username='',password='')