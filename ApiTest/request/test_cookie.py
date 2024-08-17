import requests

#创建了一个会话
req=requests.session()
url='http://sellshop.5istudy.online/sell/user/login'
###############################Cookie########################################
data={
    "username": "test01",
    "password": "123456",

}

#######登录，req保存了cookie或者session
res=req.post(url=url,data=data)
# print(r.status_code)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print(r.text)
# print("####################################")

res2=req.get(url='http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10')
print(res2.text)