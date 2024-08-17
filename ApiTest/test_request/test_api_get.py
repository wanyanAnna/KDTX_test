import requests
import pytest

@pytest.mark.p0
def test_getcode():
     url='http://kdtx-test.itheima.net/api/captchaImage'
     r=requests.get(url=url)
     assert r.status_code==200
     result=r.json()
     assert result['msg']=='操作成功'

def test_get_search():
     ###############################GET请求方式########################################
     params={
          "name":"测试开发提升课01"
     }
     headers={
          "Authorization":"eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZhY2Y5NjI5LWUzZjQtNDg5Ny1iOTg1LWYyYzEzNTlmZjUzZiJ9.UF6i3Qe3L8W4X1f3RU4XEIFU3p8HWKTdSGw1W5Deu7J6rusfehQs72_Dk2nDGSNkD3E-BPVqTAJr-PFoxmhMqw"
     }
     r=requests.get(url="http://kdtx-test.itheima.net/api/clues/course/list",params=params,headers=headers)
     assert r.status_code==200

     print(r.status_code)
     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
     print(r.json())
     print("###############################")

