import pytest

##单参数单次循环
@pytest.mark.parametrize("key",["value"])
def test_parametrize_01(key):
    print(key)
    print("我是"+key)


####单参数，多次循环
#运行时将数组里的值分别赋值给变量，每赋值一次运行一次函数，执行一次测试用例
@pytest.mark.parametrize("key",["aaa","bbb","ccc"])
def test_parametrize_02(key):
    print("我是"+key)