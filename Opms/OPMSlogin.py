import requests
host = "http://123.56.170.43:8888"
login_url=host+"/login"
head={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
datas={"username":"libai",
         "password":"opms123456"}
res = requests.post(url=login_url,headers=head,data=datas)
print(res.text)
