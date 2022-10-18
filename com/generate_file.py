# -- coding: utf-8 --
# @time :
# @author : 段璐威
# @email : duanluwei925@163.com
# @file : .py
# @software: pycharm

# 快速生成备注字数
import os
import random

def gane_file(name,length):
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(path)
    filename = os.path.join(path,'conf',name)

    # 用for循环
    # with open(filename,'w',encoding="utf-8")as f:
    #     for i in range(1,200):
    #         f.write("什么东西")

    # 通过随机数进行中英文备注
    lis = ["我","是","中","国","人","a","b","c","1","5","7"]
    with open(filename,'a',encoding="utf-8")as f:
        for i in range(length):
            rand = random.randint(0, len(lis) - 1)
            f.write(lis[rand])


gane_file("备注.txt",300)