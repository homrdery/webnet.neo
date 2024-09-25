from django.urls import path
from django.contrib import admin
from index import views

urlpatterns = [
    path('', views.index),
]
