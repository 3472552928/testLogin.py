import requests
from login1 import Login



class Pro():
    def __init__(self, s=requests.session(), host="http://123.56.170.43:8888"):
        self.s = s
        self.host = host
        # 直接self
        Login(self.s).login()
        #cookie
        # self.cookie = Login().login()

    def addPro(self):
        url = self.host + "/project/add"
        datas = {"name": " 测试", "aliasname": "测试", "started": "2022-01-01", "ended": "2022-01-02", "desc": "33",
                 "id": 0}
        res = self.s.post(url=url,data=datas)
        print(res.text)
        # return res.json()["id"]

if __name__ == '__main__':
    ap = Pro()
    ap.addPro()

