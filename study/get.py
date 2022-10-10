import requests
# 保存会话


# def login_get():
#     url = "http://123.56.170.43:8888/login"
#     res = requests.get(url)
#     print(res.text)
#
# def login_post():
#     login_url = host + "/login"
#     head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
#     datas = {"username": "libai",
#                              "password": "opms123456"}
#     res = s.post(url=login_url, headers=head, data=datas)
#     print(res.text)
#
# # 第一种查询方式
# def proser1():
#     url = host +  "/project/manage"
#     datas = "status=1&keywords=测试"
#     para_url = url +"?"+ datas
#     res = s.get(para_url)
#     print(res.text)

# 第二种查询方式
# def proser2():
#     url = host +  "/project/manage"
#     datas = {"tataus":"1",
#              "keywords":"测试"}
#     res = s.get(url=url,params=datas)
#     print(res.text)

class Opms:
    def __init__(self,s = requests.session(),host = "http://123.56.170.43:8888"):
        self.s = s
        self.host = host
        self.login_post()
    def login_post(self):
            login_url = self.host + "/login"
            head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
            datas = {"username": "libai",
                                     "password": "opms123456"}
            res = self.s.post(url=login_url, headers=head, data=datas)
            print(res.text)

    def proser2(self):
            url = self.host + "/project/manage"
            datas = {"tataus": "1",
                     "keywords": "测试"}
            res = self.s.get(url=url, params=datas)
            print(res.text)
if __name__ == '__main__':
    op = Opms
    op().proser2()