import pytest

####conftest.py配置里面可以实现数据共享，不需要import就能自动找到一些配置

@pytest.fixture(scope='session')
def test_session():
    print("我是session级别的fixture")

@pytest.fixture(scope='function')
def test_func1():
    print("我是function级别的fixture")