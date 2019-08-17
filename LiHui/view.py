from django.http import HttpResponse
from DBModule.models import LiUser
from DBModule.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from common.MyJsonResponse import JsonResponse

def hello(request):
    return HttpResponse("注册LiHui")

@csrf_exempt
def loadAll(request):
    if request.method == 'GET':
        # 查询所有
        all = LiUser.objects.all()
        # 实例化一个序列化器，指示为多条数据的序列化
        ser = UserSerializer(all, many=True)
        # 返回序列化的json数据
        return JsonResponse(ser.data)
    elif request.method == 'POST':
        # 解析http请求的数据
        userData = JSONParser().parse(request)
        # 实例化一个序列化器
        ser = UserSerializer(data=userData)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # 解析http请求的数据
        userData = JSONParser().parse(request)
        # 实例化一个序列化器
        ser = UserSerializer(data=userData)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ser.errors, status=status.HTTP_400_BAD_REQUEST)
