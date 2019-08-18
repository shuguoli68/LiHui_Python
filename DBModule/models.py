from django.db import models
'''
对数据model的CRUD操作：
1、增
LiUser.objects.create(userId='yangmv',userName='123456'  ... )
或者
obj = LiUser(userId='yangmv',userName='123456'  ... )
obj.save()
或者
dic = {'user':'yangmv','userName':'123456'}
LiUser.objects.create(**dic)

2、删
LiUser.objects.filter(userId='1001').delete()

3、改
LiUser.objects.filter(userId='1001').update(pwd='520')
或者
obj = LiUser.objects.get(userId='1001')
obj.pwd = '520'
obj.save()

4、查：
LiUser.objects.all()
LiUser.objects.all().values('user') #只取user列
LiUser.objects.all().values_list('id','user') #取出id和user列，并生成一个列表
LiUser.objects.get(userId=1001)
LiUser.objects.get(userName='userName')
'''

# Create your models here.
# LiUser的数据model，用户信息
class LiUser(models.Model):
    userName = models.CharField(max_length=20, default='userName')
    passWord = models.CharField(max_length=20, default='123456')
    userId = models.CharField(max_length=20, default='10001', primary_key='userId')
    phone = models.CharField(max_length=50, default='13200000000', null=True)
    sex = models.IntegerField(default=1, blank=True, null=True)
    year = models.IntegerField(default=18, blank=True, null=True)
    ctTime = models.DateTimeField(auto_now_add=True, null=True)
    upTime = models.DateTimeField(auto_now=True, null=True)
    
    '''
    primary_key 主键
    auto_now = True ：则每次更新都会更新这个时间
    auto_now_add=True 则只是第一次创建添加，之后的更新不再改变
    '''
    # createTime = models.DateField(auto_now_add=True, blank=True)

    def toSring(self, LiUser):
        return "LiUser(userName:" + self.userName + ",passWord:" + self.passWord + ",userId:" + self.userId + \
               ",phone:" + self.phone + ",sex:" + str(self.sex) + ",year:" + str(self.year) + ")"

# CutPage的数据model，分页使用：页码、每页条数
class CutPage(models.Model):
    pageIndex = models.IntegerField(default=1, blank=True)
    pageNumber = models.IntegerField(default=20, blank=True)