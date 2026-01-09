from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary, name='weathersimple'),
    path('forecast/', views.forecast, name='forecast'),
    path('alldata/', views.alldata, name='alldata'),
]
