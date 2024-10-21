from django.urls import path
from django.contrib import admin
from index import views

urlpatterns = [
    path('', views.index),
    path('Addr.html', views.addr),
    path('getform.html', views.getform),
    path('logs', views.getform),

]
