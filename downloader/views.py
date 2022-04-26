from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .action import download_sucessful
import urllib
# Create your views here.
def downloads(request):
    return render(request, 'downloader.html')


def yt_download(request):
    if request.method == 'GET':
        link = request.GET['link']
        a = download_sucessful(link) # return boolean
        print(a)
        if a:
            return render(request, 'yt_download.html', {
                'download_sucessful': True
            })
        else:
            return render(request, 'yt_download.html', {
            'download_sucessful': False
        })
