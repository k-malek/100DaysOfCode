from bs4 import BeautifulSoup as bs
from yt_video import YtVideo

class YtPlaylist:
    def __init__(self):
        self.videos_list=[]

    def __str__(self):
        if self.videos_list:
            lista=''
            for video in self.videos_list:
                lista+='='*20+'\n'+str(video)+'\n'
            return lista
        else:
            return 'The playlist is empty'
        
    def extract_from_file(self,filename: str ='test.html'):
        with open(fr'yt_downloader/{filename}','r',encoding='utf-8') as f:
            yt_page_soup=bs(f.read(),'html.parser')

        for video_soup in yt_page_soup.select('ytd-compact-video-renderer'):
            video_id = video_soup.select_one('a.yt-simple-endpoint').get('href').split('=')[1]
            self.videos_list.append(YtVideo(video_id))

    def download_all(self,path: str | None = None, prefix: str | None = None) -> None:
        for video in self.videos_list:
            video.download(path,prefix)