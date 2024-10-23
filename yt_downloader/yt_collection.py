import json
import os
import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
from pytube.exceptions import LiveStreamError,RegexMatchError
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
                self.videos_list.append(YtVideo(video_id, use_oauth=False))

    def extract_from_url(self,url):
        try:
            resp=requests.get(url,timeout=5)
            resp.raise_for_status()
            url_type=self.recognize_url_type(url)
            yt_page_soup=bs(resp.content.decode('utf-8'),features='lxml')
            with open('test.html','w+',encoding='utf-8') as f:
                f.write(str(resp.content))
            if url_type=='single_vid':
                self.collect_main_video(url)
                self.collect_sidebar_vids(yt_page_soup)
            elif url_type=='channel':
                self.collect_channel_videos(yt_page_soup)
            else:
                raise TypeError(f'Unrecognized or unsupported youtube url type: {url_type}')
        except requests.exceptions.ConnectionError:
            print('Check your internet connection or url')
    
    def collect_main_video(self,url: str) -> None:
        self.videos_list.append(YtVideo(url.split('=')[1].split('&')[0]))

    def collect_sidebar_vids(self,yt_page_soup: bs) -> None:
        data=json.loads(yt_page_soup.select('script')[-5].getText()[20:-1])
        for record in data['contents']['twoColumnWatchNextResults']['secondaryResults']['secondaryResults']['results']:
            try:
                self.videos_list.append(YtVideo(record['compactVideoRenderer']['videoId'],use_oauth=False))
            except KeyError:
                pass
    
    def collect_channel_videos(self,yt_page_soup: bs) -> None:
        #[print(str(i+1),script.getText()[:20]) for i,script in enumerate(yt_page_soup.select('script'))]
        #print(yt_page_soup.select('script')[-6].getText()[20:27])
        whole_script=yt_page_soup.select('script')[-6].getText()
        start=whole_script.find('[{"richItemRenderer":')
        end=whole_script.find('}}] ,')
        print(start,end)
        print(whole_script[end-20:end])
        #data=json.loads(yt_page_soup.select('script')[-6].getText()[20:-1])
        #print(data)

    @staticmethod
    def recognize_url_type(url: str) -> str:
        url_type='unknown'
        if '@' in url:
            url_type='channel'
        elif 'https://www.youtube.com/watch?v=' in url:
            url_type='single_vid'
        return url_type

    def download_all(self,path: str | None = None, prefix: str | None = None, default_path: bool = False) -> None:
        load_dotenv()
        for video in self.videos_list:
            if default_path:
                path=os.path.join(os.getenv('DEFAULT_PATH'),video.author)
            try:          
                video.download(path,prefix)
            except RegexMatchError as e:
                print('Regex issue stopped this one')
                print(e)
            except LiveStreamError as e:
                print(e)
            except OSError as e:
                print(f'Path problem: {e}')