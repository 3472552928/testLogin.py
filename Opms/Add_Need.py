from Opms.add import OpmsAdd
# zhengze
import re
# 需求name 为空是提示  失败
class TestNedd():
    def __init__(self,host="http://123.56.170.43:8888"):
        self.host = host
        self.op = OpmsAdd(host=self.host)
        self.pid = self.op.add()
        self.filename = "D:\\R-C.jpeg"
        # self.op.addneed(self.pid)

    def test_need_1(self):
        res = self.op.addneed(self.pid,self.filename,name = "")
        text = re.findall('"message":"(.*?)"',res.text)[0]
        code = re.findall('"code":(.*?),', res.text)[0]
        print(type(text))
        if text == "请填写名称" and code == "0":
            print("测试通过")
        else:
            print("测试失败")
if __name__ == '__main__':
    te = TestNedd()
    te.test_need_1()