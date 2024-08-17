import allure
import requests
import pytest
import yaml

from test_case.api import response
from test_case.conftest import get_data

@allure.feature("修改课程")
class Test_modify:

    def setup_module(self):
        print("准备测试数据")
    def teardown_module(self):
        print("清理测试数据")

    ##########课程修改成功（必填参数课程id正确）##########
    #####课程修改成功（全部必填参数填写正确）#####
    @allure.severity(severity_level="blocker")
    @pytest.mark.parametrize("id,name,subject,price,applicablePerson,info", get_data()['modify1'])
    def test_modify_01(self,login_fixture,id,name,subject,price,applicablePerson,info):
        headers = {
            "Authorization": login_fixture
        }
        json={
            "id":id,
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson":applicablePerson,
            "info": info
        }
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.put_modify_query(headers=headers,json=json)
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "操作成功"
        assert result['code']== 200

    #####修改失败用例#####
    @allure.severity(severity_level="critical")
    @pytest.mark.parametrize("id,name,subject,price,applicablePerson,info", get_data()['modify2'])
    def test_modify_02(self,login_fixture,id,name,subject,price,applicablePerson,info):
        headers = {
            "Authorization": login_fixture
        }
        json={
            "id":id,
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson":applicablePerson,
            "info": info
        }
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.put_modify_query(headers=headers,json=json)
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "操作失败"
        assert result['code']== 500

    #####添加失败（未登录）#####
    @allure.severity(severity_level="critical")
    @pytest.mark.parametrize("id,name,subject,price,applicablePerson,info", get_data()['modify3'])
    def test_modify_03(self,login_fixture,id,name,subject,price,applicablePerson,info):
        headers = {
            "Authorization": None
        }
        json={
            "id":id,
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson":applicablePerson,
            "info": info
        }
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.put_modify_query(headers=headers,json=json)
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "请求访问：/clues/course，认证失败，无法访问系统资源"
        assert result['code']== 401

###点击可以同时将本文件中所有的测试用例同时执行
if __name__=='__main__':
    pytest.main()