import pytest

###多参数多次循环
@pytest.mark.parametrize("name,word",[("aa","我是aa"),("bb","我是bb")])
def test_parametrize_03(name,word):
    print(name,"你好"+word)
    print(f'{name}说{word}')



###参数值为字典
@pytest.mark.parametrize("hero", [{"name":"aaa"},{"name":"bbb"},{"name":"ccc"}])
def test_parametrize_04(hero):
    print(hero["name"])

