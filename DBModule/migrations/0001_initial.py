# Generated by Django 2.2.4 on 2019-08-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userName', models.CharField(default='userName', max_length=20)),
                ('passWord', models.CharField(default='123456', max_length=20)),
                ('userId', models.CharField(default='10001', max_length=20, primary_key='userId', serialize=False)),
                ('phone', models.CharField(default='13200000000', max_length=50)),
                ('sex', models.IntegerField(blank=True, default=1, max_length=9)),
                ('year', models.IntegerField(blank=True, default=18, max_length=9)),
                ('createTime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
