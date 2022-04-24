from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.downloads),
    path('download', views.yt_download, name='yt_download')
]
