from Opms.add import OpmsAdd



class TestLogi():
    def __init__(self,op = OpmsAdd(host="http://123.56.170.43:8888"),):
        self.op = op

    # 用户为空
    def login1(self):
        res = self.op.login_post(username="")
        print(res)
        code = res["code"]
        if code ==0:
            print("测试通过")
        else:
            print("测试失败")


if __name__ == '__main__':
    ts = TestLogi()
    ts.login1()




