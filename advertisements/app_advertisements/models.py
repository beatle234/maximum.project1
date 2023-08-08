from django.db import models

# Create your models here.
class Advertisement(models.Model):
     title = models.CharField('заголовок', max_length=128)
     description = models.TextField('описaние')
     price = models.DecimalField('цена', max_digits=10, decimal_places=2)
     auction = models.BooleanField('торг', help_text='Oтметьте, если торг уместен')
     created_ad = models.DateTimeField(auto_now_add=True)
     update_ad = models.DateTimeField(auto_now=True)