# Generated by Django 2.1.3 on 2018-12-04 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jfapp', '0006_auto_20181129_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shebdj',
            name='shebIP',
            field=models.GenericIPAddressField(null=True, unique=True, verbose_name='IP地址'),
        ),
        migrations.AlterField(
            model_name='yjgl',
            name='bjshij',
            field=models.DateTimeField(auto_now=True, verbose_name='报警时间'),
        ),
    ]
