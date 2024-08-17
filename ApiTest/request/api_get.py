import requests


###############################GET请求方式########################################
params={
     "name":"测试开发提升课01"
}
headers={
     "Authorization":"eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjE5MTNiYjc4LWRjMTctNDZmNi04ZDA0LWNhYzc2MmEwNjk2NyJ9._-b8NXUEZFwTzPOKQmSpNydvdiZvPlQF43mb-ob3Gb_kLMhBxjNwaIEexVN7XawbMbIjUPD28FtrnVQScxRliQ"
}
r=requests.get(url="http://kdtx-test.itheima.net/api/clues/course/list",params=params,headers=headers)
print(r.status_code)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(r.json())
print("###############################")


