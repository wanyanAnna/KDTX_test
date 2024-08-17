##########pytest的规范#########
# 函数命名必须以test_开头
# 测试类必须以Test开头，并且不能有init方法
# 测试默认执行顺序，按函数的顺序执行
# 可以使用pytest-ordering插件 自定义顺序
import pytest


def test_one():
    expect=1
    actual=1
    assert expect ==actual

@pytest.mark.run(order=1)   ####自定义测试执行用例
def test_two():
    expect=1
    actual=2
    assert expect ==actual

class TestRule:
    def test_rule(self):
        assert 1==2
    def test_rule2(self):
        assert 1==1