from django.http import HttpResponse
from DBModule.models import *
from DBModule.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from common.MyJsonResponse import *
from django.core.paginator import Paginator
from LiHui.base_util import *

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
def userList(request):
    if request.method == 'GET':
        # 查询所有
        all = LiUser.objects.all()
        p = Paginator(all, 6)  # 3条数据为一页，实例化分页对象
        # 实例化一个序列化器，指示为多条数据的序列化
        ser = UserSerializer(p.page(1), many=True)
        # 返回序列化的json数据
        return JsonResponse(ser.data)
    elif request.method == 'POST':  # 正确的分页姿势
        pageData = JSONParser().parse(request)
        page = UserListSerialize(data=pageData)
        pageIndex = 1
        pageNumber = 20
        if page.is_valid():
            pageIndex = page.data.get('pageIndex')
            pageNumber = page.data.get('pageNumber')
        all = LiUser.objects.all()
        p = Paginator(all, pageNumber)  # pageNumber条数据为一页，实例化分页对象
        allPage = p.num_pages
        print('总条数：', p.count, '，总页数：', allPage)
        if 0 < pageIndex <= allPage:
            ser = UserSerializer(p.page(pageIndex), many=True)
            # 返回序列化的json数据
            jsonStr = baseResponse(data=ser.data)
            return JsonResponse(jsonStr)
        else:
            jsonStr = baseResponse(data={}, code=1050, msg='没有更多数据')
            return JsonResponse(jsonStr)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        # 解析http请求的数据
        userData = JSONParser().parse(request)
        # 实例化一个序列化器
        ser = UserSerializer(data=userData)
        if ser.is_valid():
            ser.save()
            try:
                one = LiUser.objects.all().get(userId='1018')
                print(one)
            except Exception:
                print('发生异常，找不到数据')
            print('userId', ser.data.get('userId'))
            jsonStr = baseResponse(ser.data, msg='注册成功')
            return JsonResponse(jsonStr)
        return JsonResponse(baseResponse(ser.errors, code=1101, msg='注册失败，请求数据不合法'))
