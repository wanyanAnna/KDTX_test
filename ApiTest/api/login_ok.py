'''
   登录接口封装
'''
import requests
from utils.api_utils import api_util
import config


# 创建接口类
class LoginApi:

    # 初始化
    def __init__(self):
        super().__init__()
        self.uuid = None

    # 获取验证码
    def send_code(self):
        """
        获取短信验证码
        :param json_data:
        :return:
        """
        response = api_util.api_code().json()
        self.uuid = response['uuid']
        return response['uuid']



    # 登录
    def login(self,username, password,code):
        """
        用户登录接口
        :param username:
        :param password:
        :return:
        """
        json_data = {
            "username": username,
            "password": password,
            "code":code,
            "uuid":self.uuid

        }

        return api_util.api_login(json=json_data)


loginApi = LoginApi()