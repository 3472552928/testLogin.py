import requests


class Login():
    def __init__(self, s=requests.session(), host="http://123.56.170.43:8888"):
        self.s = s
        self.host = host

    def login(self):
        url = self.host + "/login"
        head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        datas = {"username": "libai",
                 "password": "opms123456"}
        res = self.s.post(url=url, headers=head, data=datas)
        print(res.cookies)
        return res.cookies


if __name__ == '__main__':
    lg = Login()
    lg.login()
