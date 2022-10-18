import datetime


# 获取今天日期 格式2022-10-18
date1 = datetime.date.today()

# 打印当前的时间年月日时分秒 毫秒微秒
date1 = datetime.datetime.now()
print(date1)


# 打印今天的年月日
year = datetime.date.today().year
mon = datetime.date.today().month
day = datetime.date.today().day
print(year,mon,day)




