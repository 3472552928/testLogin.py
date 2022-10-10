import requests

class Login():
    def erpLogin(self):
        host = "http://123.56.170.43:3000/jshERP-boot"
        login_url = host + "/user/login"
        head = {"Content-Type": "application/json;charset=UTF-8"}
        datas = {"loginName": "root",
                 "password": "14d0dd4eb2f6dd3740a5c084688c2a94"}

        res = requests.post(url=login_url, headers=head, json=datas)
        print(res.text)
    def opmsLogin(self):
        host = "http://123.56.170.43:8888"
        login_url = host + "/login"
        head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        datas = {"username": "libai",
                 "password": "opms123456"}
        res = requests.post(url=login_url, headers=head, data=datas)
        print(res.text)

Login().opmsLogin()

class Opmslogin():
    def __init__(self,host="http://123.56.170.43:8888"):
        self.host=host
    def login(self,head,datas):
        url = self.host+"/login"
        # head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        # datas = {"username": "libai",
        #          "password": "opms123456"}
        res = requests.post(url=url,headers=head,data=datas)
        print(res.text)

    def loginout(self):
        url = self.host+"/logout"
        res = requests.get(url=url)
        print(res.text)

# /执行login
if __name__ == '__main__':
    head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    datas = {"username": "libai",
             "password": "opms123456"}
    Opmslogin().login(head=head, datas=datas)


def erpLogin():
    host = "http://123.56.170.43:3000/jshERP-boot"
    login_url = host + "/user/login"
    head = {"Content-Type": "application/json;charset=UTF-8"}
    datas = {"loginName": "root",
             "password": "14d0dd4eb2f6dd3740a5c084688c2a94"}

    res = requests.post(url=login_url, headers=head, json=datas)
    print(res.text)

def opmsLogin():
    host = "http://123.56.170.43:8888"
    login_url = host + "/login"
    head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    datas = {"username": "libai",
             "password": "opms123456"}
    res = requests.post(url=login_url, headers=head, data=datas)
    print(res.text)
