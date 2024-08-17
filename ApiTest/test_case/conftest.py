import pytest
from utils.log_util import logger
from api.login_ok import loginApi

from utils.read import base_data

def get_data():
    return base_data.read_data()

@pytest.fixture(scope='class',autouse=True)
def test_func1():
    logger.info("开始执行测试用例")
    yield
    logger.info("测试用例执行结束")

#####封装获取验证码成功接口，用于测试登录接口的用例
@pytest.fixture()
def getcode_fixture():
    uuid = loginApi.send_code()
    return uuid

### 封装登录成功接口，用于后续列表查询等用例的正确使用
@pytest.fixture(scope="session")
def login_fixture():
    data = get_data()['login1']
    username = data['username']
    password = data['password']
    code=data['code']
    loginApi.send_code()
    result= loginApi.login(username,password,code).json()
    return result['token']