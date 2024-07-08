import requests
from bs4 import BeautifulSoup as bs
from yt_collection import YtCollection

lista = YtCollection()
#lista.extract_from_file()
lista.extract_from_url('https://www.youtube.com/watch?v=4rC7yMarESw&ab_channel=Aliensrock')
lista.download_all(default_path=True)