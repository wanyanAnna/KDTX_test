import requests
import pytest
import yaml
from utils.read import base_data
apihost = base_data.read_ini()['host']['api_host']
get_data = base_data.read_yam()
class Test_api_params:

    uuid1=''
    token=''

    def setup_module(self):
        print("准备测试数据")

    def teardown_module(self):
        print("清理测试数据")


    ####获取验证码
    def test_getcode(self):
        r = requests.get(url=apihost+'/api/captchaImage')
        assert r.status_code == 200
        result = r.json()
        assert result['msg'] == '操作成功'
        uuid=result['uuid']
        Test_api_params.uuid1=uuid
        #return uuid

    ###############################parametrize值为数组嵌套形式，POST请求方式########################################
    @pytest.mark.parametrize("username,password,code", get_data['login2'])
    def test_post_login(self,username,password,code):
        #uuid2=self.test_getcode()
        json={
            "username": username,
            "password": password,
            "code": code,
            "uuid": Test_api_params.uuid1
        }

        r=requests.post(url=apihost+'/api/login',json=json)
        assert r.status_code==200

        result=r.json()
        assert result['msg'] == '操作成功'
        assert result['code'] == 200
        assert result['userId'] == 1
        Test_api_params.token=result['token']


    ####列表查询####
    def test_get_search(self):
        headers = {
            "Authorization": Test_api_params.token
        }
        param = get_data['search']
        r = requests.get(url=apihost+'/api/clues/course/list', params=param, headers=headers)
        assert r.status_code == 200
        print(r.status_code)
        print(r.json())


###点击可以同时将本文件中所有的测试用例同时执行
if __name__=='__main__':
    pytest.main()