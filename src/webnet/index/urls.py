from django.urls import path
from django.contrib import admin
from index import views
from logs.views import logs
urlpatterns = [
    path('', views.index),
    path('Addr.html', views.addr),
    path('getform.html', views.getform),
    path('logs', logs),

]
