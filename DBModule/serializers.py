from rest_framework_dyn_serializer import serializers
from .models import *


# 对LiUser的解析
class UserSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = LiUser
        # 和"__all__"等价
        fields = ('userName', 'passWord', 'userId', 'phone', 'sex', 'year')


# 对LiUser的分页解析
class UserListSerialize(serializers.ModelSerializer):
    class Meta:
        model = CutPage
        fields = ('pageIndex','pageNumber')
