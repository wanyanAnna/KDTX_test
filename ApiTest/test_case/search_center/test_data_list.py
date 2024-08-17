import allure
import requests
import pytest
import yaml



from test_case.api import response
from test_case.conftest import get_data



#get_data = base_data.read_yam()


@allure.feature("查询课程列表模块")
class Test_search:


    def setup_module(self):
        print("准备测试数据")

    def teardown_module(self):
        print("清理测试数据")



    ##########列表查询##########
    #####查询已存在的信息#####
    @allure.severity(severity_level="blocker")
    def test_get_search_01(self,login_fixture):
        headers = {
            "Authorization": login_fixture
        }
        params = get_data()['search1']
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.get_search_query(params=params,headers=headers)
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "查询成功"
        assert result['code']== 200
        assert result['total']!= 0

    #####查询不存在的信息#####
    @allure.severity(severity_level="critical")
    def test_get_search_02(self,login_fixture):
        headers = {
            "Authorization": login_fixture
        }
        params = get_data()['search2']
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.get_search_query(params=params,headers=headers)
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "查询成功"
        assert result['code']== 200 or 201
        assert result['total']== 0

    #####显示默认设置的数据（不输入查询参数）#####
    @allure.severity(severity_level="critical")
    def test_get_search_03(self,login_fixture):
        headers = {
            "Authorization": login_fixture
        }
        params = get_data()['search3']
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.get_search_query(params=params,headers=headers)
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "查询成功"
        assert result['code']== 200 or 201
        assert result['total']!= 0

    #####查询失败（用户未登录）#####
    @allure.severity(severity_level="critical")
    def test_get_search_04(self):
        headers = {
            "Authorization": None
        }
        params = get_data()['search4']
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.get_search_query(params=params,headers=headers)
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "请求访问：/clues/course/，认证失败，无法访问系统资源"
        assert result['code']== 401


###点击可以同时将本文件中所有的测试用例同时执行
if __name__=='__main__':
    pytest.main()