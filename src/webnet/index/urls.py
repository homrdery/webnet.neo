from django.urls import path
from django.contrib import admin
from index import views

urlpatterns = [
    path('', views.index, views.addr),
    path('Addr.html', views.addr),
    path('getform.html', views.getform),

]
