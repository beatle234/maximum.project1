from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
     title = models.CharField('заголовок', max_length=128)
     description = models.TextField('описaние')
     price = models.DecimalField('цена', max_digits=10, decimal_places=2)
     auction = models.BooleanField('торг', help_text='Oтметьте, если торг уместен')
     created_ad = models.DateTimeField(auto_now_add=True)
     update_ad = models.DateTimeField(auto_now=True)
     user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
     image = models.ImageField('изображение', upload_to='advertisements/')

     @admin.display(description='дата создания')
     def created_date(self):
          from django.utils import timezone
          if self.created_ad.date() == timezone.now().date():
               created_time = self.created_ad.time().strftime('%H:%M:%S')
               return format_html(
                    '<span style="color: green; font-weight:bold;">Сегодня в {}</span>', created_time
               )
          return self.created_ad.strftime('%d.%m.%Y в %H:%M:%S')

     @admin.display(description='дата последнего обновления')
     def updated_date(self):
         from django.utils import timezone
         if self.update_ad.date() == timezone.now().date():
             created_time = self.update_ad.time().strftime('%H:%M:%S')
             return format_html(
                 '<span style="color: green; font-weight:bold;">Сегодня в {}</span>', created_time
             )
         return self.update_ad.strftime('%d.%m.%Y в %H:%M:%S')

     @admin.display(description='фото')
     def get_html_image(self):
         if self.image:
             return format_html(
                 '<img scr="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
             )

     def __str__(self):
          return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

     class Meta:
          db_table = 'advertisements'