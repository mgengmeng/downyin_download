import json
from os import name
from mitmproxy import ctx
# import redis
from icecream import ic
# from utils import *
import uuid
import sys,io
from icecream import ic
from jsonpath import jsonpath 
from pymongo import MongoClient
from collections import OrderedDict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
search_stream='https://aweme.snssdk.com/aweme/v1/general/search/stream/'
search_item='https://aweme.snssdk.com/aweme/v1/search/item'
MONGO_URL = 'localhost:27017'
MONGO_DB = 'douyin'
MONGO_TABLE = 'user_video'

client = MongoClient(MONGO_URL)
db = client[MONGO_DB]

def response(flow):    
    if flow.request.url.startswith(search_item):
        text = flow.response.text
        data = json.loads(text)
        aweinfo=jsonpath(data,'$..aweme_info')
        for _ in aweinfo:
            title=_['desc']
            ic(title)
            url_list=_['video']['play_addr']['url_list']
            ic(url_list)
            db[MONGO_TABLE].insert({'title':title,'url_list':url_list})
