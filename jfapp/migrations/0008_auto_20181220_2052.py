# Generated by Django 2.1.4 on 2018-12-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jfapp', '0007_auto_20181204_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='toux',
            field=models.ImageField(upload_to='media/upload/img/', verbose_name='用户头像'),
        ),
    ]