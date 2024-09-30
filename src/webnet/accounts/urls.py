from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('login/', views.login),
    path('reg/', views.register),
    path('logout/', views.logout),
]
