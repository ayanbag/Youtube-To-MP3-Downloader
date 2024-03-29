import sys
import os
import traceback
import youtube_dl


dir_name="Downloaded Songs"
def make_savepath(title, artist, savedir=dir_name):
        return os.path.join(savedir, "%s--%s.mp3" % (title, artist))
def main_dw(url):
    options={
        'format':'bestaudio/best',
        'extractaudio':True,
        'audioformat' : "mp3",      
        'outtmpl': '%(id)s',       
        'noplaylist' : True,
    }
    dwld=youtube_dl.YoutubeDL(options)
    dl=youtube_dl.YoutubeDL()
    info=None
    with dl:
        info=dl.extract_info(url,download=False)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    savepath = make_savepath(info['title'], info['uploader'])
    try:
        result = dwld.extract_info(url,download=True)
        os.rename(result['id'], savepath)
        qw=savepath
        return qw

    except Exception:
        qw=""
        return(qw)


if __name__=="__main__":
    main()