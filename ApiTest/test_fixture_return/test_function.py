import requests
import pytest



###代表此函数的作用范围是方法，对每个方法都会调用一次func函数,若不指定scope,默认是function
# @pytest.fixture(scope="function",autouse=True)
# def func():
#     print("我是前置步骤")

class Test_kdtx:
    ####获取验证码
    uuid=''
    authorization=''
    def test_getcode(self):
        url = "http://kdtx-test.itheima.net/api/captchaImage"
        r = requests.get(url=url)
        assert r.status_code == 200
        result = r.json()
        assert result['msg'] == '操作成功'
        uuid=result['uuid']
        Test_kdtx.uuid=uuid

    ###############################POST请求方式########################################
    ###登录
    def test_post_login(self):
        json={
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            # "uuid": uuid2
            "uuid": Test_kdtx.uuid
        }

        r=requests.post(url="http://kdtx-test.itheima.net/api/login",json=json)
        assert r.status_code==200

        result=r.json()
        assert result['msg'] == '操作成功'
        assert result['code'] == 200
        assert result['userId'] == 1
        token=result['token']
        Test_kdtx.authorization=token


    ####列表查询####
    def test_get_search(self,test_params_search):
        #Authorization=test_post_login()
        headers = {
            "Authorization": Test_kdtx.authorization
        }
        r = requests.get(url="http://kdtx-test.itheima.net/api/clues/course/list", params=test_params_search, headers=headers)
        assert r.status_code == 200

        print(r.status_code)
        print(r.json())


###点击可以同时将本文件中所有的测试用例同时执行
if __name__=='__main__':
    pytest.main()
