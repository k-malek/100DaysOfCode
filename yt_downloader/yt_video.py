#from time import *
import os
from typing import Any, Callable, Dict
#from bs4 import BeautifulSoup as bs
import pytube as pt
#import urllib.request, re, math, os


class YtVideo(pt.YouTube):

    def __init__(self,
                 video_id: str, 
                 on_progress_callback: Callable[[Any, bytes, int], None] | None = None, 
                 on_complete_callback: Callable[[Any, str | None], None] | None = None, 
                 proxies: Dict[str, str] = None, 
                 use_oauth: bool = False,
                 allow_oauth_cache: bool = True):
        yt_url = video_id if 'youtube' in video_id else 'https://www.youtube.com/watch?v='+video_id 
        super().__init__(yt_url, on_progress_callback, on_complete_callback, proxies, use_oauth, allow_oauth_cache)

    def __str__(self) -> str:
        return f'Title: {self.title}\nChannel: {self.author}\nLength: {self.make_formatted_length()}'

    def download(self,path: str | None = None, prefix: str | None = None) -> None:
        print("I download for U:",self.title)
        if not ':\\' in path:
            path=os.path.join(os.getcwd(),path)
        filename=f'{self.make_stripped_title()}.mp4'
        if prefix:
            filename=f'{prefix}_{filename}'
        self.streams.get_highest_resolution().download(output_path=path,filename=filename)
        print('DONE!')

    def make_formatted_length(self) -> str:
        result=''
        temp_length=self.length
        hours=temp_length//3600
        temp_length-=hours*3600
        minutes=temp_length//60
        temp_length-=minutes*60
        seconds=temp_length
        result+=f' {hours}h' if hours else ''
        result+=f' {minutes}min' if minutes else ''
        result+=f' {seconds}s' if seconds else ''
        return result

    def make_stripped_title(self) -> str:
        forbidden_characters=['|','"','!','?','.','/']
        temp_title=self.title
        for char in forbidden_characters:
            if char in temp_title:
                temp_title=temp_title.replace(char,'')
        return temp_title


# #download single vid
# def pobier(lunk,path=None,prefix=None):
#     global all
#     global elapsed_time
#     global now
#     all=0
#     elapsed_time=0
#     now=time()
#     if 'youtube' not in lunk:
#         lunk = 'https://www.youtube.com/watch?v='+lunk
#     try:
#         vid=YouTube(lunk, on_progress_callback=progress_check)
#         print("I download for U:",vid.title)            
#         if path and prefix:
#             strim=vid.streams.get_highest_resolution().download(output_path=path,filename=str(prefix)+vid.title.replace('|','#').replace('!','').replace('?','')+'.mp4')
#         elif path:
#             strim=vid.streams.get_highest_resolution().download(output_path=path,filename=vid.title.replace('|','#').replace('!','').replace('?','')+'.mp4')
#         else:
#             strim=vid.streams.get_highest_resolution().download()
#         print("100.00%")
#     except Exception as e:
#         print("Somethin went horribly rong :<")
#         print(e)

# #download playlist        
# def pobier_liste(link_listy, list_name='moja_lista', channel=None, enum=False, ile=1000):
#     x = urllib.request.urlopen(link_listy).read()
#     x = re.findall(r'"videoId":"([^"]*)"',x.decode("utf-8"))
#     all_vid=len(x)
#     pobrane=set()
#     curr_path=os.getcwd()
#     if channel:
#         curr_path=os.path.join(curr_path,channel)
#         if not os.path.exists(curr_path):
#             os.mkdir(curr_path)
#     path=os.path.join(curr_path,list_name)
#     if not os.path.exists(path):
#         os.mkdir(path)
#     for i,vid in enumerate(x):
#         print(str(len(pobrane)+1)+"/"+str(all_vid),end=" ")
#         if vid in pobrane:
#             all_vid-=1
#             continue
#         if i<int(ile):
#             if enum:
#                 pobier(vid,path=path,prefix=str(len(pobrane)+1)+"_")
#             else:
#                 pobier(vid,path=path)
#             pobrane.add(vid)
#         else: 
#             break

# #download videos from channel            
# def pobier_kanal(link,channel_name,ile=5):
#     vids={}
#     curr_path=os.getcwd()
#     path=curr_path+r"/"+channel_name
#     if not os.path.exists(path):
#         os.mkdir(path)
#     x = urllib.request.urlopen(link).read()
#     with open('test.html','w+') as f:
#         f.write(str(x))
#     print(bs(x, "html.parser").find("a", {"id": "video-title-link"}))
#     soup = bs(x, "html.parser")
#     for a in soup.find_all('a', href=True):
#         if a['href'].startswith(r'/watch'):
#             vid.add(a['href'].split('=')[1])        
#     all_vid=len(vids)
#     pobrane=[]
#     for i,vid in enumerate(vids):
#         print(str(i+1)+"/"+str(all_vid),end=" ")
#         if vid in pobrane:
#             continue
#         if i<int(ile): 
#             pobier(vid)
#             pobrane.append(vid)
#         else: 
#             break
            
# #progress percentage visualization
# def progress_check(stream = None, chunk = None, file_handle = None, remaining = None):
#     global all
#     global elapsed_time
#     global now
#     all+=len(chunk)
#     elapsed_time+=time()-now
#     now=time()
#     percent=all/stream.filesize*100
#     remaining_time=(elapsed_time*100/percent)*((100-percent)/100)
#     hours=int(remaining_time/3600)
#     minutes=int((remaining_time-hours*3600)/60)
#     seconds=int(remaining_time-hours*3600-minutes*60)
#     strokes_for_bar=math.floor(percent//5)
#     print("{:.2f}% [".format(percent)+"="*strokes_for_bar+"-"*(20-strokes_for_bar)+"] passed {}s, ETA app. {}h {}min {}s         ".format(int(elapsed_time),hours,minutes,seconds), end='\r')