import random

import pytest

from utils.read_self_function import get_data
from faker import Faker
fake=Faker(locale="zh-CN")
def func_yaml(data):
    if isinstance(data,dict):
        for key,value in data.items():
            if 'random' in str(value):
                data[key] =eval(str(value))  ##这个函数的作用是，返回传入字符串的表达式的结果
            if 'age' in str(value):
                data[key] =eval(str(value))  ##这个函数的作用是，返回传入字符串的表达式的结果
    return data

def random_name():
    return fake.name()
def age():
    return random.randint(10,60)

@pytest.mark.parametrize("person",get_data["person"])
def test_self_person(person):
    func_yaml(person)
    print(func_yaml(person))
