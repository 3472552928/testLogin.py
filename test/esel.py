import pytest
import re
from api.home.login import Opmslogin
from com.redTxtconfig import getYaml
from com.redTxtconfig import getYaml

res = getYaml(file="\conf\db.yaml")
# print(res["login"])
# print(res["login"])
para = res["login"]
print(type(para[0]))
print(para[0])

new = []
for i in range(len(para)):
    # print(para[i])
    # print(list(para[i]))
    new.append(list(para[i]))
print(new)

