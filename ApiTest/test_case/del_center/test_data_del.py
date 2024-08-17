import allure
import requests
import pytest
import yaml

from test_case.api import response
from test_case.conftest import get_data

@allure.feature("删除课程")
class Test_del:
    def setup_module(self):
        print("准备测试数据")
    def teardown_module(self):
        print("清理测试数据")

    ##########课程删除成功##########
    @allure.severity(severity_level="blocker")
    # @pytest.mark.parametrize("id,name,subject,price,applicablePerson,info", get_data()['del1'])
    def test_del_01(self,login_fixture):
        headers = {
            "Authorization": login_fixture
        }
        # params={
        #     "id":id,
        #     "name": name,
        #     "subject": subject,
        #     "price": price,
        #     "applicablePerson":applicablePerson,
        #     "info": info
        # }
        params=get_data()['del0']
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.del_modify_query(headers=headers,course_id=params['id'])
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "操作成功"
        assert result['code']== 200

    ##########课程删除失败##########
    @allure.severity(severity_level="blocker")
    @pytest.mark.parametrize("id", get_data()['del2'])
    def test_del_02(self,login_fixture,id):
        headers = {
            "Authorization": login_fixture
        }
        id= id[0]

        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.del_modify_query(headers=headers,course_id=id)
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "操作失败"
        assert result['code']== 500
    #####课程删除失败（用户未登录）#####
    @allure.severity(severity_level="critical")
    def test_del_03(self):
        headers = {
            "Authorization": ''
        }
        params = get_data()['del3']
        ######动态自定义allure报告，title和story的信息写在yaml文件中
        title = get_data()['text']['title']
        story = get_data()['text']['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        ##########################################
        #r = api_utils.api_search(params=params,headers=headers)    ###关键字传参
        r = response.del_modify_query(headers=headers,course_id=params['id'])
        assert r.status_code == 200
        result=r.json()
        assert result['msg']== "请求访问：/clues/course/{}，认证失败，无法访问系统资源".format(params['id'])
        assert result['code']== 401


###点击可以同时将本文件中所有的测试用例同时执行
if __name__=='__main__':
    pytest.main()