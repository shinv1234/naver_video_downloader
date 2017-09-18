from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import re
import youtube_dl

if __name__ == "__main__" :
    url = input('url: ') # ex: http://tv.naver.com/v/1519505
    txt = '''Input '0' if you want to download single video and Input '1' if you want to download all videos in list.: '''
    single_or_all = int(input(txt))
    ydl_opts = {}
    if single_or_all == 0:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    if single_or_all == 1:
        res = requests.get(url)
        soup = BeautifulSoup(res.text)
        urls = soup.find_all('a', attrs = {'data-event' : "moveAnotherClipByUser"})
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for i in urls:
                print(i)
                ydl.download([i['href']])

    print('end')
