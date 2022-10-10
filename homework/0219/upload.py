import requests
from login1 import Login





class Uolocad():
    def __init__(self, s=requests.session(), host="http://121.5.121.62:8088"):
        self.s = s
        self.host = host
        Login(self.s).login()


    def up(self):
        url = self.host + "/uploadmulti"
        file = {"uploadFiles":open("01979d5d9d5aa5a8012060be51c111.jpg@1280w_1l_2o_100sh.jpg","rb")}
        res = self.s.post(url,files=file)
        print(res.text)



    def getAlbum(self):
        url = self.host + "/album/manage?filter=me"
        self.s.head(url)


if __name__ == '__main__':
    up = Uolocad()
    # up.up()
    up.getAlbum()