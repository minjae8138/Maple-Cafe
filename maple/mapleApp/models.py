from django.db import models
from django.utils import timezone
# Create your models here.


#----------------------< 공통 >----------------------
class SampleProduct(models.Model):
    pd_name = models.CharField(max_length=100)
    pd_price = models.IntegerField(default=0)




#----------------------< 김민재 >----------------------
class mapleProduct(models.Model) :
    mp_name = models.CharField(max_length=100)
    mp_price = models.IntegerField(default=0)
    mp_count = models.IntegerField(default=0)
#----------------------< 심영석 >----------------------

#----------------------< 박우환 >----------------------

#----------------------< 오은영 >----------------------

#----------------------< 정연욱 >----------------------

#----------------------< 최유숙 >----------------------


