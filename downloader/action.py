from pytube import YouTube

def download_sucessful(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        stream.order_by('reslution').desc().first().download('/home/ivar/Downloads')
        return True
    except Exception as e:
        return False

