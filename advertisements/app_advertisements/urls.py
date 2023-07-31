from django.urls import path
from .views import index, lesson4

urlpatterns =[
    path('', index),
    path('lesson4/', lesson4)
]
