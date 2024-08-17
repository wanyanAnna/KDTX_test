import requests
import pytest


###代表此函数的作用范围是当前py文件，不管类和方法有多少个，但只会调用一次func函数
@pytest.fixture(scope="module",autouse=True)
def func():
    print("我是前置步骤")

####获取验证码
def test_getcode():
    url = "http://kdtx-test.itheima.net/api/captchaImage"
    r = requests.get(url=url)
    assert r.status_code == 200
    result = r.json()
    assert result['msg'] == '操作成功'
    uuid=result['uuid']
    return uuid

###############################POST请求方式########################################
def test_post_login():
    uuid2=test_getcode()
    json={
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        # "uuid": uuid2
        "uuid": uuid2
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
