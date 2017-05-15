from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import re
import youtube_dl

if __name__ == "__main__" :
    url = input('url: ') # ex: http://tv.naver.com/v/1519505
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    urls = soup.find_all('a', attrs = {'data-event' : "moveAnotherClipByUser"})
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for i in urls:
            ydl.download([i['href']])

    print('end')
