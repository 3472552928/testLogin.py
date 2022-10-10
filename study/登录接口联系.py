# 登录接口
# def login(username,password):
#     if username == "libai" and password == "duanluwei139":
#         print('{"code":0,"message":"登录成功"}')
#     elif username == "" or password == "0":
#         print('{"code:"1,"massage":"不允许为空"}')
#     elif username != "libai" or password =="duanluwei139":
#         print('{"code:"1,"massage":"请输入正确账号"}')
#     elif username == "libai" or password != "duanluwei139":
#         print('{"code:"1,"massage":"请输入密码"}')
# login(username="libai",password="duanluwei139")

# # 注册接口
# from random import random


# def getCode(phone):
#     code = int(random()*1000000)
#     # print(code)
#     # return '{"code":0,"massage":"您的验证码是%d"}'%code
#     return code
# print(getCode("19939425498"))

# def register(username,phone,pwd,code):
#     if username == "" or phone == "" or pwd == "" or code =="":
#         print("请输入必填项")
#     if username ==1234567890:
#         print("用户仅支持中英文、数字和下划线，且不能为纯数字")
#     elif len(username)>14 or len(username)<7:
#         print("设置后不可更改，中英文均可，最长14个英文或7个汉字")
#     elif len(phone) !=11:
#         print("手机格式不正确")
#     elif len(pwd) >=14 or len(pwd) <8:
#         print("密码必须是8到14位字符")
#     elif len(str(code)) !=6:
#         print("验证码格式不正确")
# register(username="1234637",phone="19939425498",pwd="12345671",code=getCode("19939425498"))