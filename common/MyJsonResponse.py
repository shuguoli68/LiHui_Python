from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

# 继承HttpResponse类，定义一个返回json数据的响应类
class JsonResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        # 重写content属性，返回rest_framework的JSON渲染器渲染的数据
        content = JSONRenderer().render(data)
        # 通过kwargs设置返回的数据类型为json
        kwargs['content_type'] = 'application/json'
        super(JsonResponse,self).__init__(content,**kwargs)