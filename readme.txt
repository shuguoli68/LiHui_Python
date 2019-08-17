命令：
启动服务器：python manage.py runserver 0.0.0.0:8000
关闭：Ctrl + C

1、记录我们对models.py的所有改动，并且将这个改动迁移到migrations这个文件下生成一个文件例如：0001文件
python manage.py makemigrations

2、把这些改动作用到数据库也就是执行migrations里面新改动的迁移文件更新数据库，比如创建数据表，或者增加字段属性
python manage.py migrate

