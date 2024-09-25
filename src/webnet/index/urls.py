from django.urls import path
from django.contrib import admin
import rest
from index import views

urlpatterns = [
    path('/', views.index),
]
