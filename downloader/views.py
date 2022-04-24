from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .action import download_sucessful
import urllib
# Create your views here.
def downloads(request):
    return render(request, 'downloader.html')


def yt_download(request):
    if request.method == 'GET':
        link = request.GET['link']
        
        
    return render(request, 'yt_download.html')
        