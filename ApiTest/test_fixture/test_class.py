import requests
import pytest

###代表此函数的作用范围是类，对每个类调用一次func函数
@pytest.fixture(scope="function",autouse=True)
def func():
    print("我是前置步骤")

class Test_api_params:

    uuid1=''


    ####获取验证码
    def test_getcode(self):
        url = "http://kdtx-test.itheima.net/api/captchaImage"
        r = requests.get(url=url)
        assert r.status_code == 200
        result = r.json()
        assert result['msg'] == '操作成功'
        uuid=result['uuid']
        Test_api_params.uuid1=uuid
        #return uuid

    ###############################POST请求方式########################################
    def test_post_login(self):
        #uuid2=self.test_getcode()
        json={
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            # "uuid": uuid2
            "uuid": Test_api_params.uuid1
        }

        r=requests.post(url="http://kdtx-test.itheima.net/api/login",json=json)
        assert r.status_code==200

        result=r.json()
        assert result['msg'] == '操作成功'
        assert result['code'] == 200
        assert result['userId'] == 1


###点击可以同时将本文件中所有的测试用例同时执行
if __name__=='__main__':
    pytest.main()