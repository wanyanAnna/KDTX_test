import requests


###############################POST请求方式########################################
json={
    "username": "admin",
    "password": "HM_2023_test",
    "code": "2",
    "uuid": "7098215566c848c684d89f01757f3434"
}

r=requests.post(url="http://kdtx-test.itheima.net/api/login",json=json)
print(r.status_code)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(r.json())
print("####################################")
