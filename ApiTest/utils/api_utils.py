######此文件存放所有的的接口URL地址####
from method_config.method_request import Method

class Api(Method):
    def __init__(self):
        super(Api, self).__init__()
    def api_code(self):
        return self.method_get_code('/api/captchaImage')

    def api_login(self,json):
        return self.method_post_login('/api/login',json=json)

    def api_search(self,**kwargs):
        return self.method_get_search('/api/clues/course/list',**kwargs)

    def api_add(self,**kwargs):
        return self.method_post_add('/api/clues/course',**kwargs)

    def api_modify(self,**kwargs):
        return self.method_put_modify('/api/clues/course',**kwargs)
    def api_del(self,course_id,**kwargs):
        return self.method_del_modify('/api/clues/course/',course_id,**kwargs)

###实例化类
api_util = Api()