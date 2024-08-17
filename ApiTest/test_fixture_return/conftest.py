import pytest

####conftest.py配置里面可以实现数据共享，不需要import就能自动找到一些配置

@pytest.fixture(scope='session')
def test_session():
    print("我是session级别的fixture")

@pytest.fixture(scope='function')
def test_func1():
    print("我是function级别的fixture")

@pytest.fixture(scope='function')
def test_params_search():
    params = {
            "name": "测试开发提升课01",
            "code": "dx2jlgwo",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01",
    }
    # yield   print("我是后置处理")
    return params