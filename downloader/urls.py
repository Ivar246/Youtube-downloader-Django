from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.downloads),
    path('home/download/', views.yt_download, name='yt_download')
]
