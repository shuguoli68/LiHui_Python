# Generated by Django 2.2.4 on 2019-08-05 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBModule', '0003_remove_user_createtime'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='LiUser',
        ),
    ]