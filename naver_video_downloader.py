# from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import re
import youtube_dl

def download_single_video(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print('Finish!')

def download_all_videos(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    urls = soup.find_all('a', attrs = {'data-event' : "moveAnotherClipByUser"})
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for i in urls:
            # print(i['title'])
            ydl.download([i['href']])
    print('Finish!')

if __name__ == "__main__" :
    import argparse
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("url", type=str, help="Input url")
    group.add_argument('--vapp', '-v', action='store_true', help='Download v-app video')
    group.add_argument('--naver_tv_single', '-nts', action='store_true', help='Download all the videos in the naver_tv playlist.')
    group.add_argument('--naver_tv_all', '-nta', action='store_true', help='Download single naver_tv video.')
    args = parser.parse_args()
    if args.vapp or args.naver_tv_single:
        download_single_video(args.url)
    elif args.naver_tv_all:
        download_all_videos(args.url)
