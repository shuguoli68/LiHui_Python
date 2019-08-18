一、【命令】：

启动服务器：python manage.py runserver 0.0.0.0:8000
关闭：Ctrl + C

1、记录我们对models.py的所有改动，并且将这个改动迁移到migrations这个文件下生成一个文件例如：0001文件
python manage.py makemigrations

2、把这些改动作用到数据库也就是执行migrations里面新改动的迁移文件更新数据库，比如创建数据表，或者增加字段属性
python manage.py migrate



二、【数据库】

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


三、【json与字典转换】

import json
json.loads(json_str) json字符串转换成字典
json.dumps(dict) 字典转换成json字符串



四、【数据model】

primary_key 主键

auto_now = True ：则每次更新都会更新这个时间，设置为True，就无法在程序中手动为字段赋值，
在admin中字段也会成为只读的，字段会被“强制”更新到当前时间，你无法程序中手动为字段赋值

auto_now_add=True 则只是第一次创建添加，之后的更新不再改变

