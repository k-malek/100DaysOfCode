import requests
from bs4 import BeautifulSoup as bs
from yt_playlist import YtPlaylist

lista = YtPlaylist()
lista.extract_from_file()
lista.download_all(path='new')
