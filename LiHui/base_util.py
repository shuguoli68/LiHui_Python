'''
import json
json.loads(json_str) json字符串转换成字典
json.dumps(dict) 字典转换成json字符串
'''


# 返回的模型，如果成功可以只传data
def baseResponse(data, code=200, msg='请求成功'):
    return {
        'code': code,
        'msg': msg,
        'data': data,
    }
