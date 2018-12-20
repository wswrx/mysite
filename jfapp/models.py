from django.db import models

# Create your models here.

class User(models.Model):
    nich = models.CharField(max_length=16,verbose_name='昵称')
    yhm = models.CharField(max_length=32,verbose_name='用户名')
    mima = models.CharField(verbose_name='密码',max_length=32)
    youx = models.EmailField(verbose_name='邮箱')
    bm_choice = (
        (0,'信息科'),
        (1, '农水科'),
        (2, '灌溉科'),
        (3, '财务科'),
    )
    bum = models.IntegerField(verbose_name='用户部门',choices=bm_choice,default=0)
    shouj = models.IntegerField(verbose_name='手机号码')
    toux = models.ImageField(verbose_name='用户头像',upload_to = "upload/img/")
    shij = models.DateTimeField(verbose_name='注册时间',auto_now=True)

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.yhm

class Shebdj(models.Model):
    shebmc = models.CharField(max_length=32,verbose_name='设备名称')
    anzhwz = models.CharField(max_length=32,verbose_name='安装位置')
    shebIP = models.GenericIPAddressField(verbose_name='IP地址',unique=True,null=True)
    xt_choice = (
        (0, '监控系统'),
        (1, '森林防火系统'),
        (2, '网络系统'),
        (3, '机房系统'),
        (4, '配电系统'),
        (5, '智能管理系统'),
    )
    shebxt = models.IntegerField(verbose_name='子系统', choices=xt_choice, default=0)
    yssj = models.DateField(verbose_name='验收时间')
    zbsj = models.DateField(verbose_name='质保到期时间')
    shebtp = models.ImageField(verbose_name='设备图片',upload_to = "upload/img/")

    class Meta:
        verbose_name = '设备管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shebmc

class Wd(models.Model):
    jfwd = models.IntegerField(verbose_name='机房温度')
    zhswd = models.IntegerField(verbose_name='指挥室温度')
    fwqjgwd = models.IntegerField(verbose_name='服务器机柜温度')
    pdjgwd = models.IntegerField(verbose_name='配电机柜温度')
    jkjgwd = models.IntegerField(verbose_name='监控机柜温度')
    ccjgwd = models.IntegerField(verbose_name='存储机柜温度')
    dapzwd = models.IntegerField(verbose_name='大屏左温度')
    dapywd = models.IntegerField(verbose_name='大屏右温度')
    wdshij = models.DateTimeField(verbose_name='采集时间', auto_now=True)

    class Meta:
        verbose_name = '温度检测'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.wdshij)

class Pd(models.Model):
    aV = models.IntegerField(verbose_name='A项电压')
    bV = models.IntegerField(verbose_name='B项电压')
    cV = models.IntegerField(verbose_name='C项电压')
    aA = models.IntegerField(verbose_name='A项电流')
    bA = models.IntegerField(verbose_name='B项电流')
    cA = models.IntegerField(verbose_name='C项电流')
    pdshij = models.DateTimeField(verbose_name='采集时间', auto_now=True)

    class Meta:
        verbose_name = '配电检测'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.pdshij)

class Yjgl(models.Model):
    bjshij = models.DateTimeField(verbose_name='报警时间',auto_now=True)
    bj_choice = (
        (0, '电压过高'),
        (1, '电流过高'),
        (2, '漏水'),
        (3, '温度过高'),
    )
    bjlx = models.IntegerField(verbose_name='报警类型', choices=bj_choice, default=0)
    bjxx = models.CharField(verbose_name='报警信息',max_length=64)

    class Meta:
        verbose_name = '报警信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bjxx