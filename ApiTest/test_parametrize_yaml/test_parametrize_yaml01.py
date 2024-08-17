import pytest
from utils.read_data import get_data

######实现yaml+paramters 测试用例数据配置与传参分离

######传参为字典形式
@pytest.mark.parametrize("hero",get_data['heros'])
def test_parametrize_yaml01(hero):
    name=hero["name"]
    word=hero["word"]
    hp = hero["Hp"]
    print(f"{name}的台词是{word},我目前的血量是{hp}")

######传参是数组形式，单参数多次循环
@pytest.mark.parametrize("name",get_data['heros_name'])
def test_parametrize_yaml02(name):
    print('我是'+name)


######传参是数组形式，多参数多次循环
@pytest.mark.parametrize("name,word",get_data['heros_name_word'])
def test_parametrize_yaml03(name, word):
    print(f"{name}的台词是{word}")



