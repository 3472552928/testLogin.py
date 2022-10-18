import pytest
from api.project.add import OpmsAdd
from com.csvRead import ReadCsv
para = ReadCsv().readALL(start=1,end=30)



# @pytest.mark.parametrize("name,aliasname,started,ended,desc",para)
def testAddNeed_1(name,aliasname,started,ended,desc):
    res = OpmsAdd().add(name,aliasname,started,ended,desc)
    print(res)


