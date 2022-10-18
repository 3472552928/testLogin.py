from api.project.add import OpmsAdd
import pytest
import os

def test_addpro_1(login_fixture,clear_data_fix):
    s = login_fixture
    OpmsAdd(s).add()


# 通过fixture进行参数化 ，一个变量多个值
# para = ['测试','别名','2022-03-01','2022-05-01','测试1']
# @pytest.fixture(params=para)
# def geetdata(request):
#     return request.param
# def test_addpro_(login_fixture,geetdata):
#     s = login_fixture
#     OpmsAdd(s).add(name=geetdata[0])



# 通过fixture进行参数化 ，多个变量多个值
para = [['测试1','别名','2022-10-01','2022-05-01','测试1'],
        ['测试2','别名2','2022-03-01','2022-05-01','测试1'],
        ['测试3','别名3','2022-03-01','2022-05-01','测试3']]


@pytest.fixture(params=para)
def getdata(request):
    return request.param
def test_addpro1(login_fixture,getdata,clear_data_fix):
    s = login_fixture
    OpmsAdd(s).add(name=getdata[0],aliasname=getdata)

