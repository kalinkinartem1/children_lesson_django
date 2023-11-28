from django.urls import path
# from .views import *
from app import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls)
]
