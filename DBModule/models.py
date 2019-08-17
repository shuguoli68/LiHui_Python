from django.db import models


# Create your models here.
# LiUser的数据model，用户信息
class LiUser(models.Model):
    userName = models.CharField(max_length=20, default='userName')
    passWord = models.CharField(max_length=20, default='123456')
    userId = models.CharField(max_length=20, default='10001', primary_key='userId')
    phone = models.CharField(max_length=50, default='13200000000')
    sex = models.IntegerField(default=1, blank=True)
    year = models.IntegerField(default=18, blank=True)

    # createTime = models.DateField(auto_now_add=True, blank=True)

    def toSring(self, LiUser):
        return "LiUser(userName:" + self.userName + ",passWord:" + self.passWord + ",userId:" + self.userId + \
               ",phone:" + self.phone + ",sex:" + str(self.sex) + ",year:" + str(self.year) + ")"

# CutPage的数据model，分页使用：limit、offset
class CutPage(models.Model):
    # 默认每页显示的条数
    default_limit = 20
    # url 中传入的显示数据条数的参数
    limit_query_param = 'limit'
    # url中传入的数据位置的参数
    offset_query_param = 'offset'
    # 最大每页显示条数
    max_limit = None