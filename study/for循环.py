# for循环
lis = (0,1,2,3,4,5,6,7,8,9,0)
for i in lis:
    print(i)

# # 打印键值对
# dic = {"name:":"zhangsan","age":20}
# for key,value in dic.items():
#     print(key,":",value)
# # 打印key
# for k in dic.keys():
#     print(k)
# for k in dic:
#     print(k)
#
# # # 打印值
# for v in dic.values():
#     print(v)


# # while循环
# while 1:
#     print("进入死循环了")


# 解除死循环
# n = 0
# while True:
#     print("进入死循环")
    # n = n+1
    # print(n)
    # if n>5:
    #     break

# 跳出死循环执行下一个循环
# n = 10
# while True:
#     n = n-2
#     print(n)
#     if 3<n<5:
#         continue
#         print("我要跳出循环了")
#
#     elif n < 3:
#         print("我要结束了！！！")
#         break
#         print("我是break后面的print")
#

# 求1+....+10的和
# num = 1
# sum = 0
# while num<=100:
#     sum += num
#     num +=1
#     print(num)
# print(sum)

# # 求0+2+4+6.。。+100的和
# num = 0
# sum = 0
# while num<=100:
#     sum += num
#     num += 2
#     print(num)
# print(sum)