from django.http import HttpResponse
from DBModule.models import LiUser

def addUser(request):
    user = LiUser(
        userName='li',
        passWord='123456',
        userId='10002',
        phone='13200000000',
        sex=1,
        year=20
    )
    user.save()
    return HttpResponse('<p>用户添加成功</p>')

def loadAll(request):
    all = LiUser.objects.all()
    str = ""
    for user in all:
        str += "<li>%s</li>" % user.toSring(user)
    return HttpResponse(str)