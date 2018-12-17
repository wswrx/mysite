import os,django
os.environ['DJANGO_SETTINGS_MODULE']='jfdh2.settings'
django.setup()

from jfapp import models
import random,time,datetime

def Pdcj(s):
    while True:
        av_v = random.randint(200, 240)
        bv_v = random.randint(200, 240)
        cv_v = random.randint(200, 240)
        aa_v = random.randint(1, 20)
        ba_v = random.randint(1, 20)
        ca_v = random.randint(1, 20)
        pd_v = {
            'aV':av_v,
            'bV':bv_v,
            'cV':cv_v,
            'aA':aa_v,
            'bA':ba_v,
            'cA':ca_v
        }
        models.Pd.objects.create(**pd_v)
        bjnravg = {
            'bjlx': 0,
            'bjxx': 'A项电压过高'
        }
        bjnravd = {
            'bjlx': 0,
            'bjxx': 'A项电压过低'
        }
        if av_v > 235:
            models.Yjgl.objects.create(**bjnravg)
        elif av_v < 210:
            models.Yjgl.objects.create(**bjnravd)






        # if aa_v <= 210:
        #     bjnravd = {
        #         'bjshij': datetime.datetime.now(),
        #         'bjlx': 0,
        #         'bjxx': 'A项电压过低'
        #     }
        #     models.Yjgl.objects.create(**bjnravd)
        # else:
        #     pass
        #
        # if ba_v >= 235:
        #     bjnrbv = {
        #         'bjshij': datetime.datetime.now(),
        #         'bjlx': 0,
        #         'bjxx': 'B项电压过高'
        #     }
        # elif ba_v <= 210:
        #     bjnrbv = {
        #         'bjshij': datetime.datetime.now(),
        #         'bjlx': 0,
        #         'bjxx': 'B项电压过低'
        #     }
        #     models.Yjgl.objects.create(**bjnrbv)
        # else:
        #     pass
        #
        # if ca_v >= 235:
        #     bjnrcv = {
        #         'bjshij': datetime.datetime.now(),
        #         'bjlx': 0,
        #         'bjxx': 'C项电压过高'
        #     }
        # elif ca_v <= 210:
        #     bjnrcv = {
        #         'bjshij': datetime.datetime.now(),
        #         'bjlx': 0,
        #         'bjxx': 'C项电压过低'
        #     }
        #     models.Yjgl.objects.create(**bjnrcv)
        # else:
        #     pass
        time.sleep(s)

Pdcj(300)
