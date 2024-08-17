import json

import requests

from utils.log_util import logger
from utils.read import base_data

apihost = base_data.read_ini()['host']['api_host']
#######此文件存放了所有的请求方法,,,具体的url地址存放在utils.api_utils文件中

class Method:
    def __init__(self):
        self.apihost = apihost
    def method_get_code(self,code_url):
        #####获取验证码接口
        #return requests.get(url=self.apihost+code_url)
        return self.get_request(code_url,"Get")

    def method_get_search(self,search_url,**kwargs):
        ####查询列表接口
        return self.get_request(search_url,"Get",**kwargs)

    def method_post_login(self,login_api,**kwargs):
        #####登录接口
        return self.get_request(login_api, "Post", **kwargs)

    def method_post_add(self,add_api,**kwargs):
        #####添加课程接口
        return self.get_request(add_api, "Post", **kwargs)

    def method_put_modify(self,modify_api,**kwargs):
        #####添加课程接口
        return self.get_request(modify_api, "Put", **kwargs)

    def method_del_modify(self,del_api,course_id,**kwargs):
        #####删除课程接口
        return self.get_request(del_api, "Del",course_id,**kwargs)

    def get_request(self, url, method, course_id=None, **kwargs):
        if method == 'Get':
            self.print_log(url, method, **kwargs)
            return requests.get(url=self.apihost+url,**kwargs)
        if method == 'Post':
            self.print_log(url, method, **kwargs)
            return requests.post(url=self.apihost+url,**kwargs)
        if method == 'Put':
            self.print_log(url, method, **kwargs)
            return requests.put(url=self.apihost+url,**kwargs)
        if method == 'Del':
            self.print_log(url, method,**kwargs)
            return requests.delete(url=self.apihost+url+f'/{course_id}' ,**kwargs)

    def print_log(self,url, method, **kwargs):

        json_data = dict(**kwargs).get("json")
        params_data = dict(**kwargs).get("params")
        headers=dict(**kwargs).get("headers")
        if json_data is not None:
            logger.info("接口请求的json数据是>>>\n{}".format(json.dumps(json_data,indent=2)))
        if params_data is not None:
            logger.info("接口请求的params数据是>>>\n{}".format(json.dumps(params_data, indent=2)))
        logger.info("接口请求的地址>>>\n{}".format(self.apihost+url))
        logger.info("接口请求的方法>>>\n{}".format(method))




