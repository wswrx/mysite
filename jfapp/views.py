from django.shortcuts import render,redirect,HttpResponse
import json
from jfapp import models
from utils import pagination
from utils import pagination_v1 as pv

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')
        yonghu = models.User.objects.filter(nich=user,mima=pwd)
        if yonghu:
            request.session['username'] = yonghu[0].yhm
            request.session['toux'] = '/' + str(yonghu[0].toux)
            request.session['bum'] = yonghu[0].get_bum_display()
            request.session['is_login'] = True
            request.session.set_expiry(0)
            return redirect('/index/')
        else:
            return render(request,'login.html')

def index(request):
    wendu = models.Wd.objects.order_by('-id')[0]
    peid = models.Pd.objects.order_by('-id')[0]
    if request.method == 'GET':
        if request.session.get('is_login',None):
            return render(request, 'index.html',{'wendu':wendu,'peid':peid})
        else:
            return redirect('/login/')
    if request.method == 'POST':
        ret = {
            'jfwd':wendu.jfwd,
            'zhswd':wendu.zhswd,
            'fwqjgwd':wendu.fwqjgwd,
            'pdjgwd':wendu.pdjgwd,
            'jkjgwd':wendu.jkjgwd,
            'ccjgwd':wendu.ccjgwd,
            'dapwd':wendu.dapywd,
            'pdav':peid.aV,
            'pdbv':peid.bV,
            'pdcv':peid.cV,
            'pdaa':peid.aA,
            'pdba':peid.bA,
            'pdca':peid.cA,
        }
        return HttpResponse(json.dumps(ret))


def logout(request):
    request.session.clear()
    return redirect('/login/')

def pdjg(request):
    if request.session.get('is_login', None):
        return render(request, 'pdjg.html')
    else:
        return redirect('/login/')

def jmkt(request):
    if request.session.get('is_login', None):
        return render(request,'jmkt.html')
    else:
        return redirect('/login/')

def shebruk(request):
    if request.session.get('is_login', None):
        sheb = models.Shebdj.objects.all()
        LIST = []
        for i in sheb:
            LIST.append(i)
        current_page = request.GET.get('p',1)
        current_page = int(current_page)
        page_obj = pv.PageInfo(current_page, len(LIST))
        data = LIST[page_obj.From():page_obj.To()]
        cuont = [page_obj.From(), page_obj.To(), len(sheb)]
        pagetest = pv.Custompager('/shebruk/?p=',current_page,page_obj.TotalPage())
        return render(request,'shebruk.html',{'sheb':data,'page':pagetest,'count':cuont})
    else:
        return redirect('/login/')

def yjgl(request):
    if request.session.get('is_login', None):
        bjxx = models.Yjgl.objects.all()
        LIST = []
        for i in bjxx:
            LIST.append(i)
        current_page = request.GET.get('p', 1)
        current_page = int(current_page)
        page_obj = pv.PageInfo(current_page, len(LIST),peritems=10)
        data = LIST[page_obj.From():page_obj.To()]
        cuont = [page_obj.From(),page_obj.To(),len(bjxx)]
        pagetest = pv.Custompager('/yjgl/?p=', current_page, page_obj.TotalPage())
        return render(request,'yjgl.html',{'bjxx':data,'page':pagetest,'cuont':cuont})

def ccjg(request):
    if request.session.get('is_login', None):
        return render(request,'ccjg.html')

def fwqjg(request):
    if request.session.get('is_login', None):
        return render(request,'fwqjg.html')

def jkjg(request):
    if request.session.get('is_login', None):
        return render(request,'jkjg.html')

def lsjc(request):
    if request.session.get('is_login', None):
        return render(request,'lsjc.html')

def sbbf(request):
    if request.session.get('is_login', None):
        return render(request,'sbbf.html')

def sbcx(request):
    if request.session.get('is_login', None):
        return render(request,'sbcx.html')

def sbjx(request):
    if request.session.get('is_login', None):
        return render(request,'sbjx.html')

def ups(request):
    if request.session.get('is_login', None):
        return render(request,'ups.html')

def xfxt(request):
    if request.session.get('is_login', None):
        return render(request,'xfxt.html')

def xsp(request):
    if request.session.get('is_login', None):
        return render(request,'xsp.html')

def xspkt(request):
    if request.session.get('is_login', None):
        return render(request,'xspkt.html')

def xtjc(request):
    if request.session.get('is_login', None):
        return render(request,'xtjc.html')

def yxjc(request):
    if request.session.get('is_login', None):
        return render(request,'yxjc.html')

def zhskt(request):
    if request.session.get('is_login', None):
        return render(request,'zhskt.html')

def zhslsjc(request):
    if request.session.get('is_login', None):
        return render(request,'zhslsjc.html')