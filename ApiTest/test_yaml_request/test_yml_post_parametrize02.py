import requests
import pytest
import yaml
from utils.read_data import get_data

class Test_api_params:

    uuid1=''

    def setup_module(self):
        print("准备测试数据")

    def teardown_module(self):
        print("清理测试数据")


    ####获取验证码
    @pytest.mark.parametrize("url",get_data['code'])
    def test_getcode(self,url):
        r = requests.get(url=url)
        assert r.status_code == 200
        result = r.json()
        assert result['msg'] == '操作成功'
        uuid=result['uuid']
        Test_api_params.uuid1=uuid
        #return uuid

    ###############################parametrize值为数组嵌套形式，POST请求方式########################################
    @pytest.mark.parametrize("url,username,password,code", get_data['login2'])
    def test_post_login(self,url,username,password,code):
        #uuid2=self.test_getcode()
        json={
            "username": username,
            "password": password,
            "code": code,
            # "uuid": uuid2
            "uuid": Test_api_params.uuid1
        }

        r=requests.post(url=url,json=json)
        assert r.status_code==200

        result=r.json()
        assert result['msg'] == '操作成功'
        assert result['code'] == 200
        assert result['userId'] == 1


###点击可以同时将本文件中所有的测试用例同时执行
if __name__=='__main__':
    pytest.main()
