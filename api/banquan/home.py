import requests

def login():
    host = "https://banquanqiao.com"
    url = host + "/saas/openapi/copyright/message/unread"
    data = {"mobile":"19939425498"}
    res = requests.get(url=url,params=data)
    print(res.text)
login()