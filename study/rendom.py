# 随机数模块
import random

# 给定范围内的随机数
# num = random.randint(1,999999)
# print(num)


# 对整数有位数要求的,3位以内
# num1 = int(random.random()*1000)
# print(num1)


# 打印给定范围内，按步长累计数值
# num2 = random.randrange(1,99,2)
# print(num2)


#在给定值里任意返回一个值
# num3 = random.choice(["客户","用户","产品经理","市场"])
# print(num3)


# 打乱循序排序
lis = [1,2,3,4,5,6,7,8,9]
random.shuffle(lis)
print(lis)
