"""jfdh2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from jfapp import views
from django.views.static import serve
from jfdh2.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('pdjg/',views.pdjg),
    path('login/',views.login),
    path('logout/', views.logout),
    path('jmkt/',views.jmkt),
    path('shebruk/',views.shebruk),
    path('yjgl/',views.yjgl),
    path('ccjg/',views.ccjg),
    path('fwqjg/',views.fwqjg),
    path('jkjg/',views.jkjg),
    path('lsjc/',views.lsjc),
    path('sbbf/',views.sbbf),
    path('sbcx/',views.sbcx),
    path('sbjx/',views.sbjx),
    path('ups/',views.ups),
    path('xfxt/',views.xfxt),
    path('xsp/',views.xsp),
    path('xspkt/',views.xspkt),
    path('xtjc/',views.xtjc),
    path('yxjc/',views.yxjc),
    path('zhskt/',views.zhskt),
    path('zhslsjc/',views.zhslsjc),
    re_path(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
]
