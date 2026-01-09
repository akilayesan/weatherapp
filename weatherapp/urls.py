from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary, name='weathersimple'),
    path('alldata/', views.alldata, name='alldata'),
]
