import os
import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
from yt_collection import YtCollection
from pytube. innertube import _default_clients

_default_clients[ "ANDROID"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients[ "ANDROID_EMBED"][ "context"][ "client"]["clientVersion"] = "19.08.35"
_default_clients[ "IOS_EMBED"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"][ "context"]["client"]["clientVersion"] = "6.41"
_default_clients[ "ANDROID_MUSIC"] = _default_clients[ "ANDROID_CREATOR" ]
load_dotenv()

lista = YtCollection()
#lista.extract_from_file()
lista.extract_from_url(os.getenv('URL'))
lista.download_all(default_path=True)