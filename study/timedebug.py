import time

# 时间错
dt = int(time.time()*10000)

# tume.sleep 强制等待时间 休眠时间，单位s
# time.sleep(3)

# 把时间戳转换成时间元组
dt1 = time.localtime(time.time())

# 时间元组转换成时间戳
dt = time.mktime(dt1)

# 打印日期、日期+时间的标准格式
dt = time.strftime("%Y/%m/%d %H:%M:%S")
dt1 = time.strftime("%Y/%m/%d %X")
print(dt)
