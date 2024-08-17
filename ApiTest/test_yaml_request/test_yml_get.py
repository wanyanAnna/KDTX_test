import requests
import pytest
import  yaml

from utils.read_data import get_data

f=open("../config/data.yaml",encoding="utf8")
data=yaml.safe_load(f)

def test_getcode():
     url=get_data['code']['request']['url']
     print(url)
     r=requests.get(url=url)
     assert r.status_code==200
     result=r.json()
     assert result['msg']=='操作成功'



