import json
import os
import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
from pytube.exceptions import RegexMatchError
from yt_video import YtVideo

class YtCollection:
    def __init__(self):
        self.videos_list=[]

    def __str__(self):
        if self.videos_list:
            lista=''
            for video in self.videos_list:
                lista+='='*20+'\n'+str(video)+'\n'
            return lista
        else:
            return 'No videos here'
        
    def extract_from_file(self,filename: str ='test.html'):
        with open(fr'yt_downloader/{filename}','r',encoding='utf-8') as f:
            yt_page_soup=bs(f.read(),'html.parser')

            for video_soup in yt_page_soup.select('ytd-compact-video-renderer'):
                video_id = video_soup.select_one('a.yt-simple-endpoint').get('href').split('=')[1]
                self.videos_list.append(YtVideo(video_id))

    def extract_from_url(self,url):
        resp=requests.get(url,timeout=5)
        resp.raise_for_status()
        yt_page_soup=bs(resp.content.decode('utf-8'),features="lxml")
        data=json.loads(yt_page_soup.select('script')[-5].getText()[20:-1])
        for record in data['contents']['twoColumnWatchNextResults']['secondaryResults']['secondaryResults']['results']:
            try:
                self.videos_list.append(YtVideo(record['compactVideoRenderer']['videoId']))
            except KeyError:
                pass

    def download_all(self,path: str | None = None, prefix: str | None = None, default_path: bool = False) -> None:
        load_dotenv()
        for video in self.videos_list:
            if default_path:
                path=os.path.join(os.getenv('DEFAULT_PATH'),video.author)
                print(path)
            try:          
                video.download(path,prefix)
            except RegexMatchError:
                print("Regex issue stopped this one")