import json

from utils.api_utils import Api
from utils.log_util import logger
######此文件用于接收响应数据#####
class Response(Api):
    def __init__(self):
        super(Response, self).__init__()
    def get_code_query(self):
        response = self.api_code()
        self.response_log(response)
        return response

    def post_login_query(self,**kwargs):
        response = self.api_login(**kwargs)
        self.response_log(response)
        return response

    def post_add_query(self,**kwargs):
        response = self.api_add(**kwargs)
        self.response_log(response)
        return response
    def put_modify_query(self,**kwargs):
        response = self.api_modify(**kwargs)
        self.response_log(response)
        return response

    def del_modify_query(self,**kwargs):
        response = self.api_del(**kwargs)
        self.response_log(response)
        return response

    def get_search_query(self,**kwargs):
        response = self.api_search(**kwargs)
        self.response_log(response)
        return response

    def result_response(self):
        pass

    def response_log(self,response):
        if response.status_code==200 or response.status_code==201:
            self.result_response
            return logger.info("接口返回内容>>>>\n" + json.dumps(response.json(), ensure_ascii=False,indent=2))
        else :
            self.result_response()
            return logger.info("接口状态码不是2，请检查")







response=Response()

