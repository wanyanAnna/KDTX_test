import allure
import requests
import pytest
import yaml
from utils.read import base_data
from test_case.api import response
from test_case.conftest import get_data
#get_data = base_data.read_data()

@allure.epic("客达天下epic")
@allure.feature("登录模块")
class Test_api_params:



    def setup_module(self):
        print("准备测试数据")

    def teardown_module(self):
        print("清理测试数据")


    ####获取验证码
    # @allure.story("获取验证码story")
    # def test_getcode(self):
    #     r = response.get_code_query()
    #     assert r.status_code == 200
    #     result = r.json()
    #     assert result['msg'] == '操作成功'
    #     uuid=result['uuid']
    #     Test_api_params.uuid1=uuid
        #return uuid

    ################登录成功（全部参数正确）#########
    ###############################parametrize值为数组嵌套形式，POST请求方式########################################
    @allure.story("登录网站story")
    @pytest.mark.parametrize("username,password,code", [get_data()['login'][0]])
    def test_post_login01(self,getcode_fixture,username,password,code):
        json={
            "username": username,
            "password": password,
            "code": code,
            "uuid": getcode_fixture
        }
        # r = api_utils.api_login(json=json)
        r = response.post_login_query(json=json)
        assert r.status_code == 200
        result=r.json()
        assert result['msg'] == '操作成功'
        assert result['code'] == 200

    ################登录失败（用户名为空）#########
    ###############################parametrize值为数组嵌套形式，POST请求方式########################################
    @pytest.mark.parametrize("username,password,code", [get_data()['login'][1]])
    def test_post_login02(self,getcode_fixture,username,password,code):
        json={
            "username": username,
            "password": password,
            "code": code,
            "uuid": getcode_fixture
        }
        # r = api_utils.api_login(json=json)
        r = response.post_login_query(json=json)
        assert r.status_code == 200
        result=r.json()
        assert result['msg'] == '用户不存在/密码错误'
        assert result['code'] == 500

    ################登录失败（验证码错误）#########
    ###############################parametrize值为数组嵌套形式，POST请求方式########################################
    @pytest.mark.parametrize("username,password,code", [get_data()['login'][2]])
    def test_post_login03(self,getcode_fixture,username,password,code):
        json={
            "username": username,
            "password": password,
            "code": code,
            "uuid": getcode_fixture
        }
        # r = api_utils.api_login(json=json)
        r = response.post_login_query(json=json)
        assert r.status_code == 200
        result=r.json()
        assert result['msg'] == '用户不存在/密码错误'
        assert result['code'] == 500

    ################登录失败（用户名不存在）#########
    ###############################parametrize值为数组嵌套形式，POST请求方式########################################
    @pytest.mark.parametrize("username,password,code", [get_data()['login'][3]])
    def test_post_login04(self,getcode_fixture,username,password,code):
        json={
            "username": username,
            "password": password,
            "code": code,
            "uuid": getcode_fixture
        }
        # r = api_utils.api_login(json=json)
        r = response.post_login_query(json=json)
        assert r.status_code == 200
        result=r.json()
        assert result['msg'] == '验证码错误'
        assert result['code'] == 500

###点击可以同时将本文件中所有的测试用例同时执行
if __name__=='__main__':
    pytest.main()