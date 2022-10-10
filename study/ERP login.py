import requests
# # add_url = "/user/addUser"
# # url1 = host+login_url
# # url2 = host+add_url
host = "http://123.56.170.43:3000/jshERP-boot"
login_url = host+"/user/login"
head = {"Content-Type":"application/json;charset=UTF-8"}
datas = {"loginName":"root",
         "password":"14d0dd4eb2f6dd3740a5c084688c2a94"}

res = requests.post(url=login_url,headers=head,json=datas)
print(res.text)


