# Generated by Django 2.1.3 on 2018-11-27 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jfapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='toux',
            field=models.ImageField(upload_to='.../dist/img/', verbose_name='用户头像'),
        ),
    ]
