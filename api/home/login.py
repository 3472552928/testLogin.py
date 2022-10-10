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
#
# Login().opmsLogin()
from com import redTxtconfig


class Opmslogin():
    def __init__(self,s = requests.session(),host="http://121.5.121.62:8088"):
        self.host=host
        self.s = s
    def login(self,username="libai",password= "csyz@1234"):
        url = self.host+"/login"
        head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        datas = {"username": username,
                 "password": password}
        res = self.s.post(url=url,headers=head,data=datas)
        print(res.text)
        return res

    # def loginout(self):
    #     url = self.host+"/logout"
    #     res = requests.get(url=url)
    #     print(res)
    #     return res

# /执行login
# if __name__ == '__main__':
#     op = Opmslogin
#     Opmslogin().login()
#     head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
#     # datas = {"username": "libai",
#     #          "password": "opms123456"}
#     name = redTxtconfig.getTxt("\conf\data.txt")[0]
#     lg = Opmslogin().login(username=name)


# def erpLogin():
#     host = "http://123.56.170.43:3000/jshERP-boot"
#     login_url = host + "/user/login"
#     head = {"Content-Type": "application/json;charset=UTF-8"}
#     datas = {"loginName": "root",
#              "password": "14d0dd4eb2f6dd3740a5c084688c2a94"}
#
#     res = requests.post(url=login_url, headers=head, json=datas)
#     print(res.text)
#
# def opmsLogin():
#     host = "http://123.56.170.43:8888"
#     login_url = host + "/login"
#     head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
#     datas = {"username": "libai",
#              "password": "opms123456"}
#     res = requests.post(url=login_url, headers=head, data=datas)

#
if __name__ == '__main__':
    cl =Opmslogin()
    cl.login()